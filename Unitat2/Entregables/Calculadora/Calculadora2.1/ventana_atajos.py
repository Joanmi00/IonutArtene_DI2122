from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QVBoxLayout

# que herede de la main class


class MyPopup(QDialog):
    def __init__(self, parent=None):
        super(MyPopup, self).__init__(parent)

        button_shorcut = {
            ' 0': "0", ' 1': "1", ' 2': '2', ' 3': "3",
            ' 4': "4", ' 5': "5", ' 6': "6", ' 7': "7",
            ' 8': "8", ' 9': "9", ' +': "+", ' -': "-",
            ' .': ".", '<=': "Backspace", ' =': "=",
            ' *': "*", ' π': "Ctrl + n",
            ' ^': "^", ' !': "!",
            'AC': "Ctrl+Backspace",
            '()': "(", ' %': "%", ' /': "/",
        }
        self.layout_h = QHBoxLayout()
        layout_v1 = QVBoxLayout()
        layout_v2 = QVBoxLayout()

        for val, shorcut in button_shorcut.items():
            if(list(button_shorcut.keys()).index(val) <
               len(list(button_shorcut.keys()))/2):
                layout_v1.addWidget(
                    QLabel(val+" = > "+"\""+shorcut+"\""))
                layout_v1.addSpacing(2)
            else:
                layout_v2.addWidget(
                    QLabel(val+" = > "+"\""+shorcut+"\""))
                layout_v2.addSpacing(2)
        self.layout_h.addLayout(layout_v1)
        self.layout_h.addSpacing(20)
        self.layout_h.addLayout(layout_v2)
        self.setLayout(self.layout_h)
