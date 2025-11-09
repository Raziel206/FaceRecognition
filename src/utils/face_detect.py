from src import cv,face_detection
def face_detect(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = face_detection.process(rgb)
    if results.detections:
        h, w, _ = img.shape
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            x, y, bw, bh = int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)
            cv.rectangle(img, (x, y), (x + bw, y + bh), (255, 255, 255), 1)
    return img
