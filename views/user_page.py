from typing import Optional
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient, QStandardItem,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit, QMessageBox,
                               QHeaderView, QLabel, QLineEdit, QListView, QAbstractItemView,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QStackedWidget, QStatusBar, QTableView,
                               QWidget)

from model.user_model import UserModel


class UserPage(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.user_model = UserModel()
        font = QFont()
        font.setPointSize(14)
        self.label_7 = QLabel(self)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(450, 170, 58, 18))
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(510, 170, 113, 26))
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(540, 230, 80, 26))
        self.pushButton_2.clicked.connect(self.addUser)
        self.listView = QTableView(self)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(90, 80, 281, 411))
        # tableView 允许右键菜单
        self.listView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listView.setContextMenuPolicy(Qt.ActionsContextMenu)

        # 具体菜单项
        del_option = QAction(self.listView)
        del_option.setText("删除人员")
        del_option.triggered.connect(self.del_pojo)

        # tableView 添加具体的右键菜单
        self.listView.addAction(del_option)

        self.label_8 = QLabel(self)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 40, 58, 18))

    def init_data(self):
        self.listView.setModel(self.user_model.getUsers())

    def del_pojo(self):
        # index = self.listView_2.currentIndex()
        data = self.listView.selectionModel().selectedIndexes()
        id_index = data[0]
        id = id_index.data()
        # 删除数据
        self.user_model.del_pojo(id)
        # 刷新数据
        self.init_data()

    def addUser(self):
        self.pushButton_2.setEnabled(False)
        userName = self.lineEdit.text()
        # 检测是否已存在
        exists_flag = self.user_model.queryByName(userName)
        if (exists_flag):
            QMessageBox.warning(self, "提示", f'人员: "{userName}"已存在')
            self.pushButton_2.setEnabled(True)
            return
        self.user_model.addUser(userName)
        self.lineEdit.clear()
        QMessageBox.information(self, "操作成功",
                                f'"{userName}" 已添加到人员列表.')
        self.listView.setModel(self.user_model.getUsers())
        self.pushButton_2.setEnabled(True)
