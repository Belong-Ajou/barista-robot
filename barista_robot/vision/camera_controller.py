import cv2
import numpy as np
import os
from defisheye import Defisheye
import time
from PIL import Image

import pyk4a
from pyk4a import Config, PyK4A

from typing import Optional, Tuple

d_path = 'data'

def colorize(
    image: np.ndarray,
    clipping_range: Tuple[Optional[int], Optional[int]] = (None, None),
    colormap: int = cv2.COLORMAP_HSV,
) -> np.ndarray:
    if clipping_range[0] or clipping_range[1]:
        img = image.clip(clipping_range[0], clipping_range[1])  # type: ignore
    else:
        img = image.copy()
        
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    img = cv2.applyColorMap(img, colormap)
    
    return img

def main():
    k4a = PyK4A(
        Config(
            color_format=pyk4a.ImageFormat.COLOR_BGRA32,
            color_resolution=pyk4a.ColorResolution.RES_2160P,
            depth_mode=pyk4a.DepthMode.WFOV_UNBINNED,
            camera_fps=pyk4a.FPS.FPS_15,
            synchronized_images_only=True,
        )
    )
    k4a.start()

    # getters and setters directly get and set on device
    # k4a.whitebalance = 4500
    # assert k4a.whitebalance == 4500

    idx = 41
    while 1:
        capture = k4a.get_capture()
        if np.any(capture.color) and np.any(capture.depth):
            color_img = capture.color[:, :, :3]
            depth_img = capture.depth

            # Getting depth image array
            np.set_printoptions(threshold=np.inf)
            with open("depth_image.txt", "w") as file:
                depth_img_str = np.array2string(depth_img, separator=',')
                file.write(depth_img_str)
            np.set_printoptions(threshold=1000)


            dtype = 'linear'
            format = 'fullframe'
            fov = 180
            pfov = 120

            img_out = f"./defish_depth_array.jpg"

            array_out = []

            # for row in depth_img:
            #     for column in row:
            #         array_out.append([column, column, column])

            # Reshape depth_img to have a third dimension of size 1
            depth_img_reshaped = depth_img.reshape(depth_img.shape[0], depth_img.shape[1], 1)

            # Replicate the values across the third dimension
            array_out = np.repeat(depth_img_reshaped, 3, axis=2)

            print("done array out")

            depth_img = array_out

            print("obj shape:", depth_img.shape)

            obj = Defisheye(depth_img, dtype=dtype, format=format, fov=fov, pfov=pfov)

            # To save image locally 
            obj.convert(outfile=img_out)

            # To use the converted image in memory
            new_image = obj.convert()

            # np.set_printoptions(threshold=np.inf)
            # with open("obj_depth_image.txt", "w") as file:
            #     obj_img_str = np.array2string(new_image, separator=',')
            #     file.write(obj_img_str)
            # np.set_printoptions(threshold=1000)

            # print("done writing obj depth array")

            # Cropping image
            crop_coordinates = (175, 720, 45, 1020)  # Adjust these values as needed

            # Crop the image using NumPy slicing
            y_min, y_max, x_min, x_max = crop_coordinates
            cropped_image = new_image[y_min:y_max, x_min:x_max]
            print("cropped_image",cropped_image)
            print("cropped_image.shape", cropped_image.shape)

            # Resize the image using cv2.resize
            # cv2.INTER_NEAREST is often used for depth images to avoid introducing new depth values through interpolation
            resized_image = cv2.resize(cropped_image, (640, 640), interpolation=cv2.INTER_NEAREST)
            print("resized_image:", resized_image)
            print("resized_image.shape:", resized_image.shape)

            # Select one channel from the 3D array. Assuming all channels have the same value, we can just take the first.
            resized_image_2d = resized_image[:, :, 0]

            resized_image_2d_colorized = colorize(resized_image_2d, (None, 10000), cv2.COLORMAP_HSV)

            # Now save this 2D array to a CSV file, visualise and save the image too
            np.savetxt("./real_depth_resized_image_array.csv", resized_image_2d, fmt='%d', delimiter=',')
            cv2.imwrite('resized_image_2d_colorized.jpg', resized_image_2d_colorized)

            # find bounding box
            # bounding_boxes = detect_objects(captured_image)

            # 윈도우 창의 이름을 지정
            cv2.namedWindow('color', cv2.WINDOW_NORMAL)
            cv2.namedWindow('depth', cv2.WINDOW_NORMAL)

            # 윈도우 창의 크기를 조정
            cv2.resizeWindow('color', 800, 600)  # 원하는 크기로 조절
            cv2.resizeWindow('depth', 800, 600)  # 원하는 크기로 조절
            
            # 이미지를 윈도우 창에 표시
            cv2.imshow('color', color_img)

            depth2_img = colorize(depth_img, (None, 5000), cv2.COLORMAP_HSV)
            cv2.imshow("depth", depth2_img)

            cv2.imwrite('color.jpg', color_img)
            cv2.imwrite('depth.jpg', depth2_img)
            
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord(' '):
                print("Saving image ", idx)
                os.makedirs(d_path, exist_ok=True)
                
                fname1 = 'orgimg_' + str(idx) + '.jpg'
                out_1 = os.path.join(d_path, fname1)
                cv2.imwrite(out_1, color_img)

                fname2 = 'orgdepth_' + str(idx) + '.png'
                out_2 = os.path.join(d_path, fname2)
                cv2.imwrite(out_2, depth2_img)
                
                idx += 1
        time.sleep(5)
            
    cv2.destroyAllWindows()
    k4a.stop()

def capture_image():
    k4a = PyK4A(
        Config(
            color_format=pyk4a.ImageFormat.COLOR_BGRA32,
            color_resolution=pyk4a.ColorResolution.RES_1080P,
            depth_mode=pyk4a.DepthMode.WFOV_UNBINNED,
            #depth_mode=pyk4a.DepthMode.OFF,
            camera_fps=pyk4a.FPS.FPS_15,
            synchronized_images_only=True,
        )
    )
    k4a.start()

    i = 0
    while 1:
        capture = k4a.get_capture()
        if np.any(capture.color):
            color_img = capture.color[:, :, :3]

            # Resize color_img to 640x640
            resized_color_img = cv2.resize(color_img, (640, 640))

            k4a.stop()
            return resized_color_img
        else:
            i = i + 1
            print('Retry Count : ' + i)
    
    k4a.stop()

if __name__ == "__main__":
    main()