from PyQt5 import QtWidgets

class ConfiguracionMundoWidget(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Configuración del Mundo", parent)
        self.setObjectName("worldGroup")
        layout = QtWidgets.QFormLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)

        self.nombre_le = QtWidgets.QLineEdit()
        self.nombre_le.setMaximumWidth(180)
        layout.addRow("Nombre del Mundo:", self.nombre_le)

        self.modo_cb = QtWidgets.QComboBox()
        self.modo_cb.addItems(["supervivencia", "creativo", "aventura", "espectador"])
        self.modo_cb.setMaximumWidth(180)
        layout.addRow("Modo de Juego:", self.modo_cb)

        self.dificultad_cb = QtWidgets.QComboBox()
        self.dificultad_cb.addItems(["pacífica", "fácil", "normal", "difícil"])
        self.dificultad_cb.setMaximumWidth(180)
        layout.addRow("Dificultad:", self.dificultad_cb)

        self.tipo_mundo_cb = QtWidgets.QComboBox()
        self.tipo_mundo_cb.addItems([
            "predeterminado", "superplano", "amplificado",
            "bioma único", "grandes biomas", "personalizado"
        ])
        self.tipo_mundo_cb.setMaximumWidth(180)
        layout.addRow("Tipo de Mundo:", self.tipo_mundo_cb)

        self.semilla_le = QtWidgets.QLineEdit()
        self.semilla_le.setMaximumWidth(180)
        layout.addRow("Semilla:", self.semilla_le)

        self.generar_estructuras_cb = QtWidgets.QCheckBox("Generar Estructuras")
        self.generar_estructuras_cb.setChecked(True)
        self.generar_estructuras_cb.setMaximumWidth(180)
        layout.addRow(self.generar_estructuras_cb)

        self.trucos_cb = QtWidgets.QCheckBox("Permitir Comandos (Trucos)")
        self.trucos_cb.setMaximumWidth(180)
        layout.addRow(self.trucos_cb)

        self.cofre_cb = QtWidgets.QCheckBox("Cofre de Bonificación")
        self.cofre_cb.setMaximumWidth(180)
        layout.addRow(self.cofre_cb)

        self.crear_mundo_btn = QtWidgets.QPushButton("Crear Mundo")
        self.crear_mundo_btn.setMaximumWidth(180)
        layout.addRow(self.crear_mundo_btn)