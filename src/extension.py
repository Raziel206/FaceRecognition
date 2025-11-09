import cv2 as cv
import mediapipe as mp

# Mediapipe setup
mp_faces = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

face_detection = mp_faces.FaceDetection(model_selection=1, min_detection_confidence=0.5)
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=6,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)