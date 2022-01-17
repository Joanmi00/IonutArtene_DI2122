from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QLineEdit,
    QPushButton, QLabel, QVBoxLayout, QWidget,
)
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize

import sys

import dialogo_eleccion as dialogo


class Principal(QMainWindow):

    def __init__(self, user, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Principal")
        self.resize(QSize(300, 300))
        self.center()

        layout = QVBoxLayout()
        status_user = QLabel(f"{user}")
        self.label = QLabel("Estamos en el user "+user)
        widget = QWidget()

        log = QAction('&Logout', self)
        log.triggered.connect(self.login)
        salir = QAction('&Salir', self)
        salir.triggered.connect(self.close)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(log)
        file_menu.addAction(salir)

        status = self.statusBar()
        status.addPermanentWidget(status_user)

        layout.addWidget(self.label)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def login(self):
        w = Login()
        w.show()
        if(w.isVisible()):
            self.hide()

    def center(self):
        '''Centra la ventana en la pantalla'''
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        app.closeAllWindows()


class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.center()
        layoutV2 = QFormLayout()
        self.user = QLineEdit("")
        self.password = QLineEdit("")
        self.password.setEchoMode(QLineEdit.Password)
        layoutV2.addRow(QLabel("User : "), self.user)
        layoutV2.addRow(QLabel("Password : "), self.password)

        self.w = None
        self.button = QPushButton("Conectar")
        layoutV2.addRow(self.button)
        self.button.clicked.connect(
            lambda x: self.comprobacion_datos(self.user.text(),
                                              self.password.text()))
        self.setLayout(layoutV2)

    def comprobacion_datos(self, user, password):
        if(user == "admin" or user == "user" and password == "1234"):
            self.show_new_window(user)
            self.hide()
        else:
            self.dialogo()

    def show_new_window(self, user):
        if self.w is None:
            self.w = Principal(user, self)
        self.w.show()

    def dialogo(self):
        salida = dialogo.dialogo_eleccion(self)

        if not salida.exec():
            self.user.clear()
            self.password.clear()

    def center(self):
        '''Centra la ventana en la pantalla'''
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        app.closeAllWindows()


app = QApplication(sys.argv)
w = Login()
w.show()
app.exec()
