from src import cv,hands

FINGER_TIPS = [4, 8, 12, 16, 20]

def hand_mapping(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(rgb);
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            h, w, _ = img.shape
            for id, lm in enumerate(handLms.landmark):
                lmList.append((int(lm.x * w), int(lm.y * h)))

            fingers = []
            # Thumb
            if lmList[FINGER_TIPS[0]][0] > lmList[FINGER_TIPS[0] - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other 4 fingers
            for id in range(1, 5):
                if lmList[FINGER_TIPS[id]][1] < lmList[FINGER_TIPS[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)

            gesture = "Unknown"
            if totalFingers == 0:
                gesture = "Fist"
            elif totalFingers == 5:
                gesture = "Open Hand"
            elif totalFingers == 2 and fingers[1] and fingers[2]:
                gesture = "Peace"
            elif totalFingers == 1 and fingers[0]:
                gesture = "Thumbs Up "
            cv.putText(img, gesture, (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return img
