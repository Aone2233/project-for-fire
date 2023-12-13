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
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1141, 812)
        self.input = QLabel(Form)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(40, 20, 391, 41))
        font = QFont()
        font.setFamilies([u"3D Isometric"])
        font.setPointSize(12)
        font.setBold(True)
        self.input.setFont(font)
        self.calculateButton = QPushButton(Form)
        self.calculateButton.setObjectName(u"calculateButton")
        self.calculateButton.setGeometry(QRect(20, 370, 300, 81))
        font1 = QFont()
        font1.setFamilies([u"\u9510\u5b57\u6f6e\u724c\u53ef\u53d8\u771f\u8a002.0\u7b80"])
        font1.setPointSize(16)
        self.calculateButton.setFont(font1)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 540, 501, 181))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.result_y = QLabel(self.gridLayoutWidget)
        self.result_y.setObjectName(u"result_y")
        font2 = QFont()
        font2.setFamilies([u"\u5f97\u610f\u9ed1"])
        font2.setPointSize(11)
        font2.setItalic(True)
        self.result_y.setFont(font2)

        self.gridLayout_2.addWidget(self.result_y, 3, 0, 1, 1)

        self.result_out_y = QLineEdit(self.gridLayoutWidget)
        self.result_out_y.setObjectName(u"result_out_y")
        self.result_out_y.setMinimumSize(QSize(400, 30))
        self.result_out_y.setMaximumSize(QSize(400, 30))

        self.gridLayout_2.addWidget(self.result_out_y, 3, 1, 1, 1)

        self.result_x = QLabel(self.gridLayoutWidget)
        self.result_x.setObjectName(u"result_x")
        self.result_x.setFont(font2)

        self.gridLayout_2.addWidget(self.result_x, 1, 0, 1, 1)

        self.result_out_q = QLineEdit(self.gridLayoutWidget)
        self.result_out_q.setObjectName(u"result_out_q")
        self.result_out_q.setMinimumSize(QSize(400, 30))
        self.result_out_q.setMaximumSize(QSize(400, 30))

        self.gridLayout_2.addWidget(self.result_out_q, 4, 1, 1, 1)

        self.result_q = QLabel(self.gridLayoutWidget)
        self.result_q.setObjectName(u"result_q")
        self.result_q.setFont(font2)

        self.gridLayout_2.addWidget(self.result_q, 4, 0, 1, 1)

        self.result_interation = QLineEdit(self.gridLayoutWidget)
        self.result_interation.setObjectName(u"result_interation")
        self.result_interation.setMinimumSize(QSize(60, 30))
        self.result_interation.setMaximumSize(QSize(60, 30))

        self.gridLayout_2.addWidget(self.result_interation, 5, 1, 1, 1)

        self.interation_Label = QLabel(self.gridLayoutWidget)
        self.interation_Label.setObjectName(u"interation_Label")
        self.interation_Label.setFont(font2)

        self.gridLayout_2.addWidget(self.interation_Label, 5, 0, 1, 1)

        self.result_out_x = QLineEdit(self.gridLayoutWidget)
        self.result_out_x.setObjectName(u"result_out_x")
        self.result_out_x.setMinimumSize(QSize(400, 30))
        self.result_out_x.setMaximumSize(QSize(400, 30))

        self.gridLayout_2.addWidget(self.result_out_x, 1, 1, 1, 1)

        self.result_Label = QLabel(self.gridLayoutWidget)
        self.result_Label.setObjectName(u"result_Label")
        self.result_Label.setFont(font2)

        self.gridLayout_2.addWidget(self.result_Label, 0, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 130, 691, 161))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.con2 = QLabel(self.gridLayoutWidget_2)
        self.con2.setObjectName(u"con2")
        self.con2.setFont(font2)

        self.gridLayout_4.addWidget(self.con2, 4, 0, 1, 1)

        self.x_Label = QLabel(self.gridLayoutWidget_2)
        self.x_Label.setObjectName(u"x_Label")
        self.x_Label.setFont(font2)

        self.gridLayout_4.addWidget(self.x_Label, 0, 1, 1, 1)

        self.con1 = QLabel(self.gridLayoutWidget_2)
        self.con1.setObjectName(u"con1")
        self.con1.setFont(font2)

        self.gridLayout_4.addWidget(self.con1, 2, 0, 1, 1)

        self.con3_y = QLineEdit(self.gridLayoutWidget_2)
        self.con3_y.setObjectName(u"con3_y")
        self.con3_y.setMinimumSize(QSize(200, 30))
        self.con3_y.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con3_y, 2, 2, 1, 1)

        self.con2_q = QLineEdit(self.gridLayoutWidget_2)
        self.con2_q.setObjectName(u"con2_q")
        self.con2_q.setMinimumSize(QSize(200, 30))
        self.con2_q.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con2_q, 4, 3, 1, 1)

        self.con2_x = QLineEdit(self.gridLayoutWidget_2)
        self.con2_x.setObjectName(u"con2_x")
        self.con2_x.setMinimumSize(QSize(200, 30))
        self.con2_x.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con2_x, 4, 1, 1, 1)

        self.con1_x = QLineEdit(self.gridLayoutWidget_2)
        self.con1_x.setObjectName(u"con1_x")
        self.con1_x.setMinimumSize(QSize(200, 30))
        self.con1_x.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_x, 5, 1, 1, 1)

        self.con3_x = QLineEdit(self.gridLayoutWidget_2)
        self.con3_x.setObjectName(u"con3_x")
        self.con3_x.setMinimumSize(QSize(200, 30))
        self.con3_x.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con3_x, 2, 1, 1, 1)

        self.con2_y = QLineEdit(self.gridLayoutWidget_2)
        self.con2_y.setObjectName(u"con2_y")
        self.con2_y.setMinimumSize(QSize(200, 30))
        self.con2_y.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con2_y, 4, 2, 1, 1)

        self.con1_y = QLineEdit(self.gridLayoutWidget_2)
        self.con1_y.setObjectName(u"con1_y")
        self.con1_y.setMinimumSize(QSize(200, 30))
        self.con1_y.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_y, 5, 2, 1, 1)

        self.con1_q = QLineEdit(self.gridLayoutWidget_2)
        self.con1_q.setObjectName(u"con1_q")
        self.con1_q.setMinimumSize(QSize(200, 30))
        self.con1_q.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con1_q, 5, 3, 1, 1)

        self.con3 = QLabel(self.gridLayoutWidget_2)
        self.con3.setObjectName(u"con3")
        self.con3.setFont(font2)

        self.gridLayout_4.addWidget(self.con3, 5, 0, 1, 1)

        self.y_Label = QLabel(self.gridLayoutWidget_2)
        self.y_Label.setObjectName(u"y_Label")
        self.y_Label.setFont(font2)

        self.gridLayout_4.addWidget(self.y_Label, 0, 2, 1, 1)

        self.con3_q = QLineEdit(self.gridLayoutWidget_2)
        self.con3_q.setObjectName(u"con3_q")
        self.con3_q.setMinimumSize(QSize(200, 30))
        self.con3_q.setMaximumSize(QSize(200, 30))

        self.gridLayout_4.addWidget(self.con3_q, 2, 3, 1, 1)

        self.q_Label = QLabel(self.gridLayoutWidget_2)
        self.q_Label.setObjectName(u"q_Label")
        self.q_Label.setFont(font2)

        self.gridLayout_4.addWidget(self.q_Label, 0, 3, 1, 1)


        self.retranslateUi(Form)
        self.calculateButton.clicked.connect(Form.calculate)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.input.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4e09\u4e2a\u5750\u6807\u4f4d\u7f6e\u4ee5\u53ca\u5bf9\u5e94\u7684\u6bd2\u6c14\u6d53\u5ea6", None))
        self.calculateButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.result_y.setText(QCoreApplication.translate("Form", u"y\u5750\u6807", None))
        self.result_x.setText(QCoreApplication.translate("Form", u"x\u5750\u6807", None))
        self.result_q.setText(QCoreApplication.translate("Form", u"\u6bd2\u6c14\u6d53\u5ea6", None))
        self.interation_Label.setText(QCoreApplication.translate("Form", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.result_Label.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.con2.setText(QCoreApplication.translate("Form", u"\u5750\u68072\uff1a", None))
        self.x_Label.setText(QCoreApplication.translate("Form", u"x\u5750\u6807", None))
        self.con1.setText(QCoreApplication.translate("Form", u"\u5750\u68071\uff1a", None))
        self.con3.setText(QCoreApplication.translate("Form", u"\u5750\u68073\uff1a", None))
        self.y_Label.setText(QCoreApplication.translate("Form", u"y\u5750\u6807", None))
        self.q_Label.setText(QCoreApplication.translate("Form", u"\u6bd2\u6c14\u6d53\u5ea6", None))
    # retranslateUi

