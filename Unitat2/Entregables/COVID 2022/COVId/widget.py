
import sys
import os
import PySide6.QtCore

from Custom_Widgets.Widgets import *
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader





class mainw(QMainWindow):
    def __init__(self):
        super(mainw, self).__init__()
        self.window = self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        return loader.load(path, self)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    widget = mainw()
    widget.window.show()
    sys.exit(app.exec())
