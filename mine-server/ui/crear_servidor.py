from PyQt5 import QtWidgets
from core.downloader import descargar_jar

forge_versions = [
    "1.21.1", "1.20.1", "1.19.1", "1.18.1", "1.17.1",
    "1.16.2", "1.15.1", "1.14.2", "1.13.2", "1.12.1",
    "1.11.2", "1.10.2", "1.9.4", "1.8.8"
]
fabric_versions = [
    "1.21.1", "1.20.1", "1.19.1", "1.18.1",
    "1.17.1", "1.16.2", "1.15.1", "1.14.2"
]

class CrearServidorWidget(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Crear el servidor", parent)
        self.setObjectName("serverGroup")
        self.setFixedHeight(220)
        layout = QtWidgets.QFormLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)

        self.tipo_cb = QtWidgets.QComboBox()
        self.tipo_cb.addItems(["vanilla", "forge", "fabric"])
        self.tipo_cb.setObjectName("tipoCombo")
        self.tipo_cb.setMaximumWidth(180)
        self.tipo_cb.currentTextChanged.connect(self.actualizar_versiones)
        layout.addRow("Tipo de servidor:", self.tipo_cb)

        self.version_cb = QtWidgets.QComboBox()
        self.version_cb.setObjectName("versionCombo")
        self.version_cb.setMaximumWidth(180)
        layout.addRow("Versión:", self.version_cb)

        self.confirm_btn = QtWidgets.QPushButton("Confirmar")
        self.confirm_btn.setMaximumWidth(180)
        self.confirm_btn.clicked.connect(self.confirmar)
        layout.addRow(self.confirm_btn)

        self.actualizar_versiones(self.tipo_cb.currentText())

    def actualizar_versiones(self, tipo):
        self.version_cb.clear()
        if tipo in ["forge", "vanilla"]:
            self.version_cb.addItems(forge_versions)
        elif tipo == "fabric":
            self.version_cb.addItems(fabric_versions)

    def confirmar(self):
        tipo = self.tipo_cb.currentText()
        version = self.version_cb.currentText()
        if tipo not in ["vanilla", "forge", "fabric"] or not version:
            QtWidgets.QMessageBox.critical(self, "Error", "Selecciona tipo y versión")
            return
        try:
            descargar_jar(tipo, version, "servers/")
            QtWidgets.QMessageBox.information(self, "Éxito", "Descarga y configuración completadas.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error: {e}")