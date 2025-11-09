from src import cv, mp_draw, hands, mp_hands

def hand_detect(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
    return img
