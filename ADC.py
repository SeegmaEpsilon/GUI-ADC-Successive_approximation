# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ADC.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 460)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 460))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 30, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_ref = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ref.setGeometry(QtCore.QRect(730, 70, 51, 21))
        self.line_ref.setObjectName("line_ref")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 70, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bit_depth = QtWidgets.QSpinBox(self.centralwidget)
        self.bit_depth.setGeometry(QtCore.QRect(730, 30, 51, 22))
        self.bit_depth.setReadOnly(False)
        self.bit_depth.setMinimum(1)
        self.bit_depth.setMaximum(24)
        self.bit_depth.setProperty("value", 6)
        self.bit_depth.setObjectName("bit_depth")
        self.line_input = QtWidgets.QLineEdit(self.centralwidget)
        self.line_input.setGeometry(QtCore.QRect(730, 110, 51, 21))
        self.line_input.setObjectName("line_input")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 110, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 350, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 210, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line_code = QtWidgets.QLineEdit(self.centralwidget)
        self.line_code.setGeometry(QtCore.QRect(510, 240, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.line_code.setFont(font)
        self.line_code.setAlignment(QtCore.Qt.AlignCenter)
        self.line_code.setReadOnly(True)
        self.line_code.setObjectName("line_code")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 280, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.line_error = QtWidgets.QLineEdit(self.centralwidget)
        self.line_error.setGeometry(QtCore.QRect(510, 310, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.line_error.setFont(font)
        self.line_error.setAlignment(QtCore.Qt.AlignCenter)
        self.line_error.setReadOnly(True)
        self.line_error.setObjectName("line_error")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 400, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 30, 461, 361))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 350, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 140, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.line_output = QtWidgets.QLineEdit(self.centralwidget)
        self.line_output.setGeometry(QtCore.QRect(510, 170, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.line_output.setFont(font)
        self.line_output.setAutoFillBackground(False)
        self.line_output.setAlignment(QtCore.Qt.AlignCenter)
        self.line_output.setReadOnly(True)
        self.line_output.setObjectName("line_output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Количество разрядов АЦП = "))
        self.line_ref.setText(_translate("MainWindow", "10"))
        self.label_2.setText(_translate("MainWindow", "Опорное напряжение [В]   ="))
        self.line_input.setText(_translate("MainWindow", "9"))
        self.label_3.setText(_translate("MainWindow", "Входное напряжение  [В]   ="))
        self.pushButton.setText(_translate("MainWindow", "ОК"))
        self.label_4.setText(_translate("MainWindow", "Код на выходе АЦП:"))
        self.line_code.setText(_translate("MainWindow", "111 001"))
        self.label_5.setText(_translate("MainWindow", "Относительная погрешность [%]:"))
        self.line_error.setText(_translate("MainWindow", "1.042"))
        self.label_6.setText(_translate("MainWindow", "Диаграмма изменения выходного напряжения АЦП"))
        self.pushButton_2.setText(_translate("MainWindow", "СБРОС"))
        self.label_7.setText(_translate("MainWindow", "Выходное напряжение [В]:"))
        self.line_output.setText(_translate("MainWindow", "8.90625"))