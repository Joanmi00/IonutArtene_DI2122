import sys
import math
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QPushButton, QSizePolicy, QWidget,
    QLabel, QVBoxLayout, QGridLayout
)
from PySide6.QtGui import QAction, QFont, QKeySequence, QPixmap
import ventana_atajos
import dialogo_eleccion as dialogo


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.sin = QPixmap(os.path.join(os.path.dirname(
            __file__), "resources/sin_guardado.png"))

        self.con = QPixmap(os.path.join(os.path.dirname(
            __file__), "resources/con_guardado.png"))
        # Titulo de la ventana
        self.setWindowTitle("Calculadora")
        # tamaño de la ventana
        self.setFixedSize(QSize(500, 450))
        # numero de columnas que tendra la calculadora
        self.num_col = 4
        # ubicacion del archivo al cual vamos a escribir las operaciones
        self.ubicacion_archivo = ""
        # Variables que estan inicializadas a False
        # Esta variable es para verificar si se ha introducido
        # ya un paréntesis
        self.ver = False
        # Esta variable es para verificar si se ha pulsado
        # con anterioridad el igual
        self.equal = False
        # variable de si esta activa o no la calc. cientifica
        self.cient = False
        # variable en caso de ser True guardara las operaciones en un txt
        self.guardar = False
        layout = QVBoxLayout()
        # Añadimos un Qlabel para mostrar los datos introducidos
        self.valor = QLabel()
        # tamaño de la aletra dentro del QLabel
        self.valor.setFont(QFont('Arial', 20))
        # altura maxima que puede tener el QLabel
        self.valor.setMaximumHeight(40)
        # variable que contendra el modo que esta activo cientifica o normal
        self.mode = QLabel()
        self.icono = QLabel()

        # Le indicamos al QLabel que queremos el texto alineado
        # a la derecha(Qt.AlignRight) y centrado (Qt.AlignVCenter)
        self.valor.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.valor.setAutoFillBackground(True)

        # listas con el texto de los botones
        self.button_cient = ['AC', 'π', '^', '!',
                             '()', '%', '/', '<=',
                             '7', '8', '9', '*',
                             '4', '5', '6', '+',
                             '1', '2', '3', '-',
                             '0', '.', '=']

        self.button_normal = ['AC', '()', '%', '/',
                              '7', '8', '9', '*',
                              '4', '5', '6', '+',
                              '1', '2', '3', '-',
                              '0', '.', '<=', '=']
        # definimos un QGridLayout vacio
        self.button_layout = QGridLayout()
        # cargamos la calculadora normal en el QGridLayout
        self.calc_normal()
        # Cargamos el menu
        self.menu()
        # añadimos al QVBoxLayout un widget y el QGridLayout con los botones
        layout.addWidget(self.valor)
        layout.addLayout(self.button_layout)
        # definimos un QWidget y le ponemos el QVBoxLayout
        widget = QWidget()
        widget.setLayout(layout)
        # definimos a QWidget como widget central
        self.setCentralWidget(widget)

    def calc_cientifica(self):
        """[summary]
        Funcion que se encarga de llamar a la
        funcion que se encarga de la limpieza del QGridLayout
         y una vez limpio volver a dibujar todos los botones
         con los valores nuevos
        """
        self.mode.setText("Cientifica")
        # modificamos el color del texto a rojo y le ponemos un borde al
        # QLabel de color rojo
        self.valor.setStyleSheet(
            "border: 1px solid red ;color : red;")
        # en caso de que sea falso limpia los botones
        if not self.cient:
            self.limpia()
        # por cada elemento de lista añade un boton
        for element in self.button_cient:

            button = QPushButton(element)
            button.setFixedSize(80, 40)
            button.setFont(QFont('Arial', 15))
            button.setStyleSheet(
                'QPushButton {background-color: #a6adb3; color: red;}')
            self.button_layout.columnStretch(30)
            if(element == "="):
                button.setSizePolicy(
                    QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
                button.setFixedSize(QSize(200, 40))
                self.button_layout.addWidget(button,
                                             self.button_cient.index(
                                                 element) // self.num_col,
                                             self.button_cient.index(
                                                 element) % self.num_col,
                                             1,
                                             2,
                                             Qt.AlignLeft | Qt.AlignCenter
                                             )

            else:
                self.button_layout.addWidget(button,
                                             self.button_cient.index(
                                                 element) // self.num_col,
                                             self.button_cient.index(
                                                 element) % self.num_col
                                             )

            if(element == '<='):
                button.setShortcut(QKeySequence('Backspace'))
                button.setStatusTip("Backspace")
            elif(element == 'π'):
                button.setShortcut(QKeySequence('Ctrl+n'))
                button.setStatusTip('Ctrl+n')
            elif(element == '()'):
                button.setShortcut(QKeySequence('('))
                button.setStatusTip('Shift+8')
            elif(element == 'AC'):
                button.setShortcut(QKeySequence('Ctrl+Backspace'))
                button.setStatusTip('Ctrl+Backspace')
            else:
                button.setShortcut(QKeySequence(element))
                button.setStatusTip(f'{element}')
            # ponemos la variable a True ya que estamos en la cientifica
            self.cient = True
            # si un boton es pulsado llama a la funcion button_clicked
            button.clicked.connect(self.button_clicked)

    def calc_normal(self):
        """[summary]
        Funcion que se encarga de llamar a la
        funcion que se encarga de la limpieza del QGridLayout
         y una vez limpio volver a dibujar todos los botones
         con los valores nuevos

        """

        self.mode.setText("Normal")
        # modificamos el color del texto a azul y le ponemos un borde al
        # QLabel de color azul
        self.valor.setStyleSheet(
            "border: 1px solid blue ;color : blue;")
        # en caso de que sea verdadero limpia los botones
        if self.cient:
            self.limpia()
        # por cada elemento de lista añade un boton
        for element in self.button_normal:

            button = QPushButton(element)
            button.setFont(QFont('Arial', 15))
            button.setFixedSize(100, 40)
            button.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: blue;}')

            self.button_layout.addWidget(button,
                                         self.button_normal.index(
                                             element) // self.num_col,
                                         self.button_normal.index(
                                             element) % self.num_col


                                         )
            # añadimos los shorcut y el statusTip de los botones
            if(element == '<='):
                button.setShortcut(QKeySequence('Backspace'))
                button.setStatusTip("Backspace")
            elif(element == 'π'):
                button.setShortcut(QKeySequence('Ctrl+n'))
                button.setStatusTip('Ctrl+n')
            elif(element == '()'):
                button.setShortcut(QKeySequence('('))
                button.setStatusTip('(')
            elif(element == 'AC'):
                button.setShortcut(QKeySequence('Ctrl+Backspace'))
                button.setStatusTip('Ctrl+Backspace')
            else:
                button.setShortcut(QKeySequence(element))
                button.setStatusTip(f'{element}')
            # ponemos la variable a False ya que estamos en la normal
            self.cient = False
            # si un boton es pulsado llama a la funcion button_clicked
            button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        """[summary]
        Esta funciona es llamada cuando se hace clic en un boton
           recoge el texto del boton pulsado y lo manda a verificar
        """
        button = self.sender().text()
        self.verifica_valor(button)

    def menu(self):
        """[summary]
            Funcion que se encarga de crear el menu y de su funcionamiento
        """
        # Creamos los QAction para el menu
        cienti = QAction('&Cientifica', self)
        cienti.triggered.connect(self.calc_cientifica)
        cienti.setStatusTip("Cientifica")
        normal = QAction('&Normal', self)
        normal.triggered.connect(self.calc_normal)
        normal.setStatusTip("Normal")

        self.txt = QAction("Guardar en txt", self)
        self.txt.setCheckable(True)
        self.txt.triggered.connect(self.guarda)

        ventana = QAction('&Atajos', self)
        ventana.triggered.connect(self.ventana_atajos)
        ventana.setStatusTip("Atajos")

        salir = QAction('Salir', self)
        salir.triggered.connect(self.close)
        salir.setStatusTip("Salir")

        # Creamos un status bar vacio
        status = self.statusBar()
        if not self.guardar:
            self.icono.resize(self.sin.width(),
                              self.sin.height())
            self.icono.setPixmap(self.sin)

        status.addPermanentWidget(self.mode)
        status.addPermanentWidget(self.icono)

        # creamos un menu vacio
        menu = self.menuBar()
        # añadimos pestañas al menu
        file_menu = menu.addMenu("&File")
        file_mode = file_menu.addMenu("&Mode")
        file_mode.addAction(cienti)
        file_mode.addAction(normal)
        file_txt = file_menu.addMenu("&Operaciones txt")
        file_txt.addAction(self.txt)
        file_menu.addAction(salir)
        menu.addSeparator()
        shorcut_buttons = menu.addMenu("&Ayuda")
        shorcut_buttons.addAction(ventana)

    def ventana_atajos(self):
        """[summary]
            Cuando se seleccione la opcion del menu para ayuda/atajos
            imprimira aparecera un ventana con todos los atajos de cada boton
        """
        w = ventana_atajos.MyPopup(self)
        w.exec()

    def closeEvent(self, event):
        """[summary]
        Cuando se ejecute cualquier tipo de cierre de la ventana principal
        esta preguntara si estamos seguro de que si quiremos cerrar


        Args:
            event ([Event]): [Recibe el evento de cerrar]
        """
        salida = dialogo.dialogo_eleccion(self)
        if not salida.exec():
            event.ignore()

    def limpia(self):
        """[summary]
            Funcion que se ocupa de limpiar el QGridLayout
        """
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
            # Comprueba que el QLabel no este vacio
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

                if(self.guardar):
                    with open(self.ubicacion_archivo, 'a') as f:
                        f.write(f'{operacion} = {val} \n')
        # verificar si el boton apretado es el retroceso '<=' y
        # borra un espacio
        elif(button == "<="):
            # Comprueba que el QLabel no este vacio para poder borrar
            if bool(self.valor.text()):
                self.valor.setText(self.valor.text()[:-1])

    def guarda(self, s):
        """[summary]
        Funcion que se encarga que en cuanto hagamos click en la opcion del
        menu para guardar el texto guardar en una variable True or False y
        para que aparezca una ventana para elegir el archivo donde queremos
        guardar las operaciones y sus resultados

        Args:
            s ([bool]): [Es True or False segun si esta checkeado o no la
            opcion del menu]
        """
        # Abrimos el Selector de Archivos
        if not self.guardar:
            fname, _ = QFileDialog.getOpenFileName(
                self, "Elegir un fichero", "", "All Files(*);;Texto(*.txt)")
            # guardamos el valor de fname si no esta     vacio
            if fname:
                self.ubicacion_archivo = fname
                self.guardar = True
            else:
                self.guardar = False
                self.txt.setChecked(False)
        if(self.txt.isChecked):
            self.guardar = s
        if not self.guardar:
            self.icono.resize(self.sin.width(),
                              self.sin.height())
            self.icono.setPixmap(self.sin)
        else:
            self.icono.resize(self.con.width(),
                              self.con.height())
            self.icono.setPixmap(self.con)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
