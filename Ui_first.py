# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\code\project\ForFire\first.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1202, 792)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(40, 20, 391, 41))
        font = QtGui.QFont()
        font.setFamily("3D Isometric")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.calculateButton1 = QtWidgets.QPushButton(Form)
        self.calculateButton1.setGeometry(QtCore.QRect(20, 380, 241, 81))
        font = QtGui.QFont()
        font.setFamily("锐字潮牌可变真言2.0简")
        font.setPointSize(16)
        self.calculateButton1.setFont(font)
        self.calculateButton1.setStyleSheet("")
        self.calculateButton1.setObjectName("calculateButton1")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 520, 511, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.interation_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.interation_Label.setFont(font)
        self.interation_Label.setObjectName("interation_Label")
        self.gridLayout_2.addWidget(self.interation_Label, 6, 0, 1, 1)
        self.result_interation = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.result_interation.setMinimumSize(QtCore.QSize(60, 30))
        self.result_interation.setMaximumSize(QtCore.QSize(60, 30))
        self.result_interation.setObjectName("result_interation")
        self.gridLayout_2.addWidget(self.result_interation, 6, 1, 1, 1)
        self.result_x = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.result_x.setFont(font)
        self.result_x.setObjectName("result_x")
        self.gridLayout_2.addWidget(self.result_x, 2, 0, 1, 1)
        self.result_y = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.result_y.setFont(font)
        self.result_y.setObjectName("result_y")
        self.gridLayout_2.addWidget(self.result_y, 4, 0, 1, 1)
        self.result_out_x = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.result_out_x.setMinimumSize(QtCore.QSize(400, 30))
        self.result_out_x.setMaximumSize(QtCore.QSize(400, 30))
        self.result_out_x.setObjectName("result_out_x")
        self.gridLayout_2.addWidget(self.result_out_x, 2, 1, 1, 1)
        self.result_out_y = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.result_out_y.setMinimumSize(QtCore.QSize(400, 30))
        self.result_out_y.setMaximumSize(QtCore.QSize(400, 30))
        self.result_out_y.setObjectName("result_out_y")
        self.gridLayout_2.addWidget(self.result_out_y, 4, 1, 1, 1)
        self.result_out_q = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.result_out_q.setMinimumSize(QtCore.QSize(400, 30))
        self.result_out_q.setMaximumSize(QtCore.QSize(400, 30))
        self.result_out_q.setObjectName("result_out_q")
        self.gridLayout_2.addWidget(self.result_out_q, 5, 1, 1, 1)
        self.result_q = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.result_q.setFont(font)
        self.result_q.setObjectName("result_q")
        self.gridLayout_2.addWidget(self.result_q, 5, 0, 1, 1)
        self.result_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.result_Label.setFont(font)
        self.result_Label.setObjectName("result_Label")
        self.gridLayout_2.addWidget(self.result_Label, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(20, 110, 721, 231))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 700, 420))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(700, 420))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(700, 420))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 693, 412))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.con2_q = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con2_q.setMinimumSize(QtCore.QSize(200, 30))
        self.con2_q.setMaximumSize(QtCore.QSize(200, 30))
        self.con2_q.setObjectName("con2_q")
        self.gridLayout_4.addWidget(self.con2_q, 4, 3, 1, 1)
        self.con1_x_9 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_9.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_9.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_9.setObjectName("con1_x_9")
        self.gridLayout_4.addWidget(self.con1_x_9, 7, 2, 1, 1)
        self.con2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con2.setMinimumSize(QtCore.QSize(70, 30))
        self.con2.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con2.setFont(font)
        self.con2.setObjectName("con2")
        self.gridLayout_4.addWidget(self.con2, 4, 0, 1, 1)
        self.con2_x = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con2_x.setMinimumSize(QtCore.QSize(200, 30))
        self.con2_x.setMaximumSize(QtCore.QSize(200, 30))
        self.con2_x.setObjectName("con2_x")
        self.gridLayout_4.addWidget(self.con2_x, 4, 1, 1, 1)
        self.con1_x_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_2.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_2.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_2.setObjectName("con1_x_2")
        self.gridLayout_4.addWidget(self.con1_x_2, 6, 1, 1, 1)
        self.con1_x_10 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_10.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_10.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_10.setObjectName("con1_x_10")
        self.gridLayout_4.addWidget(self.con1_x_10, 7, 3, 1, 1)
        self.con3_q = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con3_q.setMinimumSize(QtCore.QSize(200, 30))
        self.con3_q.setMaximumSize(QtCore.QSize(200, 30))
        self.con3_q.setObjectName("con3_q")
        self.gridLayout_4.addWidget(self.con3_q, 2, 3, 1, 1)
        self.q_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.q_Label.setMinimumSize(QtCore.QSize(200, 40))
        self.q_Label.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.q_Label.setFont(font)
        self.q_Label.setObjectName("q_Label")
        self.gridLayout_4.addWidget(self.q_Label, 0, 3, 1, 1)
        self.con1_x_11 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_11.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_11.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_11.setObjectName("con1_x_11")
        self.gridLayout_4.addWidget(self.con1_x_11, 9, 1, 1, 1)
        self.con1_y = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_y.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_y.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_y.setObjectName("con1_y")
        self.gridLayout_4.addWidget(self.con1_y, 5, 2, 1, 1)
        self.con1_x = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x.setObjectName("con1_x")
        self.gridLayout_4.addWidget(self.con1_x, 5, 1, 1, 1)
        self.con1_x_7 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_7.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_7.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_7.setObjectName("con1_x_7")
        self.gridLayout_4.addWidget(self.con1_x_7, 8, 3, 1, 1)
        self.con1_x_13 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_13.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_13.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_13.setObjectName("con1_x_13")
        self.gridLayout_4.addWidget(self.con1_x_13, 10, 1, 1, 1)
        self.con1_q = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_q.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_q.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_q.setObjectName("con1_q")
        self.gridLayout_4.addWidget(self.con1_q, 5, 3, 1, 1)
        self.con1_x_14 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_14.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_14.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_14.setObjectName("con1_x_14")
        self.gridLayout_4.addWidget(self.con1_x_14, 11, 1, 1, 1)
        self.con3_y = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con3_y.setMinimumSize(QtCore.QSize(200, 30))
        self.con3_y.setMaximumSize(QtCore.QSize(200, 30))
        self.con3_y.setObjectName("con3_y")
        self.gridLayout_4.addWidget(self.con3_y, 2, 2, 1, 1)
        self.x_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.x_Label.setMinimumSize(QtCore.QSize(200, 40))
        self.x_Label.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.x_Label.setFont(font)
        self.x_Label.setObjectName("x_Label")
        self.gridLayout_4.addWidget(self.x_Label, 0, 1, 1, 1)
        self.con2_y = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con2_y.setMinimumSize(QtCore.QSize(200, 30))
        self.con2_y.setMaximumSize(QtCore.QSize(200, 30))
        self.con2_y.setObjectName("con2_y")
        self.gridLayout_4.addWidget(self.con2_y, 4, 2, 1, 1)
        self.con1_x_6 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_6.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_6.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_6.setObjectName("con1_x_6")
        self.gridLayout_4.addWidget(self.con1_x_6, 8, 2, 1, 1)
        self.con1_x_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_4.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_4.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_4.setObjectName("con1_x_4")
        self.gridLayout_4.addWidget(self.con1_x_4, 6, 3, 1, 1)
        self.con3_x = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con3_x.setMinimumSize(QtCore.QSize(200, 30))
        self.con3_x.setMaximumSize(QtCore.QSize(200, 30))
        self.con3_x.setObjectName("con3_x")
        self.gridLayout_4.addWidget(self.con3_x, 2, 1, 1, 1)
        self.con3_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con3_4.setMinimumSize(QtCore.QSize(70, 30))
        self.con3_4.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con3_4.setFont(font)
        self.con3_4.setObjectName("con3_4")
        self.gridLayout_4.addWidget(self.con3_4, 7, 0, 1, 1)
        self.con1_x_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_5.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_5.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_5.setObjectName("con1_x_5")
        self.gridLayout_4.addWidget(self.con1_x_5, 8, 1, 1, 1)
        self.con3_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con3_2.setMinimumSize(QtCore.QSize(70, 30))
        self.con3_2.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con3_2.setFont(font)
        self.con3_2.setObjectName("con3_2")
        self.gridLayout_4.addWidget(self.con3_2, 6, 0, 1, 1)
        self.y_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.y_Label.setMinimumSize(QtCore.QSize(200, 40))
        self.y_Label.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.y_Label.setFont(font)
        self.y_Label.setObjectName("y_Label")
        self.gridLayout_4.addWidget(self.y_Label, 0, 2, 1, 1)
        self.con3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con3.setMinimumSize(QtCore.QSize(70, 30))
        self.con3.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con3.setFont(font)
        self.con3.setObjectName("con3")
        self.gridLayout_4.addWidget(self.con3, 5, 0, 1, 1)
        self.con3_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con3_3.setMinimumSize(QtCore.QSize(70, 30))
        self.con3_3.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con3_3.setFont(font)
        self.con3_3.setObjectName("con3_3")
        self.gridLayout_4.addWidget(self.con3_3, 8, 0, 1, 1)
        self.con1_x_8 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_8.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_8.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_8.setObjectName("con1_x_8")
        self.gridLayout_4.addWidget(self.con1_x_8, 7, 1, 1, 1)
        self.con1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con1.setMinimumSize(QtCore.QSize(70, 30))
        self.con1.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con1.setFont(font)
        self.con1.setObjectName("con1")
        self.gridLayout_4.addWidget(self.con1, 2, 0, 1, 1)
        self.con1_x_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_3.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_3.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_3.setObjectName("con1_x_3")
        self.gridLayout_4.addWidget(self.con1_x_3, 6, 2, 1, 1)
        self.con1_x_12 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_12.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_12.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_12.setObjectName("con1_x_12")
        self.gridLayout_4.addWidget(self.con1_x_12, 9, 2, 1, 1)
        self.con1_x_15 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_15.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_15.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_15.setObjectName("con1_x_15")
        self.gridLayout_4.addWidget(self.con1_x_15, 12, 1, 1, 1)
        self.con1_x_16 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_16.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_16.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_16.setObjectName("con1_x_16")
        self.gridLayout_4.addWidget(self.con1_x_16, 9, 3, 1, 1)
        self.con1_x_17 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_17.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_17.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_17.setObjectName("con1_x_17")
        self.gridLayout_4.addWidget(self.con1_x_17, 10, 2, 1, 1)
        self.con1_x_18 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_18.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_18.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_18.setObjectName("con1_x_18")
        self.gridLayout_4.addWidget(self.con1_x_18, 10, 3, 1, 1)
        self.con1_x_19 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_19.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_19.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_19.setObjectName("con1_x_19")
        self.gridLayout_4.addWidget(self.con1_x_19, 11, 2, 1, 1)
        self.con1_x_20 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_20.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_20.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_20.setObjectName("con1_x_20")
        self.gridLayout_4.addWidget(self.con1_x_20, 11, 3, 1, 1)
        self.con1_x_21 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_21.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_21.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_21.setObjectName("con1_x_21")
        self.gridLayout_4.addWidget(self.con1_x_21, 12, 2, 1, 1)
        self.con1_x_22 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_22.setMinimumSize(QtCore.QSize(200, 30))
        self.con1_x_22.setMaximumSize(QtCore.QSize(200, 30))
        self.con1_x_22.setObjectName("con1_x_22")
        self.gridLayout_4.addWidget(self.con1_x_22, 12, 3, 1, 1)
        self.con3_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con3_5.setMinimumSize(QtCore.QSize(70, 30))
        self.con3_5.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con3_5.setFont(font)
        self.con3_5.setObjectName("con3_5")
        self.gridLayout_4.addWidget(self.con3_5, 9, 0, 1, 1)
        self.con3_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con3_6.setMinimumSize(QtCore.QSize(70, 30))
        self.con3_6.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con3_6.setFont(font)
        self.con3_6.setObjectName("con3_6")
        self.gridLayout_4.addWidget(self.con3_6, 10, 0, 1, 1)
        self.con3_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con3_7.setMinimumSize(QtCore.QSize(70, 30))
        self.con3_7.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con3_7.setFont(font)
        self.con3_7.setObjectName("con3_7")
        self.gridLayout_4.addWidget(self.con3_7, 11, 0, 1, 1)
        self.con3_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.con3_8.setMinimumSize(QtCore.QSize(70, 30))
        self.con3_8.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(11)
        font.setItalic(True)
        self.con3_8.setFont(font)
        self.con3_8.setObjectName("con3_8")
        self.gridLayout_4.addWidget(self.con3_8, 12, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.progress_bar = QtWidgets.QProgressBar(Form)
        self.progress_bar.setGeometry(QtCore.QRect(20, 480, 511, 23))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.calculateButton2 = QtWidgets.QPushButton(Form)
        self.calculateButton2.setGeometry(QtCore.QRect(300, 380, 241, 81))
        font = QtGui.QFont()
        font.setFamily("锐字潮牌可变真言2.0简")
        font.setPointSize(16)
        self.calculateButton2.setFont(font)
        self.calculateButton2.setObjectName("calculateButton2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(660, 390, 391, 341))
        self.widget.setObjectName("widget")
        self.plotButton = QtWidgets.QPushButton(Form)
        self.plotButton.setGeometry(QtCore.QRect(830, 200, 121, 51))
        font = QtGui.QFont()
        font.setFamily("霞鹜臻楷")
        font.setPointSize(16)
        self.plotButton.setFont(font)
        self.plotButton.setObjectName("plotButton")
        self.scrollArea.raise_()
        self.title.raise_()
        self.calculateButton1.raise_()
        self.gridLayoutWidget.raise_()
        self.progress_bar.raise_()
        self.calculateButton2.raise_()
        self.widget.raise_()
        self.plotButton.raise_()

        self.retranslateUi(Form)
        self.calculateButton1.clicked.connect(Form.calculate) # type: ignore
        self.calculateButton2.clicked.connect(Form.calculate) # type: ignore
        self.progress_bar.valueChanged['int'].connect(self.calculateButton2.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "毒气泄漏反演图像"))
        self.title.setText(_translate("Form", "请输入三个坐标位置以及对应的毒气浓度"))
        self.calculateButton1.setText(_translate("Form", "开始计算（优化）"))
        self.interation_Label.setText(_translate("Form", "迭代次数"))
        self.result_x.setText(_translate("Form", "x坐标"))
        self.result_y.setText(_translate("Form", "y坐标"))
        self.result_q.setText(_translate("Form", "毒气浓度"))
        self.result_Label.setText(_translate("Form", "计算结果"))
        self.con2.setText(_translate("Form", "坐标2："))
        self.q_Label.setText(_translate("Form", "毒气浓度"))
        self.x_Label.setText(_translate("Form", "x坐标"))
        self.con3_4.setText(_translate("Form", "坐标5："))
        self.con3_2.setText(_translate("Form", "坐标4："))
        self.y_Label.setText(_translate("Form", "y坐标"))
        self.con3.setText(_translate("Form", "坐标3："))
        self.con3_3.setText(_translate("Form", "坐标6："))
        self.con1.setText(_translate("Form", "坐标1："))
        self.con3_5.setText(_translate("Form", "坐标7："))
        self.con3_6.setText(_translate("Form", "坐标8："))
        self.con3_7.setText(_translate("Form", "坐标9："))
        self.con3_8.setText(_translate("Form", "坐标10："))
        self.calculateButton2.setText(_translate("Form", "开始计算（蒙卡）"))
        self.plotButton.setText(_translate("Form", "作图"))
