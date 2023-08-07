# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainwindow.ui'
##
# Created by: Qt User Interface Compiler version 6.5.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from re import S
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
                               QHeaderView, QLabel, QLineEdit, QListView,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QStackedWidget, QStatusBar, QTableView,
                               QWidget)
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
import os
from views.borrow_page import BorrowPage

from model.dbutil import DBUtil
from views.product_page import ProductPage
from views.record_page import RecordPage
from views.user_page import UserPage


class Ui_MainWindow(object):

    def __init__(self) -> None:
        self.dbutil = DBUtil()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 650)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1001, 624))

        # 登记页面
        self.borrowPage = BorrowPage()
        self.borrowPage.setObjectName(u"borrowPage")
        self.stackedWidget.addWidget(self.borrowPage)

        # 人员列表页面
        self.userPage = UserPage()
        self.userPage.setObjectName(u"userPage")
        self.stackedWidget.addWidget(self.userPage)

        # 记录页面
        self.recordPage = RecordPage()
        self.recordPage.setObjectName(u"recordPage")
        self.stackedWidget.addWidget(self.recordPage)

        # 仪器列表页面
        self.produpage = ProductPage()
        self.produpage.setObjectName(u"produpage")
        self.stackedWidget.addWidget(self.produpage)

        MainWindow.setCentralWidget(self.centralwidget)

        #####
        # 工具栏
        #####
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 920, 24))
        self.setMenuList(MainWindow)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        self.borrowPage.init_data()

        QMetaObject.connectSlotsByName(MainWindow)

    # 菜单设置
    def setMenuList(self, MainWindow):
        menu = self.menubar

        borrow_button_action = QAction("借用登记", MainWindow)
        borrow_button_action.triggered.connect(self.gotoBorrowPage)
        menu.addAction(borrow_button_action)

        record_button_action = QAction("记录查询", MainWindow)
        record_button_action.triggered.connect(self.gotoRecordPage)
        menu.addAction(record_button_action)

        user_button_action = QAction("人员列表", MainWindow)
        user_button_action.triggered.connect(self.gotoUserPage)
        menu.addAction(user_button_action)

        product_button_action = QAction("仪器列表", MainWindow)
        product_button_action.triggered.connect(self.gotoProductPage)
        menu.addAction(product_button_action)
        MainWindow.setMenuBar(self.menubar)
    # setupUi

    # 汉化标题
    def retranslateUi(self, MainWindow):
        # borrow_page
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"\u53f0\u8d26\u5c0f\u5de5\u5177", None))
        self.borrowPage.label.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eea\u5668", None))
        self.borrowPage.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u7f16\u53f7", None))
        self.borrowPage.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eba\u5458", None))
        self.borrowPage.saveborrow.setText(QCoreApplication.translate(
            "MainWindow", u"\u767b\u8bb0", None))
        self.borrowPage.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"\u5f00\u59cb\u65e5\u671f", None))
        self.borrowPage.label_14.setText(QCoreApplication.translate(
            "MainWindow", u"\u7ed3\u675f\u65e5\u671f", None))
        self.borrowPage.dateEdit_2.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.borrowPage.dateEdit_3.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        # user_page
        self.userPage.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"\u540d\u5b57", None))
        self.userPage.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u65b0\u589e", None))
        self.userPage.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eba\u5458\u5217\u8868", None))
        # .recordPage
        self.recordPage.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"\u65e5\u671f", None))
        self.recordPage.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eba\u5458", None))
        self.recordPage.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eea\u5668", None))

        self.recordPage.dateEdit.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.recordPage.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"\u67e5\u8be2", None))
        self.recordPage.exportExcel.setText(QCoreApplication.translate(
            "MainWindow", u"\u5bfc\u51fa", None))
        # ProductPage
        self.produpage.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eea\u5668\u5217\u8868", None))
        self.produpage.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eea\u5668\u89c4\u683c", None))
        self.produpage.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eea\u5668\u7f16\u53f7", None))
        self.produpage.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eea\u5668\u540d\u79f0", None))
        self.produpage.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"\u5382\u5bb6\u7f16\u53f7", None))

        self.produpage.pushButton_3.setText(QCoreApplication.translate(
            "MainWindow", u"\u65b0\u589e", None))
    # retranslateUi

    def gotoBorrowPage(self):
        self.gotoWinPage(0)
        self.borrowPage.init_data()

    def gotoUserPage(self):
        self.gotoWinPage(1)
        self.userPage.init_data()

    def gotoRecordPage(self):
        self.gotoWinPage(2)
        self.recordPage.init_data()

    def gotoProductPage(self):
        self.gotoWinPage(3)
        self.produpage.init_data()

    def gotoWinPage(self, index):
        self.stackedWidget.setCurrentIndex(index)
