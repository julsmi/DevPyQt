# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(656, 512)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 81, 16))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.noteHead = QPlainTextEdit(Form)
        self.noteHead.setObjectName(u"noteHead")
        self.noteHead.setGeometry(QRect(10, 40, 341, 31))
        self.note_Text = QPlainTextEdit(Form)
        self.note_Text.setObjectName(u"note_Text")
        self.note_Text.setGeometry(QRect(10, 100, 481, 171))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 141, 21))
        self.label_2.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(450, 20, 160, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.dateTimeEdit = QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateTimeEdit)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(500, 100, 90, 86))
        self.verticalLayout = QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.saveButton = QPushButton(self.horizontalLayoutWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)

        self.delete_Button = QPushButton(self.horizontalLayoutWidget)
        self.delete_Button.setObjectName(u"delete_Button")

        self.verticalLayout.addWidget(self.delete_Button)

        self.newNoteButton = QPushButton(self.horizontalLayoutWidget)
        self.newNoteButton.setObjectName(u"newNoteButton")

        self.verticalLayout.addWidget(self.newNoteButton)

        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 280, 381, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.dateTimeEdit_2 = QDateTimeEdit(self.horizontalLayoutWidget_2)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.dateTimeEdit_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 340, 321, 151))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043c\u0430", None))
        self.noteHead.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043c\u0443 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.note_Text.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0435\u0434\u043b\u0430\u0439\u043d", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.delete_Button.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.newNoteButton.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043c\u0435\u0442\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
    # retranslateUi

