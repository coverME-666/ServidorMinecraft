from PyQt5 import QtWidgets

class ConsolaWidget(QtWidgets.QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setObjectName("terminalBox")

    def append_message(self, mensaje):
        self.append(mensaje)
