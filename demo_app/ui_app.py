# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: red;\n"
"border-radius: 5px;\n"
"padding: 5px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.focal = QtWidgets.QLineEdit(self.page)
        self.focal.setObjectName("focal")
        self.gridLayout.addWidget(self.focal, 2, 1, 1, 1)
        self.model_name = QtWidgets.QComboBox(self.page)
        self.model_name.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.model_name.setObjectName("model_name")
        self.model_name.addItem("")
        self.gridLayout.addWidget(self.model_name, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.resolution = QtWidgets.QComboBox(self.page)
        self.resolution.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.resolution.setObjectName("resolution")
        self.resolution.addItem("")
        self.gridLayout.addWidget(self.resolution, 3, 1, 1, 1)
        self.source = QtWidgets.QComboBox(self.page)
        self.source.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.source.setObjectName("source")
        self.source.addItem("")
        self.gridLayout.addWidget(self.source, 0, 1, 1, 1)
        self.btn_choose_video = QtWidgets.QPushButton(self.page)
        self.btn_choose_video.setObjectName("btn_choose_video")
        self.gridLayout.addWidget(self.btn_choose_video, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.btn_detect = QtWidgets.QPushButton(self.page)
        self.btn_detect.setObjectName("btn_detect")
        self.verticalLayout_2.addWidget(self.btn_detect)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("")
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: red;\n"
"border-radius: 5px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_video = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_video.sizePolicy().hasHeightForWidth())
        self.input_video.setSizePolicy(sizePolicy)
        self.input_video.setObjectName("input_video")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.input_video)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout.addWidget(self.input_video)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_compare = QtWidgets.QPushButton(self.widget_4)
        self.btn_compare.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_compare.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_compare.setObjectName("btn_compare")
        self.verticalLayout_3.addWidget(self.btn_compare)
        self.btn_home = QtWidgets.QPushButton(self.widget_4)
        self.btn_home.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_home.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_3.addWidget(self.btn_home)
        self.horizontalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter)
        self.output_video = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_video.sizePolicy().hasHeightForWidth())
        self.output_video.setSizePolicy(sizePolicy)
        self.output_video.setObjectName("output_video")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.output_video)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout.addWidget(self.output_video)
        self.verticalLayout_4.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DEMO NHẬN DIỆN BIỂN BÁO GIAO THÔNG"))
        self.label_2.setText(_translate("MainWindow", "Phan Anh Dũng - 20182445"))
        self.label_3.setText(_translate("MainWindow", "Đồ án tốt nghiệp"))
        self.label_4.setText(_translate("MainWindow", "Chọn mô hình"))
        self.label_7.setText(_translate("MainWindow", "Độ phân giải"))
        self.model_name.setItemText(0, _translate("MainWindow", "YOLOv8"))
        self.label_6.setText(_translate("MainWindow", "Tiêu cự"))
        self.label_5.setText(_translate("MainWindow", "Kiểu dữ liệu"))
        self.resolution.setItemText(0, _translate("MainWindow", "1920x1080"))
        self.source.setItemText(0, _translate("MainWindow", "Video"))
        self.btn_choose_video.setText(_translate("MainWindow", "Choose File"))
        self.btn_detect.setText(_translate("MainWindow", "Detect"))
        self.label_8.setText(_translate("MainWindow", "DEMO NHẬN DIỆN BIỂN BÁO GIAO THÔNG"))
        self.label_9.setText(_translate("MainWindow", "Phan Anh Dũng - 20182445"))
        self.label_10.setText(_translate("MainWindow", "Đồ án tốt nghiệp"))
        self.btn_compare.setText(_translate("MainWindow", "COMPARE"))
        self.btn_home.setText(_translate("MainWindow", "HOME"))
