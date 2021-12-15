from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget


class MyPopup(QWidget):
    def __init__(self):
        super(MyPopup, self).__init__()

        button_shorcut = {
            '0': "0", '1': "1", '2': "2", '3': "3",
            '4': "4", '5': "5", '6': "6", '7': "7",
            '8': "8", '9': "9", '+': "+", '-': "-",
            '.': ".", '<=': "Backspace", '=': "Shift + 0",
            '*': "Shift + +", 'π': "Ctrl + n",
            '^': "Shift + `", '!': "Shift + 1",
            'AC': "Ctrl+Backspace",
            '()': "Shift + 8", '%': "Shift + 5", '/': "Alt + º",
        }
        layout_h = QHBoxLayout()
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
        layout_h.addLayout(layout_v1)
        layout_h.addSpacing(20)
        layout_h.addLayout(layout_v2)
        self.setLayout(layout_h)
