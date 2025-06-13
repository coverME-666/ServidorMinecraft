import os
import shutil
from PyQt5 import QtWidgets, QtCore

class GestionMundosWidget(QtWidgets.QGroupBox):
    mundo_seleccionado = QtCore.pyqtSignal(str)
    iniciar_servidor = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__("Gestión de Mundos", parent)
        self.setObjectName("gestionGroup")
        layout = QtWidgets.QGridLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)

        self.mundos_cb = QtWidgets.QComboBox()
        self.mundos_cb.setMaximumWidth(180)
        layout.addWidget(self.mundos_cb, 0, 0, 1, 1)

        self.seleccionar_btn = QtWidgets.QPushButton("Seleccionar Mundo")
        self.seleccionar_btn.setMaximumWidth(180)
        layout.addWidget(self.seleccionar_btn, 0, 1, 1, 1)

        self.eliminar_btn = QtWidgets.QPushButton("Eliminar Mundo")
        self.eliminar_btn.setMaximumWidth(180)
        layout.addWidget(self.eliminar_btn, 1, 0, 1, 1)

        self.iniciar_btn = QtWidgets.QPushButton("Iniciar Servidor")
        self.iniciar_btn.setMaximumWidth(180)
        layout.addWidget(self.iniciar_btn, 1, 1, 1, 1)

        self.cargar_mundos()

        self.seleccionar_btn.clicked.connect(self.seleccionar_mundo)
        self.eliminar_btn.clicked.connect(self.eliminar_mundo)
        self.iniciar_btn.clicked.connect(self.iniciar_servidor_clicked)

    def cargar_mundos(self):
        worlds_dir = "worlds"
        if not os.path.exists(worlds_dir):
            os.makedirs(worlds_dir)
        mundos = [d for d in os.listdir(worlds_dir) if os.path.isdir(os.path.join(worlds_dir, d))]
        self.mundos_cb.clear()
        self.mundos_cb.addItems(mundos)

    def seleccionar_mundo(self):
        mundo = self.mundos_cb.currentText()
        if mundo:
            QtWidgets.QMessageBox.information(self, "Mundo seleccionado", f"Has seleccionado el mundo '{mundo}'.")
            self.mundo_seleccionado.emit(mundo)

    def eliminar_mundo(self):
        mundo = self.mundos_cb.currentText()
        if not mundo:
            return
        reply = QtWidgets.QMessageBox.question(
            self, "Eliminar mundo",
            f"¿Seguro que deseas eliminar el mundo '{mundo}'?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            shutil.rmtree(os.path.join("worlds", mundo))
            self.cargar_mundos()
            QtWidgets.QMessageBox.information(self, "Eliminado", f"Mundo '{mundo}' eliminado.")

    def iniciar_servidor_clicked(self):
        mundo = self.mundos_cb.currentText()
        if mundo:
            self.iniciar_servidor.emit(mundo)