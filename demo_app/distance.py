import cv2
import numpy as np

# kích thước len cong 17mm, len thẳng 14mm
# 1 pixel = 0,2646 mm
class SingleCamDistanceMeasure(object):
    # 1 cm = 0.39 inch, original size h x w
    # INCH = 0.39
    h_len_mm = 17
    h_len_pixel = 64
    RefSizeDict = {
        "no traffic both ways": (0.7, 0.7),
        "No parking": (0.7, 0.7),
        "intersection with non-priority road": (0.7, 0.7),
    }

    def __init__(self, object_list=["no traffic both ways", "No parking", "intersection with non-priority road"]):
        self.object_list = object_list
        self.distance_points = []

    def calcDistance(self, x1, y1, x2, y2, f, height_image):
        # f là tiêu cự thấu kính từ 2.8 đến 50 mm
        self.distance_points = []

        if y2 <= 650:
            point_x = (x1 + x2) // 2
            point_y = y2

            try:
                distance = (f * 0.7 * height_image) / ((y2 - y1) * 4.55)
                self.distance_points.append([point_x, point_y, distance])
            except:
                pass

    def DrawDetectedOnFrame(self, frame_show):
        if (len(self.distance_points) != 0):
            for x, y, d in self.distance_points:
                cv2.circle(frame_show, (x, y), 4, (0, 255, 0), thickness=-1)
                unit = 'm'
                if d < 0:
                    text = ' {} {}'.format("unknown", unit)
                else:
                    text = ' {:.2f} {}'.format(d, unit)
                if (d > 3):
                    fontScale = 1
                elif (1.5 < d <= 3):
                    fontScale = 1
                elif (d <= 1.5):
                    fontScale = 1
                else:
                    fontScale = 1

                # get coords based on boundary
                textsize = cv2.getTextSize(text, 0, fontScale=fontScale, thickness=3)[0]
                textX = int((x - textsize[0] / 2))
                textY = int((y + textsize[1]))

                cv2.putText(frame_show, text, (textX + 1, textY + 5), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                            fontScale=fontScale,
                            color=(0, 0, 255), thickness=3)
