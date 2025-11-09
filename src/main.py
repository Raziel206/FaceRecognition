from src import cv
from src.utils import resize, face_detect, hand_detect
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

cv.namedWindow('frame', cv.WINDOW_NORMAL)
cv.resizeWindow('frame', 800, 600)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.flip(frame, 1)
    frame = face_detect(frame)
    frame = hand_detect(frame)
    output = resize(frame)
    if (cv.waitKey(1) & 0xFF) == 27:
        break
    cv.imshow('frame', output)

cap.release()
cv.destroyAllWindows()
