import sys
import os
from PyQt5 import QtWidgets
from ui.launcher_window import LauncherWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("ui/styles/main.qss").read() if os.path.exists("ui/styles/main.qss") else "")
    window = LauncherWindow()
    window.show()
    sys.exit(app.exec_())
