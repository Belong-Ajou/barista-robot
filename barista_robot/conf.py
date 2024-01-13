home_point = \
    {
        "J": [0.000, -90.009, -89.968, -180.013, 0.005, -0.005],
        "P": [240.054, -202.000, 318.097, 90.000, -0.004, -0.005]
    }
grab_cup_point = \
    {
        # # 1.PTP - 원두 컵 앞에 위치 (Locate in front of the cup of coffee beans)
        # # "J1": [-6.117, -112.227, -123.535, -125.78, -20.499, 0.980],
        # "P1": [250.732, -223.656, 97.368, 90.578, 0.566, 14.382], #X,Y,Z,RX,RY,RZ
        # # 2.Linear - 원두 컵쪽으로 들어가기 (Move forward to the cup)
        # # "J2": [-23.961, -122.697, -102.762, -135.443, -39.093, 3.807],
        # "P2": [275.260, -318.871, 101.532, 90.575, 0.276, 15.132],
        # # 3.Linear - 원두 컵 잡기 위해 올림 (Move up to grab the cup)
        # # "J3": [-25.959, -119.019, -98.106, -143.677, -39.189, 0.259],
        # "P3": [275.267, -318.877, 141.386, 90.572, -3.104, 15.099],
        # 4.Linear - 잡은 뒤 컵 올리기 (Pick up the cup)
        # "J4": [-26.107, -120.769, -20.516, -219.518, -39.336, 0.255],
        # "P4": [273.503, -333.754, 427.799, 90.507, 0.368, 13.229],
        
        "CUP_X_OFFSET" : 150.0,
        # 1. 원두 컵 잡기 위해 위치
        "P1": [10.708, -311.978, 397.799, 90.814, -2.741, 1.904],
        # 2. 원두 컵 잡는 위치
        "P2": [10.708, -311.978, 145.404, 90.814, -2.741, 1.904],   
    }
locate_coffee_ground_point = \
    {
        # 1.Linear - 붓기 전, 드리퍼 위에 위치시키기 (Locate the cup over the dripper)
        "P1": [308.879, 193.313, 439.094, 91.684, -0.485, 76.794],
        # y1:210.554 y2: 38.756, y3: -110.367
        # 2.PTP - 붓기 위해 위치 조정 (Adjust the coordinates to pour it)
        "P2": [322.207, 233.598, 416.727, 92.871, 24.334, 60.556],
        # 3.PTP - 원두 붓기 (Pour it)
        "P3": [322.207, 233.597, 416.727, -92.871, 35.590, -122.505],
        "DRIPPER_Y_OFFSET": -153.2 
    }

place_used_cup_point = \
    {
        # 1. PTP - 사용한 컵 두기 위한 위치로 이동
        "P1" : [58.716, 334.624, 406.727, 90.676, -0.29, 152.164],
        # 2. Linear - 사용한 컵 두기(z축 이동)
        "P2" : [58.716, 334.624, 255.555, 90.676, -0.29, 152.164]
    }

grab_kettle_point = \
    {
        # 1. 주전자 잡기 위한 위치로 이동 
        "P1" : [194.500, 243.314, 155.473, -157.019, 88.510, -115.259],
        # 2. 주전자 손잡이 위치로 이동 hardcoding10n1
        "P2" : [331.596, 376.371, 150.684, -157.081, 88.444, -115.318],
        # 3. 주전자 들어올리기 hardcoding10n2
        "P3" : [331.596, 376.371, 327.328 , -157.081, 88.444, -115.318],
        # 4. 드리퍼 가기 전 위치 
        "P4" : [233.034, 158.849, 506.158, 0.503, 85.955, 58.024]  
    }

brewing_program = \
    {
        "recipe1_1" : "brewing1",
        "recipe1_2" : "brewing2",
        "recipe1_3" : "brewing3"
    }


''' brewing2.lua
PTP(hardcoding13,20,-1,0)
PTP(hardcodingspiralnew1,20,-1,0)
Spiral(hardcodingspiralnew2,hardcodingspiralnew3,hardcodingspiralnew4,5,0,0,0,0,0,0,0,5,0,0,0,28,0)
PTP(hardcoding13,20,-1,0)
sleep_ms(35000)
PTP(hardcodingspiralnew5,20,-1,0)
Spiral(hardcodingspiralnew6,hardcodingspiralnew7,hardcodingspiralnew8,5,0,0,0,0,0,0,0,6,0,0,0,20,0)
PTP(hardcoding13,20,-1,0)
sleep_ms(35000)
PTP(hardcodingspiralnew9,20,-1,0)
Spiral(hardcodingspiralnew10,hardcodingspiralnew11,hardcodingspiralnew12,5,0,0,0,0,0,0,0,5,0,0,0,20,0)
PTP(hardcoding13,20,-1,0)
sleep_ms(35000)
PTP(hardcodingspiralnew13,20,-1,0)
Spiral(hardcodingspiralnew14,hardcodingspiralnew15,hardcodingspiralnew16,5,0,0,0,0,0,0,0,5,0,0,0,20,0)
PTP(hardcoding13,20,-1,0)
'''