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
                               QMainWindow, QMenu, QMenuBar, QPushButton, QAbstractItemView,
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
        self.listView_2.setGeometry(QRect(70, 50, 500, 531))
        self.listView_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        # tableView 允许右键菜单
        self.listView_2.setContextMenuPolicy(Qt.ActionsContextMenu)

        # 具体菜单项
        del_option = QAction(self.listView_2)
        del_option.setText("删除")
        del_option.triggered.connect(self.del_product)

        # tableView 添加具体的右键菜单
        self.listView_2.addAction(del_option)

        self.label_9 = QLabel(self)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 20, 58, 18))

        self.label_10 = QLabel(self)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(580, 200, 58, 18))
        self.label_11 = QLabel(self)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(580, 100, 58, 18))
        self.label_12 = QLabel(self)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(580, 150, 58, 18))

        self.label_13 = QLabel(self)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(580, 250, 58, 18))

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(680, 290, 91, 31))
        self.pushButton_3.clicked.connect(self.addProduct)

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(660, 100, 161, 31))
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(660, 150, 161, 31))
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(660, 200, 161, 31))

        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(660, 250, 161, 31))

    def init_data(self):
        self.listView_2.setModel(self.product_model.getProducts())

    def del_product(self):
        # index = self.listView_2.currentIndex()
        data = self.listView_2.selectionModel().selectedIndexes()
        id_index = data[0]
        id = id_index.data()
        # 删除数据
        self.product_model.del_prod(id)
        # 刷新数据
        self.init_data()

    def addProduct(self):
        self.pushButton_3.setEnabled(False)
        id = self.lineEdit_2.text()
        name = self.lineEdit_3.text()
        spec = self.lineEdit_4.text()
        fac_id = self.lineEdit_5.text()
        if not id or not name:
            QMessageBox.warning(self, "提示", f'管理编号和仪器名称不能为空')
            self.pushButton_3.setEnabled(True)
            return
        # 检测是否已存在
        exists_flag = self.product_model.queryById(id)
        if (exists_flag):
            QMessageBox.warning(self, "提示", f'管理编号: "{id}"已存在')
            self.pushButton_3.setEnabled(True)
            return
        self.product_model.addProduct(id, name, spec, fac_id)
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        QMessageBox.information(self, "操作成功",
                                f'"{id}:{name}" 已添加到仪器列表.')
        self.listView_2.setModel(self.product_model.getProducts())
        self.pushButton_3.setEnabled(True)
