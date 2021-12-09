from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout,
    QGridLayout

)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Calculadora")
        num_col = 4
        dim = QSize(400, 400)
        layout = QVBoxLayout()

        self.valor = QLabel()
        self.valor.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.valor.setStyleSheet("border: 1px solid black;")

        self.bot = {}
        self.ver = False
        self.equal = False
        self.valores = ''

        button_list = [
            'AC', '()', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '+',
            '1', '2', '3', '-',
            '0', '.', '<=', '=']

        button_layout = QGridLayout()

        for element in button_list:
            self.bot[element] = QPushButton(element)

            button_layout.addWidget(self.bot[element],
                                    button_list.index(element) // num_col,
                                    button_list.index(element) % num_col

                                    )
            self.bot[element].clicked.connect(self.mod_label)

        layout.addWidget(self.valor)
        layout.addLayout(button_layout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setFixedSize(dim)
        self.setCentralWidget(widget)

    def mod_label(self):
        button = self.sender().text()
        self.verifica_valor(button)
        

    def verifica_valor(self, button):
        operacion = ['+', '*', '-', '/', ]
        numeros = ['0', '1', '2', '2', '3', '4', '5', '6', '7', '8', '9']
        dist = ['.', '%']
        # verificar si se a introducido una operacion
        for ope in operacion:
            if(ope == button):

                if(self.equal):

                    self.equal = False
                    self.valores += button
                    self.valor.setText(self.valor.text() + button)
                else:
                    self.valor.setText(self.valor.text() + button)
        # verificar si se ha introducido un numero
        for num in numeros:
            if(num == button):
                if(self.equal):
                    self.valor.setText(self.valor.text()[
                        :-len(self.valor.text())])
                    self.equal = False
                    self.valores += button
                    self.valor.setText(self.valor.text() + button)
                else:
                    self.valores += button
                    self.valor.setText(self.valor.text() + button)
        for d in dist:
            if(d == button):
                if(self.equal):
                    if(button == '%'):
                        self.valores += "/100"
                    self.valor.setText(self.valor.text()[
                        :-len(self.valor.text())])
                    self.equal = False
                    self.valor.setText(self.valor.text() + button)
                else:
                    self.valores += "/100"
                    self.valor.setText(self.valor.text() + button)

        # Si se pulsa 'AC' se establece el QLabel a vacio
        if(button == "AC"):
            self.valor.setText("")
            self.valores = ''
            self.equal = False
        # verificar si se ha introducido paréntesis antes
        elif(button == "()"):
            if(self.equal):
                self.valor.setText(
                    self.valor.text()[:-len(self.valor.text())])
                self.valores = self.valores[:-len(self.valores)]
                self.equal = False
            if not self.ver:
                self.ver = True
                self.valores += "("
                self.valor.setText(self.valor.text() + "(")

            elif(self.ver):
                self.ver = False
                self.valores += ")"
                self.valor.setText(self.valor.text() + ")")
        # verificar si el boton apretado es '=' , si es asi devolver el calculo
        elif(button == "="):
            val = ""
            self.equal = True
            if '%' in self.valor.text():
                val = str(eval('{}'.format(self.valores)))
            else:
                val = str(eval('{}'.format(self.valor.text())))
            self.valor.setText(val)
        # verificar si el boton apretado es el retroceso '<=' y
        # borrar un espacio
        elif(button == "<="):
            self.valor.setText(self.valor.text()[:-1])


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
