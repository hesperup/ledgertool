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

from model.product_model import ProductModel


class ProductPage(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.product_model = ProductModel()
        font = QFont()
        font.setPointSize(14)
        self.listView_2 = QTableView(self)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(70, 50, 400, 531))

        self.label_9 = QLabel(self)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 20, 58, 18))
        self.label_10 = QLabel(self)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(480, 210, 58, 18))
        self.label_11 = QLabel(self)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(480, 100, 58, 18))
        self.label_12 = QLabel(self)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(480, 160, 58, 18))
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(640, 290, 91, 31))
        self.pushButton_3.clicked.connect(self.addProduct)
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(560, 90, 161, 31))
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(560, 150, 161, 31))
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(560, 210, 161, 31))

    def init_data(self):
        self.listView_2.setModel(self.product_model.getProducts())

    def addProduct(self):
        self.pushButton_3.setEnabled(False)
        id = self.lineEdit_2.text()
        name = self.lineEdit_3.text()
        spec = self.lineEdit_4.text()
        if not id or not name:
            QMessageBox.warning(self, "提示", f'编号和仪器名称不能为空')
            self.pushButton_3.setEnabled(True)
            return
        # 检测是否已存在
        exists_flag = self.product_model.queryById(id)
        if (exists_flag):
            QMessageBox.warning(self, "提示", f'编号: "{id}"已存在')
            self.pushButton_3.setEnabled(True)
            return
        self.product_model.addUser(id, name, spec)
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        QMessageBox.information(self, "操作成功",
                                f'"{id}:{name}" 已添加到仪器列表.')
        self.listView_2.setModel(self.product_model.getProducts())
        self.pushButton_3.setEnabled(True)
