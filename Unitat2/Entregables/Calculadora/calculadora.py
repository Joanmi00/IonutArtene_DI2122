from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout,
    QGridLayout

)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #titulo de la ventana
        self.setWindowTitle("Calculadora")
        # numero de columnas que tendra la calculadora
        num_col = 4
        # tamaño de la calculadora
        dim = QSize(400, 400)

        # Creamos un QVBoxLayout para añadir el QLabel y el QGridLayout
        layout = QVBoxLayout()
        # Añadimos un Qlabel para mostrar los datos introducidos
        # e resultado
        self.valor = QLabel()
        # Le indicamos al QLabel que queremos el texto alineado
        # a la derecha(Qt.AlignRight) y centrado (Qt.AlignVCenter)
        self.valor.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # Le ponemos al QLabel un borde
        self.valor.setStyleSheet("border: 1px solid black;")

        self.bot = {}
        # Variables que estan inicializadas a False
        # Esta variable es para verificar si se ha introducido ya un paréntesis
        self.ver = False
        # Esta variable es para verificar si se ha pulsado el igual
        self.equal = False
        # lista con el texto de los botones en el orden deseado
        button_list = [
            'AC', '()', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '+',
            '1', '2', '3', '-',
            '0', '.', '<=', '=']
        # Creamos un QGridLayout para añadir los botones
        button_layout = QGridLayout()

        # recorremos la lista y vamos añadiendo los botones a QGridLayout
        for element in button_list:

            self.bot[element] = QPushButton(element)

            button_layout.addWidget(self.bot[element],
                                    button_list.index(element) // num_col,
                                    button_list.index(element) % num_col

                                    )

            # si un boton es pulsado llama a la funcion mod_label
            self.bot[element].clicked.connect(self.mod_label)

        layout.addWidget(self.valor)
        layout.addLayout(button_layout)
        # Creamos un widget para añadir el layout que contiene
        # el QLabel y el QGridLayout
        widget = QWidget()
        widget.setLayout(layout)
        self.resize(dim)
        self.setCentralWidget(widget)

    def mod_label(self):
        """[Esta funciona es llamada cuando se hace clic en un boton
            y a su vez llama a otra funciona que verifica que el valor
            introducido es corecto pasandole el valor del boton]

        """
        button = self.sender().text()
        self.verifica_valor(button)

    def verifica_valor(self, button):
        """[Esta funcion es llamada para comprobar los valores que recibe
        existen haciendo las comprobaciones pertinentes ]


        Args:
            button ([String]): [texto del boton]
        """
        operacion = ['+', '*', '-', '/']
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        dist = ['.', '%']

        # verificar si se a introducido una operacion
        if button in operacion:

            if(self.equal):

                self.equal = False
                self.a_text(self.valor.text() + button)
            if not bool(self.valor.text()):
                self.a_text(self.valor.text())

            else:
                self.a_text(self.valor.text() + button)

        # verificar si se ha introducido un numero
        if button in numeros:
            if(self.equal):
                self.a_text(self.valor.text()[
                    :-len(self.valor.text())])
                self.equal = False

                self.a_text(self.valor.text() + button)

            else:

                self.a_text(self.valor.text() + button)

        # verificar si se ha introducido otros signos
        if button in dist:
            if(self.equal):

                self.a_text(self.valor.text()[
                    :-len(self.valor.text())])
                self.equal = False
                self.a_text(self.valor.text() + button)
            else:
                self.a_text(self.valor.text() + button)

        # Si se pulsa 'AC' se establece el QLabel a vacio
        if(button == "AC"):
            self.a_text("")
            self.equal = False

        # verificar si se ha introducido paréntesis antes
        elif(button == "()"):
            # verifica si lo que hay en el QLabel es un resultado
            # de una operacion
            if(self.equal):
                self.a_text(self.valor.text()[:-len(self.valor.text())])
                self.equal = False
            # Los 2 if siguientes son para verificar si sa introducido
            # antes un paréntesis o no y actua en consecuencia
            if not self.ver:
                self.ver = True
                self.a_text(self.valor.text() + "(")

            elif(self.ver):
                self.ver = False

                self.a_text(self.valor.text() + ")")

        # verificar si el boton apretado es '=' , si es asi devolver el calculo
        elif(button == "="):
            # Comprueba que el QLabel no esta vacio
            # y si no lo esta seguira ejecutando
            if bool(self.valor.text()):
                self.equal = True
                self.r_text(self.valor.text())
        # verificar si el boton apretado es el retroceso '<=' y
        # borra un espacio
        elif(button == "<="):
            # Comprueba que el QLabel no este vacio para poder borrar
            if bool(self.valor.text()):
                self.b1_text()

    def a_text(self, text):
        """[Actualiza el QLabel con los datos que le pasan]


        Args:
            text ([String]): [es el texto que le pasan]
        """
        self.valor.setText(text)

    def b_text(self):
        """
        [Borra el texto que contiene el QLabels]

        """
        self.a_text("")
        self.guardados = ""

    def r_text(self, operacion):
        """[ Recibe un string que contiene la operacionç
        con la cual hacer los calculos]

        Args:
            operacion ([String]): [operacion]
        """
        self.a_text(str(eval(operacion.replace("%", "/100"))))

    def b1_text(self):
        """[Borra un espacio del QLabel]
        """
        self.a_text((self.valor.text()[:-1]))


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
