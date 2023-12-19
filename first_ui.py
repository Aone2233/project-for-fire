# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1202, 792)
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(40, 20, 391, 41))
        font = QFont()
        font.setFamilies([u"3D Isometric"])
        font.setPointSize(12)
        font.setBold(True)
        self.title.setFont(font)
        self.calculateButton1 = QPushButton(Form)
        self.calculateButton1.setObjectName(u"calculateButton1")
        self.calculateButton1.setGeometry(QRect(20, 380, 241, 81))
        font1 = QFont()
        font1.setFamilies([u"\u9510\u5b57\u6f6e\u724c\u53ef\u53d8\u771f\u8a002.0\u7b80"])
        font1.setPointSize(16)
        self.calculateButton1.setFont(font1)
        self.calculateButton1.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 520, 511, 181))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.interation_Label = QLabel(self.gridLayoutWidget)
        self.interation_Label.setObjectName(u"interation_Label")
        font2 = QFont()
        font2.setFamilies([u"\u5f97\u610f\u9ed1"])
        font2.setPointSize(11)
        font2.setItalic(True)
        self.interation_Label.setFont(font2)

        self.gridLayout_2.addWidget(self.interation_Label, 6, 0, 1, 1)

        self.result_interation = QLineEdit(self.gridLayoutWidget)
        self.result_interation.setObjectName(u"result_interation")
        self.result_interation.setMinimumSize(QSize(60, 30))
        self.result_interation.setMaximumSize(QSize(60, 30))

        self.gridLayout_2.addWidget(self.result_interation, 6, 1, 1, 1)

        self.result_x = QLabel(self.gridLayoutWidget)
        self.result_x.setObjectName(u"result_x")
        self.result_x.setFont(font2)

        self.gridLayout_2.addWidget(self.result_x, 2, 0, 1, 1)

        self.result_y = QLabel(self.gridLayoutWidget)
        self.result_y.setObjectName(u"result_y")
        self.result_y.setFont(font2)

        self.gridLayout_2.addWidget(self.result_y, 4, 0, 1, 1)

        self.result_out_x = QLineEdit(self.gridLayoutWidget)
        self.result_out_x.setObjectName(u"result_out_x")
        self.result_out_x.setMinimumSize(QSize(400, 30))
        self.result_out_x.setMaximumSize(QSize(400, 30))

        self.gridLayout_2.addWidget(self.result_out_x, 2, 1, 1, 1)

        self.result_out_y = QLineEdit(self.gridLayoutWidget)
        self.result_out_y.setObjectName(u"result_out_y")
        self.result_out_y.setMinimumSize(QSize(400, 30))
        self.result_out_y.setMaximumSize(QSize(400, 30))

        self.gridLayout_2.addWidget(self.result_out_y, 4, 1, 1, 1)

        self.result_out_q = QLineEdit(self.gridLayoutWidget)
        self.result_out_q.setObjectName(u"result_out_q")
        self.result_out_q.setMinimumSize(QSize(400, 30))
        self.result_out_q.setMaximumSize(QSize(400, 30))

        self.gridLayout_2.addWidget(self.result_out_q, 5, 1, 1, 1)

        self.result_q = QLabel(self.gridLayoutWidget)
        self.result_q.setObjectName(u"result_q")
        self.result_q.setFont(font2)

        self.gridLayout_2.addWidget(self.result_q, 5, 0, 1, 1)

        self.result_Label = QLabel(self.gridLayoutWidget)
        self.result_Label.setObjectName(u"result_Label")
        self.result_Label.setFont(font2)

        self.gridLayout_2.addWidget(self.result_Label, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 110, 721, 231))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 700, 420))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(700, 420))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(700, 420))
        self.gridLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 693, 412))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.con2_q = QLineEdit(self.gridLayoutWidget_2)
        self.con2_q.setObjectName(u"con2_q")
        self.con2_q.setMinimumSize(QSize(200, 30))
        self.con2_q.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con2_q, 4, 3, 1, 1)

        self.con1_x_9 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_9.setObjectName(u"con1_x_9")
        self.con1_x_9.setMinimumSize(QSize(200, 30))
        self.con1_x_9.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_9, 7, 2, 1, 1)

        self.con2 = QLabel(self.gridLayoutWidget_2)
        self.con2.setObjectName(u"con2")
        self.con2.setMinimumSize(QSize(70, 30))
        self.con2.setMaximumSize(QSize(70, 30))
        self.con2.setFont(font2)

        self.gridLayout_4.addWidget(self.con2, 4, 0, 1, 1)

        self.con2_x = QLineEdit(self.gridLayoutWidget_2)
        self.con2_x.setObjectName(u"con2_x")
        self.con2_x.setMinimumSize(QSize(200, 30))
        self.con2_x.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con2_x, 4, 1, 1, 1)

        self.con1_x_2 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_2.setObjectName(u"con1_x_2")
        self.con1_x_2.setMinimumSize(QSize(200, 30))
        self.con1_x_2.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_2, 6, 1, 1, 1)

        self.con1_x_10 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_10.setObjectName(u"con1_x_10")
        self.con1_x_10.setMinimumSize(QSize(200, 30))
        self.con1_x_10.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_10, 7, 3, 1, 1)

        self.con3_q = QLineEdit(self.gridLayoutWidget_2)
        self.con3_q.setObjectName(u"con3_q")
        self.con3_q.setMinimumSize(QSize(200, 30))
        self.con3_q.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con3_q, 2, 3, 1, 1)

        self.q_Label = QLabel(self.gridLayoutWidget_2)
        self.q_Label.setObjectName(u"q_Label")
        self.q_Label.setMinimumSize(QSize(200, 40))
        self.q_Label.setMaximumSize(QSize(200, 40))
        self.q_Label.setFont(font2)

        self.gridLayout_4.addWidget(self.q_Label, 0, 3, 1, 1)

        self.con1_x_11 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_11.setObjectName(u"con1_x_11")
        self.con1_x_11.setMinimumSize(QSize(200, 30))
        self.con1_x_11.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_11, 9, 1, 1, 1)

        self.con1_y = QLineEdit(self.gridLayoutWidget_2)
        self.con1_y.setObjectName(u"con1_y")
        self.con1_y.setMinimumSize(QSize(200, 30))
        self.con1_y.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_y, 5, 2, 1, 1)

        self.con1_x = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x.setObjectName(u"con1_x")
        self.con1_x.setMinimumSize(QSize(200, 30))
        self.con1_x.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x, 5, 1, 1, 1)

        self.con1_x_7 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_7.setObjectName(u"con1_x_7")
        self.con1_x_7.setMinimumSize(QSize(200, 30))
        self.con1_x_7.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_7, 8, 3, 1, 1)

        self.con1_x_13 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_13.setObjectName(u"con1_x_13")
        self.con1_x_13.setMinimumSize(QSize(200, 30))
        self.con1_x_13.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_13, 10, 1, 1, 1)

        self.con1_q = QLineEdit(self.gridLayoutWidget_2)
        self.con1_q.setObjectName(u"con1_q")
        self.con1_q.setMinimumSize(QSize(200, 30))
        self.con1_q.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_q, 5, 3, 1, 1)

        self.con1_x_14 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_14.setObjectName(u"con1_x_14")
        self.con1_x_14.setMinimumSize(QSize(200, 30))
        self.con1_x_14.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_14, 11, 1, 1, 1)

        self.con3_y = QLineEdit(self.gridLayoutWidget_2)
        self.con3_y.setObjectName(u"con3_y")
        self.con3_y.setMinimumSize(QSize(200, 30))
        self.con3_y.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con3_y, 2, 2, 1, 1)

        self.x_Label = QLabel(self.gridLayoutWidget_2)
        self.x_Label.setObjectName(u"x_Label")
        self.x_Label.setMinimumSize(QSize(200, 40))
        self.x_Label.setMaximumSize(QSize(200, 40))
        self.x_Label.setFont(font2)

        self.gridLayout_4.addWidget(self.x_Label, 0, 1, 1, 1)

        self.con2_y = QLineEdit(self.gridLayoutWidget_2)
        self.con2_y.setObjectName(u"con2_y")
        self.con2_y.setMinimumSize(QSize(200, 30))
        self.con2_y.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con2_y, 4, 2, 1, 1)

        self.con1_x_6 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_6.setObjectName(u"con1_x_6")
        self.con1_x_6.setMinimumSize(QSize(200, 30))
        self.con1_x_6.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_6, 8, 2, 1, 1)

        self.con1_x_4 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_4.setObjectName(u"con1_x_4")
        self.con1_x_4.setMinimumSize(QSize(200, 30))
        self.con1_x_4.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_4, 6, 3, 1, 1)

        self.con3_x = QLineEdit(self.gridLayoutWidget_2)
        self.con3_x.setObjectName(u"con3_x")
        self.con3_x.setMinimumSize(QSize(200, 30))
        self.con3_x.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con3_x, 2, 1, 1, 1)

        self.con3_4 = QLabel(self.gridLayoutWidget_2)
        self.con3_4.setObjectName(u"con3_4")
        self.con3_4.setMinimumSize(QSize(70, 30))
        self.con3_4.setMaximumSize(QSize(70, 30))
        self.con3_4.setFont(font2)

        self.gridLayout_4.addWidget(self.con3_4, 7, 0, 1, 1)

        self.con1_x_5 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_5.setObjectName(u"con1_x_5")
        self.con1_x_5.setMinimumSize(QSize(200, 30))
        self.con1_x_5.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_5, 8, 1, 1, 1)

        self.con3_2 = QLabel(self.gridLayoutWidget_2)
        self.con3_2.setObjectName(u"con3_2")
        self.con3_2.setMinimumSize(QSize(70, 30))
        self.con3_2.setMaximumSize(QSize(70, 30))
        self.con3_2.setFont(font2)

        self.gridLayout_4.addWidget(self.con3_2, 6, 0, 1, 1)

        self.y_Label = QLabel(self.gridLayoutWidget_2)
        self.y_Label.setObjectName(u"y_Label")
        self.y_Label.setMinimumSize(QSize(200, 40))
        self.y_Label.setMaximumSize(QSize(200, 40))
        self.y_Label.setFont(font2)

        self.gridLayout_4.addWidget(self.y_Label, 0, 2, 1, 1)

        self.con3 = QLabel(self.gridLayoutWidget_2)
        self.con3.setObjectName(u"con3")
        self.con3.setMinimumSize(QSize(70, 30))
        self.con3.setMaximumSize(QSize(70, 30))
        self.con3.setFont(font2)

        self.gridLayout_4.addWidget(self.con3, 5, 0, 1, 1)

        self.con3_3 = QLabel(self.gridLayoutWidget_2)
        self.con3_3.setObjectName(u"con3_3")
        self.con3_3.setMinimumSize(QSize(70, 30))
        self.con3_3.setMaximumSize(QSize(70, 30))
        self.con3_3.setFont(font2)

        self.gridLayout_4.addWidget(self.con3_3, 8, 0, 1, 1)

        self.con1_x_8 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_8.setObjectName(u"con1_x_8")
        self.con1_x_8.setMinimumSize(QSize(200, 30))
        self.con1_x_8.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_8, 7, 1, 1, 1)

        self.con1 = QLabel(self.gridLayoutWidget_2)
        self.con1.setObjectName(u"con1")
        self.con1.setMinimumSize(QSize(70, 30))
        self.con1.setMaximumSize(QSize(70, 30))
        self.con1.setFont(font2)

        self.gridLayout_4.addWidget(self.con1, 2, 0, 1, 1)

        self.con1_x_3 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_3.setObjectName(u"con1_x_3")
        self.con1_x_3.setMinimumSize(QSize(200, 30))
        self.con1_x_3.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_3, 6, 2, 1, 1)

        self.con1_x_12 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_12.setObjectName(u"con1_x_12")
        self.con1_x_12.setMinimumSize(QSize(200, 30))
        self.con1_x_12.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_12, 9, 2, 1, 1)

        self.con1_x_15 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_15.setObjectName(u"con1_x_15")
        self.con1_x_15.setMinimumSize(QSize(200, 30))
        self.con1_x_15.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_15, 12, 1, 1, 1)

        self.con1_x_16 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_16.setObjectName(u"con1_x_16")
        self.con1_x_16.setMinimumSize(QSize(200, 30))
        self.con1_x_16.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_16, 9, 3, 1, 1)

        self.con1_x_17 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_17.setObjectName(u"con1_x_17")
        self.con1_x_17.setMinimumSize(QSize(200, 30))
        self.con1_x_17.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_17, 10, 2, 1, 1)

        self.con1_x_18 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_18.setObjectName(u"con1_x_18")
        self.con1_x_18.setMinimumSize(QSize(200, 30))
        self.con1_x_18.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_18, 10, 3, 1, 1)

        self.con1_x_19 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_19.setObjectName(u"con1_x_19")
        self.con1_x_19.setMinimumSize(QSize(200, 30))
        self.con1_x_19.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_19, 11, 2, 1, 1)

        self.con1_x_20 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_20.setObjectName(u"con1_x_20")
        self.con1_x_20.setMinimumSize(QSize(200, 30))
        self.con1_x_20.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_20, 11, 3, 1, 1)

        self.con1_x_21 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_21.setObjectName(u"con1_x_21")
        self.con1_x_21.setMinimumSize(QSize(200, 30))
        self.con1_x_21.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_21, 12, 2, 1, 1)

        self.con1_x_22 = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x_22.setObjectName(u"con1_x_22")
        self.con1_x_22.setMinimumSize(QSize(200, 30))
        self.con1_x_22.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x_22, 12, 3, 1, 1)

        self.con3_5 = QLabel(self.gridLayoutWidget_2)
        self.con3_5.setObjectName(u"con3_5")
        self.con3_5.setMinimumSize(QSize(70, 30))
        self.con3_5.setMaximumSize(QSize(70, 30))
        self.con3_5.setFont(font2)

        self.gridLayout_4.addWidget(self.con3_5, 9, 0, 1, 1)

        self.con3_6 = QLabel(self.gridLayoutWidget_2)
        self.con3_6.setObjectName(u"con3_6")
        self.con3_6.setMinimumSize(QSize(70, 30))
        self.con3_6.setMaximumSize(QSize(70, 30))
        self.con3_6.setFont(font2)

        self.gridLayout_4.addWidget(self.con3_6, 10, 0, 1, 1)

        self.con3_7 = QLabel(self.gridLayoutWidget_2)
        self.con3_7.setObjectName(u"con3_7")
        self.con3_7.setMinimumSize(QSize(70, 30))
        self.con3_7.setMaximumSize(QSize(70, 30))
        self.con3_7.setFont(font2)

        self.gridLayout_4.addWidget(self.con3_7, 11, 0, 1, 1)

        self.con3_8 = QLabel(self.gridLayoutWidget_2)
        self.con3_8.setObjectName(u"con3_8")
        self.con3_8.setMinimumSize(QSize(70, 30))
        self.con3_8.setMaximumSize(QSize(70, 30))
        self.con3_8.setFont(font2)

        self.gridLayout_4.addWidget(self.con3_8, 12, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.progress_bar = QProgressBar(Form)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(20, 480, 511, 23))
        self.progress_bar.setValue(24)
        self.calculateButton2 = QPushButton(Form)
        self.calculateButton2.setObjectName(u"calculateButton2")
        self.calculateButton2.setGeometry(QRect(300, 380, 241, 81))
        self.calculateButton2.setFont(font1)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(680, 420, 391, 341))
        self.scrollArea.raise_()
        self.title.raise_()
        self.calculateButton1.raise_()
        self.gridLayoutWidget.raise_()
        self.progress_bar.raise_()
        self.calculateButton2.raise_()
        self.widget.raise_()

        self.retranslateUi(Form)
        self.calculateButton1.clicked.connect(Form.calculate)
        self.calculateButton2.clicked.connect(Form.calculate)
        self.progress_bar.valueChanged.connect(self.calculateButton2.click)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6bd2\u6c14\u6cc4\u6f0f\u53cd\u6f14\u56fe\u50cf", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4e09\u4e2a\u5750\u6807\u4f4d\u7f6e\u4ee5\u53ca\u5bf9\u5e94\u7684\u6bd2\u6c14\u6d53\u5ea6", None))
        self.calculateButton1.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8ba1\u7b97\uff08\u4f18\u5316\uff09", None))
        self.interation_Label.setText(QCoreApplication.translate("Form", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.result_x.setText(QCoreApplication.translate("Form", u"x\u5750\u6807", None))
        self.result_y.setText(QCoreApplication.translate("Form", u"y\u5750\u6807", None))
        self.result_q.setText(QCoreApplication.translate("Form", u"\u6bd2\u6c14\u6d53\u5ea6", None))
        self.result_Label.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.con2.setText(QCoreApplication.translate("Form", u"\u5750\u68072\uff1a", None))
        self.q_Label.setText(QCoreApplication.translate("Form", u"\u6bd2\u6c14\u6d53\u5ea6", None))
        self.x_Label.setText(QCoreApplication.translate("Form", u"x\u5750\u6807", None))
        self.con3_4.setText(QCoreApplication.translate("Form", u"\u5750\u68075\uff1a", None))
        self.con3_2.setText(QCoreApplication.translate("Form", u"\u5750\u68074\uff1a", None))
        self.y_Label.setText(QCoreApplication.translate("Form", u"y\u5750\u6807", None))
        self.con3.setText(QCoreApplication.translate("Form", u"\u5750\u68073\uff1a", None))
        self.con3_3.setText(QCoreApplication.translate("Form", u"\u5750\u68076\uff1a", None))
        self.con1.setText(QCoreApplication.translate("Form", u"\u5750\u68071\uff1a", None))
        self.con3_5.setText(QCoreApplication.translate("Form", u"\u5750\u68077\uff1a", None))
        self.con3_6.setText(QCoreApplication.translate("Form", u"\u5750\u68078\uff1a", None))
        self.con3_7.setText(QCoreApplication.translate("Form", u"\u5750\u68079\uff1a", None))
        self.con3_8.setText(QCoreApplication.translate("Form", u"\u5750\u680710\uff1a", None))
        self.calculateButton2.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8ba1\u7b97\uff08\u8499\u5361\uff09", None))
    # retranslateUi

