from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import subprocess


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

        self.setWindowTitle("Exemple signals-slots 1")
        #self.setFixedSize(QSize(self.size_w, self.size_h))
        self.resize(self.size_w, self.size_h)
        self.center()

        self.pybutton = QPushButton('Minimitzar', self)
        self.pybutton1 = QPushButton('Normalitza', self)
        self.pybutton2 = QPushButton('Maximitzar', self)

        # Connectem la senyal clicked a la ranura button_pressed
        self.pybutton.clicked.connect(self.minimitzar)
        self.pybutton1.clicked.connect(self.normalitza)
        self.pybutton2.clicked.connect(self.maximitzar)

        self.pybutton.resize(self.sizew_b, self.sizeh_b)
        self.pybutton1.resize(self.sizew_b, self.sizeh_b)
        self.pybutton2.resize(self.sizew_b, self.sizeh_b)

        self.pybutton.move(self.pos, (self.size_h-self.sizeh_b) / 2)
        self.pybutton1.move(self.pos+(self.sizew_b+self.pos),
                            (self.size_h-self.sizeh_b) / 2)
        self.pybutton2.move(self.pos+(self.sizew_b*2+self.pos*2),
                            (self.size_h-self.sizeh_b) / 2)

    def maximitzar(self):
        self.pybutton.setEnabled(True)
        self.pybutton1.setEnabled(True)
        self.size_w = 900
        self.size_h = 900
        self.cal_pos()
        self.pybutton.move(self.pos, (self.size_h-self.sizeh_b) / 2)
        self.pybutton1.move(self.pos+(self.sizew_b+self.pos),
                            (self.size_h-self.sizeh_b) / 2)
        self.pybutton2.move(self.pos+(self.sizew_b*2+self.pos*2),
                            (self.size_h-self.sizeh_b) / 2)
        self.resize(self.size_w, self.size_h)
        
        self.pybutton2.setEnabled(False)

    def minimitzar(self):
        self.pybutton1.setEnabled(True)
        self.pybutton2.setEnabled(True)

        self.resize(self.sizew_b*3, self.sizeh_b)
        self.pybutton.move(0, 0)
        self.pybutton1.move(0+self.sizew_b, 0)
        self.pybutton2.move(0+(self.sizew_b*2), 0)
        self.pybutton.setEnabled(False)

    def normalitza(self):
        self.pybutton.setEnabled(True)
        self.pybutton2.setEnabled(True)
        self.size_w = 600
        self.size_h = 600
        self.cal_pos()
        self.pybutton.move(self.pos, (self.size_h-self.sizeh_b) / 2)
        self.pybutton1.move(self.pos+(self.sizew_b+self.pos),
                            (self.size_h-self.sizeh_b) / 2)
        self.pybutton2.move(self.pos+(self.sizew_b*2+self.pos*2),
                            (self.size_h-self.sizeh_b) / 2)
        self.resize(self.size_w, self.size_h)

        self.pybutton1.setEnabled(False)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def cal_pos(self):
       self.pos = (((self.size_w/self.sizew_b)-self.numb)
                    * self.sizew_b)/(self.numb+1)


if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()

    mainWin.show()
    app.exec()
