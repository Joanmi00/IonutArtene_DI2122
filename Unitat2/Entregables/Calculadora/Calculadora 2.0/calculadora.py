import sys
import math
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget,
    QLabel, QVBoxLayout, QGridLayout
)
from PySide6.QtGui import QAction, QKeySequence
from ventana_atajos import MyPopup


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Calculadora")
        self.setFixedSize(QSize(500, 450))
        # numero de columnas que tendra la calculadora
        self.num_col = 4
        self.cient = False
        self.guadar = False
        layout = QVBoxLayout()
        # Añadimos un Qlabel para monstrar los datos introducidos
        self.valor = QLabel()
        self.valor.setMinimumHeight(40)

        # Le indicamos al QLabel que queremos el texto alineado
        # a la derecha(Qt.AlignRight) y centrado (Qt.AlignVCenter)
        self.valor.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.valor.setAutoFillBackground(True)

        # Variables que estan inicializadas a False
        # Esta variable es para verificar si se ha introducido ya un paréntesis
        self.ver = False
        # Esta variable es para verificar si se ha pulsado el igual
        self.equal = False
        # listas con el texto de los botones
        self.button_list = ['AC', 'π', '^', '!',
                            '()', '%', '/', '<=',
                            '7', '8', '9', '*',
                            '4', '5', '6', '+',
                            '1', '2', '3', '-',
                            '0', '.', '=']

        self.button_list2 = ['AC', '()', '%', '/',
                             '7', '8', '9', '*',
                             '4', '5', '6', '+',
                             '1', '2', '3', '-',
                             '0', '.', '<=', '=']

        self.button_layout = QGridLayout()

        self.calc_normal()
        self.menu()

        layout.addWidget(self.valor)
        layout.addLayout(self.button_layout)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def calc_cientifica(self):
        """[Funcion que se encarga de llamar a la 
        funcion que se encarga de la limpieza del QGridLayout
         y una vez limpio volver a dibujar todos los botones 
         con los valores nuevos]
        """
        self.valor.setStyleSheet(
            "border: 1px solid red ;color : red;")

        if not self.cient:
            self.limpia()

        for element in self.button_list:

            button = QPushButton(element)
            button.setFixedSize(80, 40)
            button.setStyleSheet(
                'QPushButton {background-color: #a6adb3; color: red;}')

            if(element == "="):
                button.setFixedSize(210, 40)

                self.button_layout.addWidget(button,
                                             self.button_list.index(
                                                 element) // self.num_col,
                                             self.button_list.index(
                                                 element) % self.num_col,
                                             1,
                                             2,
                                             Qt.AlignLeft | Qt.AlignCenter
                                             )

            else:
                self.button_layout.addWidget(button,
                                             self.button_list.index(
                                                 element) // self.num_col,
                                             self.button_list.index(
                                                 element) % self.num_col
                                             )

            if(element == '='):
                button.setShortcut(QKeySequence('Shift+0'))
            elif(element == '%'):
                button.setShortcut(QKeySequence('Shift+5'))
            elif(element == '!'):
                button.setShortcut(QKeySequence('Shift+1'))
                button.setEnabled(False)
            elif(element == '*'):
                button.setShortcut(QKeySequence('Shift++'))
            elif(element == '/'):
                button.setShortcut(QKeySequence('Shift+7'))
            elif(element == '<='):
                button.setShortcut(QKeySequence('Backspace'))
            elif(element == '^'):
                button.setShortcut(QKeySequence('Shift+`'))
            elif(element == 'π'):
                button.setShortcut(QKeySequence('Ctrl+n'))
            elif(element == '()'):
                button.setShortcut(QKeySequence('Shift+8'))
            elif(element == 'AC'):
                button.setShortcut(QKeySequence('Ctrl+Backspace'))
            else:
                button.setShortcut(QKeySequence(element))

            self.cient = True
            # si un boton es pulsado llama a una funcion
            button.clicked.connect(self.button_clicked)

    def calc_normal(self):
        self.valor.setStyleSheet(
            "border: 1px solid blue ;color : blue;")
        if self.cient:
            self.limpia()

        for element in self.button_list2:

            button = QPushButton(element)
            button.setFixedSize(100, 40)
            button.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: blue;}')

            self.button_layout.addWidget(button,
                                         self.button_list2.index(
                                             element) // self.num_col,
                                         self.button_list2.index(
                                             element) % self.num_col


                                         )
            if(element == '='):
                button.setShortcut(QKeySequence('Shift+0'))
            elif(element == '%'):
                button.setShortcut(QKeySequence('Shift+5'))
            elif(element == '*'):
                button.setShortcut(QKeySequence('Shift++'))
            elif(element == '/'):
                button.setShortcut(QKeySequence('Shift+7'))
            elif(element == '<='):
                button.setShortcut(QKeySequence('Backspace'))
            elif(element == '()'):
                button.setShortcut(QKeySequence('Shift+8'))
            elif(element == 'AC'):
                button.setShortcut(QKeySequence('Ctrl+Backspace'))
            else:
                button.setShortcut(QKeySequence(element))

            self.cient = False
            # si un boton es pulsado llama a una funcion
            button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        """[summary]
        Esta funciona es llamada cuando se hace clic en un boton
           recoge el texto del boton pulsado y lo manda a verificar
        """
        button = self.sender().text()
        self.verifica_valor(button)

    def menu(self):
        cienti = QAction('&Cientifica', self)
        cienti.triggered.connect(self.calc_cientifica)
        normal = QAction('&Normal', self)
        normal.triggered.connect(self.calc_normal)
        txt = QAction("Guardar en txt", self)
        txt.setCheckable(True)
        txt.triggered.connect(self.guarda)
        ventana = QAction('&Atajos', self)
        ventana.triggered.connect(self.ventana_atajos)
        salir = QAction('Salir', self)
        salir.triggered.connect(self.close)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_mode = file_menu.addMenu("&Mode")
        file_mode.addAction(cienti)
        file_mode.addAction(normal)
        file_txt = file_menu.addMenu("&Operaciones txt")
        file_txt.addAction(txt)
        file_menu.addAction(salir)
        menu.addSeparator()
        shorcut_buttons = menu.addMenu("&Ayuda")
        shorcut_buttons.addAction(ventana)

    # abre la ventana con los atajos de los botones
    def ventana_atajos(self):
        self.w = MyPopup()
        self.w.show()

    # limpia el QGridLayout
    def limpia(self):
        for i in reversed(range(self.button_layout.count())):
            widgetToRemove = self.button_layout.itemAt(i).widget()
            self.button_layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

    def verifica_valor(self, button):
        """[summary]
        Esta funcion es llamada para comprobar los valores que recibe
        son existen haciendo las comprobaciones pertinentes y segun
        la tecla pulsada hace un tipo de comprobacion u otro

        Args:
            button (String): [Es el texto que tiene el boton que ha sido
                                pulsado]
        """
        operacion = ['+', '*', '-', '/', ]
        numeros = ['0', '1', '2', '2', '3', '4', '5', '6', '7', '8', '9']
        dist = ['.', '%', 'π', '^', '!']

        # verificar si se a introducido una operacion
        if button in operacion:

            if(self.equal):

                self.equal = False
                self.valor.setText(self.valor.text() + button)
            if not bool(self.valor.text()):
                self.valor.setText(self.valor.text())

            else:
                self.valor.setText(self.valor.text() + button)

        # verificar si se ha introducido un numero
        if button in numeros:
            if(self.equal):
                self.valor.setText(self.valor.text()[
                    :-len(self.valor.text())])
                self.equal = False

                self.valor.setText(self.valor.text() + button)
            else:

                self.valor.setText(self.valor.text() + button)
        # verificar si se ha introducido otros signos
        if button in dist:
            if(self.equal):

                self.valor.setText(self.valor.text()[
                    :-len(self.valor.text())])
                self.equal = False
                self.valor.setText(self.valor.text() + button)
            else:
                self.valor.setText(self.valor.text() + button)

        # Si se pulsa 'AC' se establece el QLabel a vacio
        if(button == "AC"):
            self.valor.setText("")
            self.equal = False

        # verificar si se ha introducido paréntesis antes
        elif(button == "()"):
            # verifica si lo que hay en el QLabel es un resultado
            # de una operacion
            if(self.equal):
                self.valor.setText(
                    self.valor.text()[:-len(self.valor.text())])
                self.equal = False
            # Los 2 if siguientes son para verificar si sa introducido
            # antes un paréntesis o no y actua en consecuencia
            if not self.ver:
                self.ver = True
                self.valor.setText(self.valor.text() + "(")

            elif(self.ver):
                self.ver = False

                self.valor.setText(self.valor.text() + ")")

        # verificar si el boton apretado es '=' , si es asi devolver el calculo
        elif(button == "="):
            # Comprueba que el QLabel no esta vacio
            # y si no lo esta seguira ejecutando
            if bool(self.valor.text()):
                val = ""
                self.equal = True
                operacion = self.valor.text()
                val = str(eval('{}'.format(self.valor.text()
                                           .replace("%", "/100")
                                           .replace("^", "**")
                                           .replace("π", str(math.pi)))))
                self.valor.setText(val)
                if(self.guadar):
                    with open(os.path.join(os.path.dirname(__file__),
                                           "operaciones"), 'a') as f:
                        f.write(f'{operacion} = {val} \n')
        # verificar si el boton apretado es el retroceso '<=' y
        # borra un espacio
        elif(button == "<="):
            # Comprueba que el QLabel no este vacio para poder borrar
            if bool(self.valor.text()):
                self.valor.setText(self.valor.text()[:-1])

    def guarda(self, s):
        """[Funcion que se encarga que en cuanto hagamos click en la opcion del menu
        para guardar el texto guardar en una variable True or False]

        Args:
            s ([bool]): [Es True or False segun si esta checkeado o no la
            opcion del menu]
        """
        self.guadar = s


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
