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
import datetime


class BorrowPage(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.record_model = RecordModel()
        self.user_model = UserModel()
        self.pro_model = ProductModel()
        self.ptypeselect = QComboBox(self)
        self.ptypeselect.setObjectName(u"ptypeselect")
        self.ptypeselect.setGeometry(QRect(350, 100, 181, 41))
        self.ptypeselect.activated.connect(self.changePid)
        self.pidselect = QComboBox(self)
        self.pidselect.setObjectName(u"pidselect")
        self.pidselect.setGeometry(QRect(350, 180, 181, 41))
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 110, 81, 20))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 190, 81, 20))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 270, 81, 20))
        self.label_3.setFont(font)
        self.userselect = QComboBox(self)
        self.userselect.setObjectName(u"userselect")
        self.userselect.setGeometry(QRect(350, 260, 181, 41))
        # save
        self.saveborrow = QPushButton(self)
        self.saveborrow.setObjectName(u"saveborrow")
        self.saveborrow.setGeometry(QRect(590, 520, 91, 31))
        self.saveborrow.setFont(font)
        self.saveborrow.clicked.connect(self.save)

        # ke hu 名称
        self.label_15 = QLabel(self)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(230, 340, 81, 20))
        self.label_15.setFont(font)

        self.customer = QLineEdit(self)
        self.customer.setObjectName(u"customer")
        self.customer.setGeometry(QRect(350, 330, 181, 41))

        self.label_13 = QLabel(self)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(230, 410, 81, 20))
        self.label_13.setFont(font)
        self.label_14 = QLabel(self)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(230, 490, 81, 20))
        self.label_14.setFont(font)

        self.dateEdit_2 = QDateEdit(QDate.currentDate(), self)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(350, 400, 181, 41))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_3 = QDateEdit(QDate.currentDate(), self)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setGeometry(QRect(350, 470, 181, 41))
        self.dateEdit_3.setCalendarPopup(True)

    def init_data(self):
        self.init_user()
        self.init_product()
        self.pidselect.clear()

    def save(self):
        # 禁用按钮
        self.saveborrow.setEnabled(False)
        # 校验数据
        id = self.pidselect.currentText()
        name = self.userselect.currentText()
        customer = self.customer.text()
        start = self.dateEdit_2.text()
        end = self.dateEdit_3.text()
        if not id:
            QMessageBox.warning(self, "提示", f'仪器编号不能为空')
            self.saveborrow.setEnabled(True)
            return
        if not name:
            QMessageBox.warning(self, "提示", f'人员不能为空')
            self.saveborrow.setEnabled(True)
            return
        start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
        if (start_date > end_date):
            QMessageBox.warning(self, "提示", f'开始日期不能大于结束日期')
            self.saveborrow.setEnabled(True)
            return
        # 检测仪器是否已借用
        borro_flag = self.record_model.getBorrowFlag(id, start, end)
        if borro_flag:
            QMessageBox.warning(
                self, "提示", f'仪器: "{name}-{id}在{start}至{end}期间"已被借用')
            self.saveborrow.setEnabled(True)
            return
        # 记录借用
        user_id = self.user_model.queryIdByName(name)
        self.record_model.saveBorrow(id, user_id, start, end, customer)
        # 解除按钮
        self.ptypeselect.setCurrentIndex(0)
        self.pidselect.clear()
        self.userselect.setCurrentIndex(0)
        self.dateEdit_2.setDate(QDate.currentDate())
        self.dateEdit_3.setDate(QDate.currentDate())
        QMessageBox.information(self, "操作成功",
                                '登记成功')
        self.saveborrow.setEnabled(True)

    def init_user(self):
        self.userselect.clear()
        user_list = self.user_model.queryUserList()
        for name in user_list:
            self.userselect.addItem(name)

    def init_product(self):
        self.ptypeselect.clear()
        prod_list = self.pro_model.queryProdList()
        for name in prod_list:
            self.ptypeselect.addItem(name)

    def changePid(self):
        self.pidselect.clear()
        prod_name = self.ptypeselect.currentText()
        # print(prod_name)
        qid_list = self.pro_model.queryPidList(prod_name)
        for id in qid_list:
            self.pidselect.addItem(id)
