import cv2, os
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog

def cv2qpixmap(cv_img):
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
    return QPixmap.fromImage(convert_to_Qt_format) 

def openFile():
    dir_ = os.getcwd()
    dir_ = QFileDialog.getOpenFileName(None, 'Select a folder:', dir_, str("Video (*.avi *.mp4)"))
    return dir_