from PIL import Image
from ultralytics import YOLO
import vision.camera_controller as AK
import numpy as np

class Vision:
    def __init__(self, path):
        #학습한 pt파일을 불러온다
        self.model = YOLO(path)
        self.conf = 0.3 # 인식 Confidence. 수정 가능
        self.Object_Region = {}
        self.Reward_Value = np.array([-20, -20, 20, 20]) # Object_Region 넓혀주는 보상 값. 수정 가능
    
    def Set_Object_Region(self, path = ""):
        results = self.Object_Detect(path)

        # 시각화
        for r in results:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            im.show()  # show image
            im.save("./image_result_box.jpg", "JPEG")
        
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

        return
    
    def Check_Object_Position(self, path = ""):
        results = self.Object_Detect(path)

        boxes = results[0].boxes
        paired_boxes = [pair for pair in zip(boxes.xyxy.cpu().detach().numpy(), boxes.conf.cpu().detach().numpy(), boxes.cls.cpu().numpy()) if pair[1] >= self.conf and pair[2] != 2]

        result_dict = {}
        for box in paired_boxes:
            class_name = self.model.names[box[2]]
            box_array = box[0]

            if (class_name in result_dict.keys()):
                continue
            else:
                for array in self.Object_Region[class_name]:
                    if box_array[0] >= array[0] and box_array[1] >= array[1] and box_array[2] <= array[2] and box_array[3] <= array[3]:
                        indices = np.where(np.all(self.Object_Region[class_name] == array, axis=1))
                        result_dict[class_name] = int(indices[0])

        # temp_result_dict = {'Cup' : 3, 'Dripper' : 2}
        return result_dict
    
    def Object_Detect(self, path):
        if (path == ""):
            img = AK.capture_image()
            pil_img = Image.fromarray(np.array(img)[:, :, [2, 1, 0]]) # BGR Image를 RGB로 변환
            results = self.model([pil_img])
        else:
            results = self.model(path)  # results list
        return results

# from barista_basic import BaristaBasic

# class BaristaVision(BaristaBasic):
#     def _rinse(self):
#         print("Check dripper, cup")
#         vision_model = Vision(r'./barista_robot/best.pt')
#         vision_model.Set_Object_Region()
#         result = vision_model.Check_Object_Position()
#         print(f"Vision result:{result}")
#         self.set_cup_location(result['Cup'])
#         self.set_dripper_location(result['Dripper'])
#         print("Rinse the coffee filter paper.")
#         super()._rinse()
#         return
    
if __name__ == "__main__":
    mode = "Debug"
    # mode = "Release"
    if mode == "Debug":
        # barista.robot.activate_gripper()
        # barista.robot.set_global_speed(50)
        # barista.robot.set_speed(5.0)
        # barista.set_cup_location(1)
        # barista.set_dripper_location(2)
        # barista._pour(1,1)
        vision_model = Vision(r'./barista_robot/best.pt')
        vision_model.Set_Object_Region()
        result = vision_model.Check_Object_Position()
        print(result)
    # else: 
        # my_recipe = [["bloom", 0, 0], ["pour", 10, 90]]
        # barista = BaristaVision("192.168.58.2")
        # barista.make_coffee(my_recipe)