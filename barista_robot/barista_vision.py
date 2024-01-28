from PIL import Image
from ultralytics import YOLO
import vision.camera_controller as AK
import numpy as np
from barista_basic import BaristaBasic
from math import *

class BaristaVision(BaristaBasic):
    def __init__(self, path, ip):
        # super().__init__(ip)
        #학습한 pt파일을 불러온다
        self.model = YOLO(path)
        self.conf = 0.3 # 인식 Confidence. 수정 가능
        self.Object_Region = {}
        self.Reward_Value = np.array([-20, -20, 20, 20]) # Object_Region 넓혀주는 보상 값. 수정 가능
        
        #known from measurement. 
        self.x_cam = 54 # x axis Distance between camera and robot
        self.y_cam = -38 # y axis Distance between camera and robot
        self.pitch_cam = 41*pi/180 # 
        self.yaw_cam = 30*pi/180
    
    def Set_Object_Region(self, path = ""):
        #results = self.Object_Detect(path)
        results, depth_results = self.Object_Detect(path)

        # 시각화
        for r in results:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            im.show()  # show image
        
        boxes = results[0].boxes
        paired_boxes = [pair for pair in zip(boxes.xyxy.cpu().detach().numpy(), boxes.conf.cpu().detach().numpy(), boxes.cls.cpu().numpy()) if pair[1] >= self.conf and pair[2] != 2]
        sorted_boxes = sorted(paired_boxes, key=lambda x: x[0][0], reverse=False) # x좌표로 오름차순 정렬
        for box in sorted_boxes:
            class_name = self.model.names[box[2]]
            Box_Rewarded = [x+y for x,y in zip(box[0], self.Reward_Value)] #영역 넓혀주기
            if (class_name in self.Object_Region.keys()):
                temp_arr = self.Object_Region[class_name]
                self.Object_Region[class_name] = np.append(temp_arr, [Box_Rewarded], axis=0)
            else:
                self.Object_Region[class_name] = [Box_Rewarded]
        
        for box in sorted_boxes:
            class_name = self.model.names[box[2]]
            if (class_name == "Cup"):
                box_array = box[0]

                # Extracting top-left (X1, Y1) and bottom-right (X2, Y2) coordinates of the bounding box
                x1, y1, x2, y2 = box_array[:4]
                # cropped_distance_array = depth_results[y1:y2, x1:x2]
                # Optionally, you can calculate the center coordinates
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2

                print(f"Object: {class_name}, Coordinates: Top-Left({x1}, {y1}), Center({center_x}, {center_y}), Bottom-Right({x2}, {y2})")
                self.Calculate_ObjectPosition_Ref_Robot(depth_results[round(y2), round(center_x)])
                break

        return
    
    def Check_Object_Position(self, path = ""):
        #results = self.Object_Detect(path)
        results, depth_results = self.Object_Detect(path)

        boxes = results[0].boxes
        paired_boxes = [pair for pair in zip(boxes.xyxy.cpu().detach().numpy(), boxes.conf.cpu().detach().numpy(), boxes.cls.cpu().numpy()) if pair[1] >= self.conf and pair[2] != 2]
        sorted_boxes = sorted(paired_boxes, key=lambda x: x[0][0], reverse=False) # x좌표로 오름차순 정렬
        result_dict = {}
        for box in sorted_boxes:
            class_name = self.model.names[box[2]]
            box_array = box[0]

            if (class_name in result_dict.keys()):
                continue
            else:
                for array in self.Object_Region[class_name]:
                    if box_array[0] >= array[0] and box_array[1] >= array[1] and box_array[2] <= array[2] and box_array[3] <= array[3]:
                        indices = np.where(np.all(self.Object_Region[class_name] == array, axis=1))
                        result_dict[class_name] = int(indices[0]) + 1

        # temp_result_dict = {'Cup' : 3, 'Dripper' : 2}
        return result_dict
    
    def Object_Detect(self, path):
        if (path == ""):
            img, depth_img = AK.capture_image_ver2()
            # img = AK.capture_image()
            pil_img = Image.fromarray(np.array(img)[:, :, [2, 1, 0]]) # BGR Image를 RGB로 변환
            results = self.model([pil_img])
        else:
            results = self.model(path)  # results list
        return results, depth_img
    
    def Calculate_ObjectPosition_Ref_Robot(self, distance):
        #known from camera
        cup_to_camera_distance = distance

        # #known from measurement
        # x_cam = 54 # 
        # y_cam = -38
        # pitch_cam = 60*pi/180
        # yaw_cam = 72*pi/180

        def get_x(x_cam, y_cam, cup_to_camera_distance, pitch_cam):
            x = x_cam - cup_to_camera_distance*cos(pitch_cam)*cos(self.yaw_cam)
            return x

        def get_y(x_cam, y_cam, cup_to_camera_distance, pitch_cam):
            y = y_cam + cup_to_camera_distance*cos(pitch_cam)*sin(self.yaw_cam)
            return y

        cup1_posx = get_x(self.x_cam, self.y_cam, cup_to_camera_distance, self.pitch_cam)
        cup1_posy = get_y(self.x_cam, self.y_cam, cup_to_camera_distance, self.pitch_cam)
        cup2_posx = cup1_posx - 1.5 
        cup2_posy = cup1_posy + 14
        cup3_posx = cup1_posx - 3
        cup3_posy = cup1_posy + 29

        print("CUP 1 position: (" + "%.2f" %cup1_posx + ", " + "%.2f" %cup1_posy  + ")")
        print("CUP 2 position: (" + "%.2f" %cup2_posx + ", " + "%.2f" %cup2_posy + ")")
        print("CUP 3 position: (" + "%.2f" %cup3_posx + ", " + "%.2f" %cup3_posy + ")")
    
    def _rinse(self):
        print("Check dripper, cup")
        result = self.Check_Object_Position()
        print(f"Vision result:{result}")
        self.set_cup_location(result['Cup'])
        self.set_dripper_location(result['Dripper'])
        print("Rinse the coffee filter paper.")
        super()._rinse()
        return
    
if __name__ == "__main__":
    mode = "Debug"
    #mode = "Release"
    if mode == "Debug":
        # barista.robot.activate_gripper()
        # barista.robot.set_global_speed(50)
        # barista.robot.set_speed(5.0)
        # barista.set_cup_location(1)
        # barista.set_dripper_location(2)
        # barista._pour(1,1)
        vision_model = BaristaVision(r'./barista_robot/best.pt', "192.168.58.2")
        vision_model.Set_Object_Region()
        result = vision_model.Check_Object_Position()
        print(result)
    else: 
        my_recipe = [["bloom", 0, 0], ["pour", 10, 90]]
        barista = BaristaVision(r'./barista_robot/best.pt', "192.168.58.2")
        barista.Set_Object_Region()
        barista.make_coffee(my_recipe)