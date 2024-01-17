import cv2
import numpy as np
import os

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

            # 윈도우 창의 이름을 지정
            cv2.namedWindow('color', cv2.WINDOW_NORMAL)
            cv2.namedWindow('depth', cv2.WINDOW_NORMAL)

            # 윈도우 창의 크기를 조정
            cv2.resizeWindow('color', 800, 600)  # 원하는 크기로 조절
            cv2.resizeWindow('depth', 800, 600)  # 원하는 크기로 조절
            
            # 이미지를 윈도우 창에 표시
            cv2.imshow('color', color_img)
            cv2.imshow("depth", colorize(depth_img, (None, 5000), cv2.COLORMAP_HSV))
            
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
                cv2.imwrite(out_2, depth_img)
                
                idx += 1
            
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