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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(988, 668)
        self.input = QLabel(Form)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(40, 20, 391, 41))
        font = QFont()
        font.setFamilies([u"3D Isometric"])
        font.setPointSize(12)
        font.setBold(True)
        self.input.setFont(font)
        self.con1_x = QLineEdit(Form)
        self.con1_x.setObjectName(u"con1_x")
        self.con1_x.setGeometry(QRect(130, 150, 60, 30))
        self.con1_x.setMinimumSize(QSize(60, 30))
        self.con1_x.setMaximumSize(QSize(60, 30))
        self.con1 = QLabel(Form)
        self.con1.setObjectName(u"con1")
        self.con1.setGeometry(QRect(30, 155, 72, 20))
        font1 = QFont()
        font1.setFamilies([u"\u5f97\u610f\u9ed1"])
        font1.setPointSize(11)
        font1.setItalic(True)
        self.con1.setFont(font1)
        self.con1_y = QLineEdit(Form)
        self.con1_y.setObjectName(u"con1_y")
        self.con1_y.setGeometry(QRect(210, 150, 60, 30))
        self.con1_y.setMinimumSize(QSize(60, 30))
        self.con1_y.setMaximumSize(QSize(60, 30))
        self.con2 = QLabel(Form)
        self.con2.setObjectName(u"con2")
        self.con2.setGeometry(QRect(30, 214, 72, 21))
        self.con2.setFont(font1)
        self.con2_x = QLineEdit(Form)
        self.con2_x.setObjectName(u"con2_x")
        self.con2_x.setGeometry(QRect(130, 210, 60, 30))
        self.con2_x.setMinimumSize(QSize(60, 30))
        self.con2_x.setMaximumSize(QSize(60, 30))
        self.con2_y = QLineEdit(Form)
        self.con2_y.setObjectName(u"con2_y")
        self.con2_y.setGeometry(QRect(210, 210, 60, 30))
        self.con2_y.setMinimumSize(QSize(60, 30))
        self.con2_y.setMaximumSize(QSize(60, 30))
        self.con3 = QLabel(Form)
        self.con3.setObjectName(u"con3")
        self.con3.setGeometry(QRect(30, 280, 72, 21))
        self.con3.setFont(font1)
        self.con2_x_2 = QLineEdit(Form)
        self.con2_x_2.setObjectName(u"con2_x_2")
        self.con2_x_2.setGeometry(QRect(130, 270, 60, 30))
        self.con2_x_2.setMinimumSize(QSize(60, 30))
        self.con2_x_2.setMaximumSize(QSize(60, 30))
        self.con3_y = QLineEdit(Form)
        self.con3_y.setObjectName(u"con3_y")
        self.con3_y.setGeometry(QRect(210, 270, 60, 30))
        self.con3_y.setMinimumSize(QSize(60, 30))
        self.con3_y.setMaximumSize(QSize(60, 30))
        self.con1_q = QLineEdit(Form)
        self.con1_q.setObjectName(u"con1_q")
        self.con1_q.setGeometry(QRect(310, 150, 120, 30))
        self.con1_q.setMinimumSize(QSize(120, 30))
        self.con1_q.setMaximumSize(QSize(120, 30))
        self.con2_q = QLineEdit(Form)
        self.con2_q.setObjectName(u"con2_q")
        self.con2_q.setGeometry(QRect(310, 210, 120, 30))
        self.con2_q.setMinimumSize(QSize(120, 30))
        self.con2_q.setMaximumSize(QSize(120, 30))
        self.con3_q = QLineEdit(Form)
        self.con3_q.setObjectName(u"con3_q")
        self.con3_q.setGeometry(QRect(310, 270, 120, 30))
        self.con3_q.setMinimumSize(QSize(120, 30))
        self.con3_q.setMaximumSize(QSize(120, 30))
        self.x_Label = QLabel(Form)
        self.x_Label.setObjectName(u"x_Label")
        self.x_Label.setGeometry(QRect(140, 100, 61, 21))
        self.x_Label.setFont(font1)
        self.y_Label = QLabel(Form)
        self.y_Label.setObjectName(u"y_Label")
        self.y_Label.setGeometry(QRect(220, 100, 61, 21))
        self.y_Label.setFont(font1)
        self.q_Label = QLabel(Form)
        self.q_Label.setObjectName(u"q_Label")
        self.q_Label.setGeometry(QRect(310, 100, 61, 21))
        self.q_Label.setFont(font1)
        self.result_Label = QLabel(Form)
        self.result_Label.setObjectName(u"result_Label")
        self.result_Label.setGeometry(QRect(30, 440, 72, 20))
        self.result_Label.setFont(font1)
        self.result_out_y_2 = QLineEdit(Form)
        self.result_out_y_2.setObjectName(u"result_out_y_2")
        self.result_out_y_2.setGeometry(QRect(310, 490, 120, 30))
        self.result_out_y_2.setMinimumSize(QSize(120, 30))
        self.result_out_y_2.setMaximumSize(QSize(120, 30))
        self.result_y = QLabel(Form)
        self.result_y.setObjectName(u"result_y")
        self.result_y.setGeometry(QRect(220, 440, 61, 21))
        self.result_y.setFont(font1)
        self.result_out_x = QLineEdit(Form)
        self.result_out_x.setObjectName(u"result_out_x")
        self.result_out_x.setGeometry(QRect(130, 490, 60, 30))
        self.result_out_x.setMinimumSize(QSize(60, 30))
        self.result_out_x.setMaximumSize(QSize(60, 30))
        self.result_out_y = QLineEdit(Form)
        self.result_out_y.setObjectName(u"result_out_y")
        self.result_out_y.setGeometry(QRect(210, 490, 60, 30))
        self.result_out_y.setMinimumSize(QSize(60, 30))
        self.result_out_y.setMaximumSize(QSize(60, 30))
        self.result_q = QLabel(Form)
        self.result_q.setObjectName(u"result_q")
        self.result_q.setGeometry(QRect(310, 440, 61, 21))
        self.result_q.setFont(font1)
        self.result_x = QLabel(Form)
        self.result_x.setObjectName(u"result_x")
        self.result_x.setGeometry(QRect(140, 440, 61, 21))
        self.result_x.setFont(font1)
        self.interation_Label = QLabel(Form)
        self.interation_Label.setObjectName(u"interation_Label")
        self.interation_Label.setGeometry(QRect(30, 550, 72, 20))
        self.interation_Label.setFont(font1)
        self.result_interation = QLineEdit(Form)
        self.result_interation.setObjectName(u"result_interation")
        self.result_interation.setGeometry(QRect(130, 550, 60, 30))
        self.result_interation.setMinimumSize(QSize(60, 30))
        self.result_interation.setMaximumSize(QSize(60, 30))
        self.calculate_Button = QPushButton(Form)
        self.calculate_Button.setObjectName(u"calculate_Button")
        self.calculate_Button.setGeometry(QRect(120, 340, 131, 51))
        font2 = QFont()
        font2.setFamilies([u"\u9510\u5b57\u6f6e\u724c\u53ef\u53d8\u771f\u8a002.0\u7b80"])
        font2.setPointSize(16)
        self.calculate_Button.setFont(font2)

        self.retranslateUi(Form)
        self.calculate_Button.clicked.connect(Form.calculate)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.input.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4e09\u4e2a\u5750\u6807\u4f4d\u7f6e\u4ee5\u53ca\u5bf9\u5e94\u7684\u6bd2\u6c14\u6d53\u5ea6", None))
        self.con1.setText(QCoreApplication.translate("Form", u"\u5750\u68071\uff1a", None))
        self.con2.setText(QCoreApplication.translate("Form", u"\u5750\u68072\uff1a", None))
        self.con3.setText(QCoreApplication.translate("Form", u"\u5750\u68073\uff1a", None))
        self.x_Label.setText(QCoreApplication.translate("Form", u"x\u5750\u6807", None))
        self.y_Label.setText(QCoreApplication.translate("Form", u"y\u5750\u6807", None))
        self.q_Label.setText(QCoreApplication.translate("Form", u"\u6bd2\u6c14\u6d53\u5ea6", None))
        self.result_Label.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.result_y.setText(QCoreApplication.translate("Form", u"y\u5750\u6807", None))
        self.result_q.setText(QCoreApplication.translate("Form", u"\u6bd2\u6c14\u6d53\u5ea6", None))
        self.result_x.setText(QCoreApplication.translate("Form", u"x\u5750\u6807", None))
        self.interation_Label.setText(QCoreApplication.translate("Form", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.calculate_Button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8ba1\u7b97", None))
    # retranslateUi

