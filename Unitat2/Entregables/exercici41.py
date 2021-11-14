from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.size_w = 600
        self.size_h = 600
        self.sizew_b = 150
        self.sizeh_b = 100
        self.numb = 3
        self.pos = (((self.size_w/self.sizew_b)-self.numb)
                    * self.sizew_b)/(self.numb+1)

        self.setWindowTitle("Exercici4")
        #self.setFixedSize(QSize(self.size_w, self.size_h))

        

        self.pybutton_min = QPushButton('Minimitzar', self)
        self.pybutton_nor = QPushButton('Normalitza', self)
        self.pybutton_max = QPushButton('Maximitzar', self)

        # Connectem la senyal clicked a la ranura button_pressed
        self.pybutton_min.clicked.connect(self.minimitzar)
        self.pybutton_nor.clicked.connect(self.normalitza)
        self.pybutton_max.clicked.connect(self.maximitzar)

        self.pybutton_min.resize(self.sizew_b, self.sizeh_b)
        self.pybutton_nor.resize(self.sizew_b, self.sizeh_b)
        self.pybutton_max.resize(self.sizew_b, self.sizeh_b)

        self.cambia_p_b()
        self.pybutton_nor.setEnabled(False)

    def maximitzar(self):
        '''Cambia de tamaño la ventana actual y actualiza la
            variable pos segun ventana y dibuja los botones'''
        self.pybutton_min.setEnabled(True)
        self.pybutton_nor.setEnabled(True)
        self.size_w = 900
        self.size_h = 900
        self.cambia_p_b()
        self.pybutton_max.setEnabled(False)

    def minimitzar(self):
        '''Cambia de tamaño la ventana actual y actualiza la
            variable pos segun ventana y dibuja los botones'''
        self.pybutton_nor.setEnabled(True)
        self.pybutton_max.setEnabled(True)
        self.size_w = self.sizew_b*3
        self.size_h = self.sizeh_b

        self.cambia_p_b()
        self.pybutton_min.setEnabled(False)

    def normalitza(self):
        '''Cambia de tamaño la ventana actual y actualiza la
            variable pos segun ventana y dibuja los botones'''
        self.pybutton_min.setEnabled(True)
        self.pybutton_max.setEnabled(True)
        self.size_w = 600
        self.size_h = 600
        self.cambia_p_b()
        self.pybutton_nor.setEnabled(False)

    def center(self):
        '''Centra la ventana en la pantalla'''
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def cal_pos(self):
        '''Actualiza pos segun los nuevos datos de ventana'''
        self.pos = (((self.size_w/self.sizew_b)-self.numb)
                    * self.sizew_b)/(self.numb+1)

    def cambia_p_b(self):
        '''actualiza la variable pos segun tamaño ventana,mueve los botones
        segun la variable pos,y cambia de tamaño la ventana'''
        self.cal_pos()
        self.pybutton_min.move(self.pos, (self.size_h-self.sizeh_b) / 2)
        self.pybutton_nor.move(self.pos+(self.sizew_b+self.pos),
                               (self.size_h-self.sizeh_b) / 2)
        self.pybutton_max.move(self.pos+(self.sizew_b*2+self.pos*2),
                               (self.size_h-self.sizeh_b) / 2)
        self.resize(self.size_w, self.size_h)


if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    mainWin.center()
    app.exec()
