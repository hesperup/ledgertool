import calendar
import datetime
import os
import string
import time
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
                               QHeaderView, QLabel, QLineEdit, QListView, QMessageBox,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QStackedWidget, QStatusBar, QTableView,
                               QWidget)

from model.record_model import RecordModel
from model.user_model import UserModel
from model.product_model import ProductModel
from openpyxl import Workbook
from win32com import client


class RecordPage(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.record_model = RecordModel()
        self.user_model = UserModel()
        self.pro_model = ProductModel()
        font = QFont()
        font.setPointSize(14)
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 80, 58, 18))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 80, 58, 18))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(470, 80, 58, 18))
        self.label_6.setFont(font)
        self.dateEdit = QDateEdit(QDate.currentDate(), self)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setGeometry(QRect(110, 70, 138, 41))
        self.dateEdit.setFont(font)
        # self.dateEdit.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateEdit.setCalendarPopup(True)
        # self.dateEdit.setDate(QDate(2023, 8, 1))
        # 人员
        self.comboBox = QComboBox(self)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(330, 70, 121, 41))
        self.comboBox.setFont(font)

        # 仪器
        self.comboBox_2 = QComboBox(self)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(540, 70, 131, 41))
        self.comboBox_2.setFont(font)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(710, 70, 91, 41))
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.queryRecordsByParam)

        # excel
        self.exportExcel = QPushButton(self)
        self.exportExcel.setGeometry(QRect(800, 70, 91, 41))
        self.exportExcel.setFont(font)
        self.exportExcel.clicked.connect(self.export_excel)

        self.tableView = QTableView(self)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 130, 861, 461))
        # record_list = self.record_model.getRecords()
        # self.tableView.setModel(record_list)

    def init_data(self):
        record_list = self.record_model.getRecords()
        self.tableView.setModel(record_list)
        self.init_user()
        self.init_product()

    def export_excel(self):
        self.queryRecordsByParam()
        query_date = self.dateEdit.text()
        prodt_name = self.comboBox_2.currentText()
        user_name = self.comboBox.currentText()
        # 创建一个 workbook
        wb = Workbook()
        # 获取被激活的 worksheet
        ws = wb.active
        self.exportExcel.setEnabled(False)
        record_list = self.record_model.getRecordList(
            user_name, prodt_name, query_date)
        for f in range(len(record_list)):
            ws.append(record_list[f])
        ws.column_dimensions['A'].width = 22
        ws.column_dimensions['C'].width = 25
        ws.column_dimensions['D'].width = 14
        ws.column_dimensions['E'].width = 12
        ws.column_dimensions['F'].width = 12

        ts = calendar.timegm(time.gmtime())

        filename = str(ts)+".xlsx"
        fullPath = os.path.join(os.path.expanduser('~'),
                                filename)  # 得到完整的filepath
        wb.save(fullPath)

        et = client.DispatchEx("Excel.Application")
        # 0或者False都可以
        et.Visible = 1  # 不显示
        et.DisplayAlerts = 0  # 不警告
        wbc = et.Workbooks.Open(fullPath)

    def queryRecordsByParam(self):
        query_date = self.dateEdit.text()
        prodt_name = self.comboBox_2.currentText()
        user_name = self.comboBox.currentText()
        self.tableView.setModel(self.record_model.getRecordsByQuery(
            user_name, prodt_name, query_date))

    def init_user(self):
        self.comboBox.clear()
        user_list = self.user_model.queryUserList()
        for name in user_list:
            self.comboBox.addItem(name)

    def init_product(self):
        self.comboBox_2.clear()
        prod_list = self.pro_model.queryProdList()
        for name in prod_list:
            self.comboBox_2.addItem(name)
