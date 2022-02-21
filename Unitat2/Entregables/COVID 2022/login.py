from PySide6.QtWidgets import (
    QApplication, QFormLayout, QLineEdit,
    QPushButton, QLabel, QWidget
)
from PySide6.QtCore import (QCoreApplication, Qt)

import sys

import dialogo_eleccion as dialogo
import principal
import bases_de_datos as bd


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
        if(bd.sql_read(user, password)):
            self.show_covid()
            self.hide()
        else:
            self.dialogo()

    def show_covid(self):
        if self.w is None:
            self.w = principal.mainw(self)
        self.w.window.show()

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


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    window = Login()
    window.show()
    sys.exit(app.exec())