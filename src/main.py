from src import cv
import threading
from src.utils import resize, face_detect, hand_detect, hand_mapping
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

    frame_results = {}


    def process_face(frame):
        frame_results['face'] = face_detect(frame)


    def process_hand(frame):
        frame_results['hand'] = hand_detect(frame)


    def process_mapping(frame):
        frame_results['map'] = hand_mapping(frame)


    threads = [
        threading.Thread(target=process_face, args=(frame,)),
        threading.Thread(target=process_hand, args=(frame,)),
        threading.Thread(target=process_mapping, args=(frame,))
    ]

    for t in threads: t.start()
    for t in threads: t.join()

    frame = resize(frame_results.get('map', frame))
    if (cv.waitKey(1) & 0xFF) == 27:
        break
    cv.imshow('frame', frame)

cap.release()
cv.destroyAllWindows()
