from PyQt5 import QtWidgets, QtCore
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget 
import sys, os
from threading import Thread
from ui_app import Ui_MainWindow
import utils
from detect import detect

# os.environ.update({"QT_QPA_PLATFORM_PLUGIN_PATH": "/home/anh/.local/lib/python3.8/site-packages/PySide2/Qt/plugins"})

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.videoPath = None
        self.addVideoWidget()
        self.setup_ui()
        self.button_onclicked()

    def addVideoWidget(self):
        self.inPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        inVideoWidget = QVideoWidget()
        self.ui.verticalLayout_5.addWidget(inVideoWidget)
        self.inPlayer.setVideoOutput(inVideoWidget)
        self.outPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        outVideoWidget = QVideoWidget()
        self.ui.verticalLayout_6.addWidget(outVideoWidget)
        self.outPlayer.setVideoOutput(outVideoWidget)

    def setup_ui(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.btn_compare.setCheckable(True)

    def button_onclicked(self):
        self.ui.btn_choose_video.clicked.connect(self.chooseVideo)
        self.ui.btn_detect.clicked.connect(self.moveToPage2)
        self.ui.btn_home.clicked.connect(self.moveToPage1)
        self.ui.btn_compare.clicked.connect(self.compare)

    def chooseVideo(self):
        inVideoPath, _ = utils.openFile()
        inVideoName = os.path.basename(inVideoPath)
        parent_path = os.path.dirname(inVideoPath)
        outVideoPath = os.path.join(parent_path, "result", inVideoName)
        self.videoPath = [inVideoPath, outVideoPath]
        
    def moveToPage1(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.inPlayer.pause()
        self.outPlayer.pause()
        
    def moveToPage2(self):
        if self.videoPath[1] == None:
            self.videoPath[1] = detect.run(self.videoPath[0])
        else:
            if self.videoPath[0] != None:
                self.ui.stackedWidget.setCurrentIndex(1)
                self.inPlayer.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(self.videoPath[0])))
                self.outPlayer.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(self.videoPath[1])))
                self.inPlayer.play()
                self.outPlayer.play()

    def compare(self):
        if self.ui.btn_compare.isChecked():
            self.inPlayer.stop()
            self.outPlayer.stop()
        else:
            self.inPlayer.play()
            self.outPlayer.play()

    def updateInputScreen(self, frame):
        # print('1')
        pixmap = utils.cv2qpixmap(frame)
        bgsize = self.ui.input_video.size()
        image = pixmap.scaled(bgsize, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.input_display.setPixmap(image)

    def updateOutputScreen(self, frame):
        # print('2')
        pixmap = utils.cv2qpixmap(frame)
        bgsize = self.ui.output_video.size()
        image = pixmap.scaled(bgsize, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.output_display.setPixmap(image)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

