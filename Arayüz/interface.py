# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(957, 629)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                  stop:0 #2E2E2E, stop:1 #1C1C1C);\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                  stop:0 #2E2E2E, stop:1 #1C1C1C);\n"
"")
        self.pushButton_chart = QPushButton(self.centralwidget)
        self.pushButton_chart.setObjectName(u"pushButton_chart")
        self.pushButton_chart.setGeometry(QRect(710, 20, 221, 61))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_chart.setFont(font)
        self.pushButton_chart.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 91, 20))
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 110, 121, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 180, 181, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 260, 151, 41))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 350, 101, 21))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 410, 119, 20))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(400, 330, 73, 20))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(330, 260, 191, 20))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(350, 190, 221, 20))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(410, 40, 101, 31))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(370, 120, 151, 20))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.lineEdit_age = QLineEdit(self.centralwidget)
        self.lineEdit_age.setObjectName(u"lineEdit_age")
        self.lineEdit_age.setGeometry(QRect(177, 38, 125, 28))
        self.lineEdit_age.setStyleSheet(u"QLineEdit, QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"	font-weight: bold;\n"
"}")
        self.comboBox_loan_grade = QComboBox(self.centralwidget)
        self.comboBox_loan_grade.addItem("")
        self.comboBox_loan_grade.addItem("")
        self.comboBox_loan_grade.addItem("")
        self.comboBox_loan_grade.addItem("")
        self.comboBox_loan_grade.addItem("")
        self.comboBox_loan_grade.addItem("")
        self.comboBox_loan_grade.addItem("")
        self.comboBox_loan_grade.setObjectName(u"comboBox_loan_grade")
        self.comboBox_loan_grade.setGeometry(QRect(170, 410, 122, 28))
        self.comboBox_loan_grade.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    min-width: 100px;\n"
"    font: 10pt \"Segoe UI\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #aaa;\n"
"    background-color: #e1e1e1;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);  /* Qt Resource kullan\u0131labilir */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    selection-background-color: #87cefa;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"")
        self.comboBox_person_emp_length = QComboBox(self.centralwidget)
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.addItem("")
        self.comboBox_person_emp_length.setObjectName(u"comboBox_person_emp_length")
        self.comboBox_person_emp_length.setGeometry(QRect(190, 260, 122, 28))
        self.comboBox_person_emp_length.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    min-width: 100px;\n"
"    font: 10pt \"Segoe UI\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #aaa;\n"
"    background-color: #e1e1e1;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);  /* Qt Resource kullan\u0131labilir */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    selection-background-color: #87cefa;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"")
        self.comboBox_person_home_ownership = QComboBox(self.centralwidget)
        self.comboBox_person_home_ownership.addItem("")
        self.comboBox_person_home_ownership.addItem("")
        self.comboBox_person_home_ownership.addItem("")
        self.comboBox_person_home_ownership.addItem("")
        self.comboBox_person_home_ownership.setObjectName(u"comboBox_person_home_ownership")
        self.comboBox_person_home_ownership.setGeometry(QRect(190, 190, 122, 28))
        self.comboBox_person_home_ownership.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    min-width: 100px;\n"
"    font: 10pt \"Segoe UI\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #aaa;\n"
"    background-color: #e1e1e1;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);  /* Qt Resource kullan\u0131labilir */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    selection-background-color: #87cefa;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"")
        self.lineEdit_loan_amnt = QLineEdit(self.centralwidget)
        self.lineEdit_loan_amnt.setObjectName(u"lineEdit_loan_amnt")
        self.lineEdit_loan_amnt.setGeometry(QRect(530, 330, 125, 28))
        self.lineEdit_loan_amnt.setStyleSheet(u"QLineEdit, QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"	font-weight: bold;\n"
"}")
        self.comboBox_cb_person_cred_hist_length = QComboBox(self.centralwidget)
        self.comboBox_cb_person_cred_hist_length.addItem("")
        self.comboBox_cb_person_cred_hist_length.addItem("")
        self.comboBox_cb_person_cred_hist_length.addItem("")
        self.comboBox_cb_person_cred_hist_length.addItem("")
        self.comboBox_cb_person_cred_hist_length.setObjectName(u"comboBox_cb_person_cred_hist_length")
        self.comboBox_cb_person_cred_hist_length.setGeometry(QRect(530, 260, 122, 28))
        self.comboBox_cb_person_cred_hist_length.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    min-width: 100px;\n"
"    font: 10pt \"Segoe UI\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #aaa;\n"
"    background-color: #e1e1e1;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);  /* Qt Resource kullan\u0131labilir */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    selection-background-color: #87cefa;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"")
        self.lineEdit_loan_int_rate = QLineEdit(self.centralwidget)
        self.lineEdit_loan_int_rate.setObjectName(u"lineEdit_loan_int_rate")
        self.lineEdit_loan_int_rate.setGeometry(QRect(530, 40, 125, 28))
        self.lineEdit_loan_int_rate.setStyleSheet(u"QLineEdit, QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"	font-weight: bold;\n"
"}")
        self.lineEdit_loan_percent_income = QLineEdit(self.centralwidget)
        self.lineEdit_loan_percent_income.setObjectName(u"lineEdit_loan_percent_income")
        self.lineEdit_loan_percent_income.setGeometry(QRect(540, 110, 125, 28))
        self.lineEdit_loan_percent_income.setStyleSheet(u"QLineEdit, QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"	font-weight: bold;\n"
"}")
        self.pushButton_chart_3 = QPushButton(self.centralwidget)
        self.pushButton_chart_3.setObjectName(u"pushButton_chart_3")
        self.pushButton_chart_3.setEnabled(True)
        self.pushButton_chart_3.setGeometry(QRect(240, 490, 271, 61))
        self.pushButton_chart_3.setMinimumSize(QSize(50, 0))
        self.pushButton_chart_3.setFont(font)
        self.pushButton_chart_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(550, 480, 131, 31))
        self.label_8.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(550, 530, 131, 31))
        self.label_14.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(710, 480, 161, 31))
        self.lineEdit_8.setStyleSheet(u"QLineEdit, QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"	font-weight: bold;\n"
"}")
        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(710, 530, 161, 31))
        self.lineEdit_9.setStyleSheet(u"QLineEdit, QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"	font-weight: bold;\n"
"}")
        self.lineEdit_person_income = QLineEdit(self.centralwidget)
        self.lineEdit_person_income.setObjectName(u"lineEdit_person_income")
        self.lineEdit_person_income.setGeometry(QRect(170, 110, 125, 28))
        self.lineEdit_person_income.setStyleSheet(u"QLineEdit, QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"	font-weight: bold;\n"
"}")
        self.comboBox_loan_intent = QComboBox(self.centralwidget)
        self.comboBox_loan_intent.addItem("")
        self.comboBox_loan_intent.addItem("")
        self.comboBox_loan_intent.addItem("")
        self.comboBox_loan_intent.addItem("")
        self.comboBox_loan_intent.addItem("")
        self.comboBox_loan_intent.addItem("")
        self.comboBox_loan_intent.setObjectName(u"comboBox_loan_intent")
        self.comboBox_loan_intent.setGeometry(QRect(180, 340, 122, 28))
        self.comboBox_loan_intent.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    min-width: 100px;\n"
"    font: 10pt \"Segoe UI\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #aaa;\n"
"    background-color: #e1e1e1;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);  /* Qt Resource kullan\u0131labilir */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    selection-background-color: #87cefa;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"")
        self.comboBox_cb_person_default_on_file = QComboBox(self.centralwidget)
        self.comboBox_cb_person_default_on_file.addItem("")
        self.comboBox_cb_person_default_on_file.addItem("")
        self.comboBox_cb_person_default_on_file.setObjectName(u"comboBox_cb_person_default_on_file")
        self.comboBox_cb_person_default_on_file.setGeometry(QRect(540, 180, 122, 28))
        self.comboBox_cb_person_default_on_file.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    min-width: 100px;\n"
"    font: 10pt \"Segoe UI\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #aaa;\n"
"    background-color: #e1e1e1;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png);  /* Qt Resource kullan\u0131labilir */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #aaa;\n"
"    selection-background-color: #87cefa;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 957, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_chart.setText(QCoreApplication.translate("MainWindow", u"Tablolar\u0131 G\u00f6r\u00fcnt\u00fcle", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"person_age", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"person_income", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"person_home_ownership", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"person_emp_length", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"loan_intent", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"loan_grade", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"loan_amnt", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"cb_person_cred_hist_length", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"cb_person_default_on_file", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"loan_int_rate", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"loan_percent_income", None))
        self.comboBox_loan_grade.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.comboBox_loan_grade.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_loan_grade.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.comboBox_loan_grade.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.comboBox_loan_grade.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.comboBox_loan_grade.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.comboBox_loan_grade.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))

        self.comboBox_person_emp_length.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_person_emp_length.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_person_emp_length.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_person_emp_length.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_person_emp_length.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_person_emp_length.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_person_emp_length.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_person_emp_length.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_person_emp_length.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_person_emp_length.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.comboBox_person_home_ownership.setItemText(0, QCoreApplication.translate("MainWindow", u"Other", None))
        self.comboBox_person_home_ownership.setItemText(1, QCoreApplication.translate("MainWindow", u"Mortgage", None))
        self.comboBox_person_home_ownership.setItemText(2, QCoreApplication.translate("MainWindow", u"Rent", None))
        self.comboBox_person_home_ownership.setItemText(3, QCoreApplication.translate("MainWindow", u"Own", None))

        self.comboBox_cb_person_cred_hist_length.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_cb_person_cred_hist_length.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_cb_person_cred_hist_length.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_cb_person_cred_hist_length.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.pushButton_chart_3.setText(QCoreApplication.translate("MainWindow", u"Kredi Risk Durumunu Sorgula", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tahmin Sonucu", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"G\u00fcven Skoru", None))
        self.comboBox_loan_intent.setItemText(0, QCoreApplication.translate("MainWindow", u"Education", None))
        self.comboBox_loan_intent.setItemText(1, QCoreApplication.translate("MainWindow", u"Medical", None))
        self.comboBox_loan_intent.setItemText(2, QCoreApplication.translate("MainWindow", u"Venture", None))
        self.comboBox_loan_intent.setItemText(3, QCoreApplication.translate("MainWindow", u"HomeImprovement", None))
        self.comboBox_loan_intent.setItemText(4, QCoreApplication.translate("MainWindow", u"Debtconsolidation", None))
        self.comboBox_loan_intent.setItemText(5, QCoreApplication.translate("MainWindow", u"Personal", None))

        self.comboBox_cb_person_default_on_file.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_cb_person_default_on_file.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

    # retranslateUi

