place_coffee_grounds_point = \
    {
        # 1.PTP - 원두 컵 앞에 위치 (Locate in front of the cup of coffee beans)
        "J1": [-7.371, -112.275, -123.395, -125.77, -20.603, 0.979],
        "P1": [246.739, -229.154, -98.059, 90.507, 0.369, 0.979], #X,Y,Z,RX,RY,RZ
        # 2.Linear - 원두 컵쪽으로 들어가기 (Move forward to the cup)
        "J2": [-25.943, -124.425, -100.999, -135.379, -39.168, -.259],
        "P2": [270.765, -331.366, 97.109, 90.514, 0.368, 13.229],
        # 3.Linear - 원두 컵 잡기 위해 올림 (Move up to grab the cup)
        "J3": [-25.959, -119.019, -98.106, -143.677, -39.189, 0.259],
        "P3": [271.094, -331.659, 137.108, 90.509, 0.368, 13.229],
        # 4.Linear - 잡은 뒤 컵 올리기 (Pick up the cup)
        "J4": [-26.107, -120.769, -20.516, -219.518, -39.336, 0.255],
        "P4": [273.501, -333.753, 427.799, 90.507, 0.368, 13.229],
        # 5.Linear - 붓기 전, 드리퍼 위에 위치시키기 (Locate the cup over the dripper)
        "J5": [52.364, -89.459, -62.827, -214.022, -4.584, 5.918],
        "P5": [285.859, 40.423, 429.329, 90.505, 0.374, 56.919],
        # 6.PTP - 붓기 위해 위치 조정 (Adjust the coordinates to pour it)
        "J6": [47.769, -103.107, -55.039, -214.654, -11.889, -11.826],
        "P6": [338.687, 75.774, 398.006, 92.871, 24.334, 60.556],
        # 7.PTP - 원두 붓기 (Pour it)
        "J7": [47.769, -103.107, -55.039, -214.654, -11.889, -131.826],
        "P7": [338.687, 75.774, 398.006, 92.871, 24.334, 60.556],
        # 8.PTP - 컵 되돌려놓기 위한 
    }

bloom_point = \
    {
        # 1.Linear - 컵 놓고 주전자 가지러 가기위한 1단계
        "J1": [-26.107, -120.769, -20.516, -219.518, -39.336, 0.255],
        "P1": [273.501, -333.753, 427.799, 90.507, 0.368, 13.229],
        # 2. PTP - 주전자 가지러 가기위한 2단계
        "J2": [62.268, -105.645, -33.004, -225.428, -39.357, 0.282],
        "P2": [303.755, 192.429, 461.936, 92.588, 2.871, 101.684],
        # 3. PTP - 주전자 가지러 가기위한 3단계. 주전자에 ARM 넣기 직전.
        "J3": [84.369, -92.461, -129.327, -140.076, -47.399, -89.320],
        "P3": [194.500, 243.314, 155.473, -157.019, 88.510, -115.259],
        # 4. LIN - 주전자에 ARM 집어 넣기
        "J4": [63.969, -128.358	, -77.396, -155.729, -67.791, -90.019],
        "P4": [336.195, 369.801, 150.916, -157.102, 88.509, -115.342],
        # 5. LIN - 턱에 걸리는 것을 방지하기 위해 주전자 집은 상태에서 살짝 들어올리기.
        "J5": [63.969, -126.066, -73.691, -161.735, -67.790, -90.019],
        "P5": [336.538, 370.498, 180.833, -157.105, 88.501, -115.346],
        # 6. PTP - 주전자 들고 뜸 들이러 가기 1단계
        "J6": [110.154, -111.783, -87.155, -161.702, 52.917, -85.381],
        "P6": [66.221, 290.616, 221.013, 83.118, 85.736, 50.376],
        # 7. PTP - 주전자 들고 뜸 들이러 가기 2단계
        "J7": [92.364, -97.039, -50.972, -211.319, 31.601, -85.393],
        "P7": [179.311, 194.227, 442.426, 93.888, 84.810, 64.637],
        # 8. PTP - 주전자 들고 뜸 들이러 가기 3단계
        "J8": [44.485, -93.276, -44.024, -217.290, 8.706, -97.815],
        "P8": [274.099, -12.309, 479.328, -108.342, 87.401, -162.508],
    }

pour_point = \
    {
        # 1. PTP - 1st Pour를 위한 이동
        "J1": [44.475, -92.518, -44.844, -217.223, 8.697, -121.819],
        "P1": [271.602, -14.806, 479.327, -91.834, 63.523, -145.825],
        # 2. Spiral - 1st Pour Point1
        "J2": [45.492, -93.119, -44.167, -217.860, 9.708, -121.251],
        "P2": [271.602, -9.808, 479.327, -91.834, 63.523, -145.825],
        # 3. Spiral - 1st Pour Point2
        "J3": [44.494, -94.045, -43.177, -217.374, 8.715, -121.808],
        "P3": [276.602, -9.808, 479.327, -91.834, 63.523, -145.825],
        # 4. Spiral - 1st Pour Point3
        "J4": [43.487, -93.384, -43.947, -216.566, 7.713, -122.515],
        "P4": [276.602, -14.806, 479.327, -91.834, 63.523, -145.825],
        # 5. PTP - 2nd Pour를 위한 이동
        "J5": [44.476, -92.518, -44.844, -217.224, 8.697, -129.819],
        "P5": [271.600, -14.804, 479.327, -91.445, 55.526, -145.374],
        # 6. Spiral - 2nd Pour Point1
        "J6": [45.492, -93.119, -44.167, -217.861, 9.709, -129.251],
        "P6": [271.600, -9.804, 479.327, -91.445, 55.526, -145.374],
        # 7. Spiral - 2nd Pour Point2
        "J7": [44.495, -94.045, -43.177, -217.374, 8.715, -129.808],
        "P7": [276.600, -9.804, 479.327, -91.445, 55.526, -145.374],
        # 8. Spiral - 2nd Pour Point3
        "J8": [43.485, -93.384, -43.946, -216.565, 7.713, -130.515],
        "P8": [276.600, -14.804, 479.327, -91.445, 55.526, -145.374],
        # 9. PTP - 3rd, 4th Pour를 위한 이동
        "J9": [44.485, -93.276, -44.024, -217.290, 8.706, -134.815],
        "P9": [274.098, -12.309, 479.329, -91.286, 50.527, -145.176],
        # 10. Spiral - 3rd, 4th Pour Point1
        "J10": [45.483, -93.888, -43.322, -217.931, 9.701, -134.256],
        "P10": [274.098, -7.309, 479.329, -91.286, 50.527, -145.176],
        # 11. Spiral - 3rd, 4th Pour Point2
        "J11": [44.503, -94.825, -42.300, -217.476, 8.724, -134.803],
        "P11": [279.098, -7.309, 479.329, -91.286, 50.527, -145.176],
        # 12. Spiral - 3rd, 4th Pour Point3
        "J12": [43.513, -94.154, -43.094, -216.668, 7.739, -135.495],
        "P12": [279.098, -12.309, 479.329, -91.286, 50.527, -145.176],
        # 13. PTP - 5th Pour를 위한 이동
        "J13": [44.502, -94.826, -42.299, -217.475, 8.722, -139.804],
        "P13": [279.101, -7.308, 479.329, -91.167, 45.528, -145.014],
        # 14. Spiral - 5th Pour Point1
        "J14": [45.467, -95.463, -41.543, -218.127, 9.684, -139.264],
        "P14": [279.101, -2.308, 479.329, -91.167, 45.528, -145.014],
        # 15. Spiral - 5th Pour Point2
        "J15": [44.520, -96.425, -40.449, -217.737, 8.740, -139.792],
        "P15": [284.101, -2.308, 479.329, -91.167, 45.528, -145.014],
        # 16. Spiral - 5th Pour Point3
        "J16": [43.563, -95.732, -41.299, -216.925, 7.787, -140.456],
        "P16": [284.101, -7.308, 479.329, -91.167, 45.528, -145.014],
        # 17. PTP - 붓기 사이에 정위치
        "J17": [44.485, -93.276, -44.024, -217.290, 8.706, -97.815],
        "P17": [274.099, -12.309, 479.328, -108.342, 87.401, -162.508]
    }