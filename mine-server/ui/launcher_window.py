import os
import random
import getpass
from PyQt5 import QtWidgets, QtCore, QtGui

from ui.crear_servidor import CrearServidorWidget
from ui.configuracion_mundo import ConfiguracionMundoWidget
from ui.gestion_mundos import GestionMundosWidget
from ui.consola import ConsolaWidget

def generar_fondo_pixelado(ancho, alto, tam_pixel=16):
    pixmap = QtGui.QPixmap(ancho, alto)
    painter = QtGui.QPainter(pixmap)
    for y in range(0, alto, tam_pixel):
        for x in range(0, ancho, tam_pixel):
            tono = random.randint(80, 180)
            color = QtGui.QColor(tono, random.randint(120, 200), tono // 2)
            painter.fillRect(x, y, tam_pixel, tam_pixel, color)
    painter.end()
    return pixmap

class LauncherWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minecraft Server Launcher")
        self.setFixedSize(900, 666)
        qss_path = os.path.join(os.path.dirname(__file__), 'styles', 'main.qss')
        if os.path.exists(qss_path):
            with open(qss_path, 'r', encoding='utf-8') as f:
                self.setStyleSheet(f.read())
        self.init_ui()
        self.set_fondo_pixelado()

    def set_fondo_pixelado(self):
        fondo = generar_fondo_pixelado(self.width(), self.height(), tam_pixel=16)
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(fondo))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def init_ui(self):
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Panel izquierdo con scroll
        left_panel = QtWidgets.QScrollArea()
        left_panel.setWidgetResizable(True)
        left_panel.setFrameShape(QtWidgets.QFrame.NoFrame)

        left_widget = QtWidgets.QWidget()
        left_layout = QtWidgets.QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(20)

        self.crear_servidor = CrearServidorWidget()
        left_layout.addWidget(self.crear_servidor)

        self.gestion_mundos = GestionMundosWidget()
        left_layout.addWidget(self.gestion_mundos)

        self.consola = ConsolaWidget()
        usuario = getpass.getuser()
        self.consola.setText(f"¿Qué vamos a crear hoy, {usuario}?...")  # mensaje inicial
        left_layout.addWidget(self.consola)

        left_layout.addStretch()
        left_panel.setWidget(left_widget)
        main_layout.addWidget(left_panel, 1)

        # Panel derecho
        right_panel = QtWidgets.QWidget()
        right_layout = QtWidgets.QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.config_mundo = ConfiguracionMundoWidget()
        scroll_area.setWidget(self.config_mundo)

        right_layout.addWidget(scroll_area, stretch=1)
        main_layout.addWidget(right_panel, 1)
