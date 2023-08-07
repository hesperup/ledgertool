import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow
from model.dbutil import DBUtil
from views.main_ui import Ui_MainWindow

# basedir = os.path.dirname(__file__)


if __name__ == "__main__":
    # loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    # db init
    DBUtil.init_db()
    # window = loader.load(os.path.join(basedir, "mainwindow.ui"), None)
    main = QMainWindow()
    ui_win = Ui_MainWindow()
    ui_win.setupUi(main)
    main.show()
    app.exec()
