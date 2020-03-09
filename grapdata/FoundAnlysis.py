# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FoundAnlysis.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 864)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        Form.setFont(font)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(510, 10, 541, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 10, 451, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_UpdateData = QtWidgets.QPushButton(Form)
        self.btn_UpdateData.setGeometry(QtCore.QRect(1080, 10, 93, 28))
        self.btn_UpdateData.setObjectName("btn_UpdateData")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 129, 1061, 731))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_displayImage = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_displayImage.setFont(font)
        self.lbl_displayImage.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_displayImage.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_displayImage.setObjectName("lbl_displayImage")
        self.horizontalLayout.addWidget(self.lbl_displayImage)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 80, 951, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmb_Dir = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_Dir.setObjectName("cmb_Dir")
        self.horizontalLayout_3.addWidget(self.cmb_Dir)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_LoadImage = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_LoadImage.setObjectName("btn_LoadImage")
        self.horizontalLayout_2.addWidget(self.btn_LoadImage)
        self.btn_UpImage = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_UpImage.setObjectName("btn_UpImage")
        self.horizontalLayout_2.addWidget(self.btn_UpImage)
        self.btn_DownImage = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_DownImage.setObjectName("btn_DownImage")
        self.horizontalLayout_2.addWidget(self.btn_DownImage)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.btn_PlayVedio = QtWidgets.QPushButton(Form)
        self.btn_PlayVedio.setGeometry(QtCore.QRect(1120, 220, 93, 28))
        self.btn_PlayVedio.setObjectName("btn_PlayVedio")
        self.btn_initCam = QtWidgets.QPushButton(Form)
        self.btn_initCam.setGeometry(QtCore.QRect(1120, 150, 93, 28))
        self.btn_initCam.setObjectName("btn_initCam")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Notice: 为提高速度，需要提前下载最新数据至本地数据库："))
        self.btn_UpdateData.setText(_translate("Form", "更新数据"))
        self.lbl_displayImage.setText(_translate("Form", "test"))
        self.label_2.setText(_translate("Form", "Directory："))
        self.btn_LoadImage.setText(_translate("Form", "LoadImage"))
        self.btn_UpImage.setText(_translate("Form", "Up"))
        self.btn_DownImage.setText(_translate("Form", "Down"))
        self.btn_PlayVedio.setText(_translate("Form", "PlayVedio"))
        self.btn_initCam.setText(_translate("Form", "Initial Cam"))