from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


class dialogo_eleccion(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Elige una opcion")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Estas seguro que quieres cerrar ?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
