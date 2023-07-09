import os
from ultralytics import YOLO
import cv2
#from distance import SingleCamDistanceMeasure
import cvzone
import math
import time

path = '../static/a.mp4'
basename = os.path.basename(path)
file_output_path = os.path.join('.', 'static', 'result', basename)

cap = cv2.VideoCapture(path)
ret, img = cap.read()

cap_out = cv2.VideoWriter(file_output_path, cv2.VideoWriter_fourcc(*'mp4v'), cap.get(cv2.CAP_PROP_FPS),
                          (img.shape[1], img.shape[0]))

model = YOLO("../weights/best.pt")

classNames = ["no traffic both ways", "No parking", "intersection with non-priority road"]

prev_frame_time = 0
new_frame_time = 0

#distance = SingleCamDistanceMeasure()
while ret:
    new_frame_time = time.time()
    # success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            height, weight, depth = img.shape
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Distance
            # distance.calcDistance(x1, y1, x2, y2, 2.8, height)
            # distance.DrawDetectedOnFrame(img)
            cls = int(box.cls[0])
            img_result = cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1,
                                thickness=1)

    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)

    cap_out.write(img)
    ret, img = cap.read()
cap.release()
cap_out.release()
cv2.destroyAllWindows()

