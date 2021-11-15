import sys
import argparse
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindows(QMainWindow):
    def __init__(self, args, fixed=False):
        super().__init__()
        #Main window config
        size_x, size_y = args.size
        fixed=args.fixed_size
        self.setWindowTitle(args.title)
        self.setFixedSize(size_x, size_y)
        # self.button.setMaximumSize(100,25)
        # self.setMaximumSize(400,400)
        # self.setMinimumSize(200,200)

        #boton
        self.button = QPushButton(args.button_text, self)
        self.setCentralWidget(self.button)
        # self.button.show() - No hace falta ya que el boton pertenece a la ventana
        # y cuando haces el show de la ventana lo hace tambien del boton


def main():
    #argparse
    #title, boton, fixed, size_x, size_y = "", "", False, 300, 200
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--title", help="Elige el titulo de la aplicacion")
    parser.add_argument("-b", "--button-text", help="Elige el texto del boton")
    parser.add_argument("-f", "--fixed-size",
                        action="store_true", help="Window fixed size")
    parser.add_argument("-s", "--size", nargs=2, metavar=('size_x',
                        'size_y'), type=int, help="Size of windows")
    args = parser.parse_args()

    ''' if args.title:
        title = args.title
    if args.button_text:
        boton = args.button_text
    if args.fixed_size:
        fixed = args.fixed_size
    if args.size:
        size_x, size_y = args.size'''
        
    #Iniciate window
    app = QApplication()
    windows = MainWindows(args)
    windows.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
