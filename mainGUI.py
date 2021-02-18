import sys
import random
import Launcher
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(840, 525)
        self.center()
        self.setWindowTitle('Sky Line Minecraft Launcher2-dev0.0.2')
        self.setWindowIcon(QIcon('.\\assets\\images\\icon.png'))
        bgnum = str(random.randint(1, 4))
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./assets/images/bg/" + bgnum + ".png")))
        self.button()
        self.setPalette(palette)
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def launch(self):
        Launcher.launch("1.12.2")
    def button(self):
        self.LaunchButton = QPushButton('启动游戏', self)
        self.LaunchButton.setStyleSheet("QPushButton{font-family:'Microsoft YaHei';font-size:16px;color:rgb(0,0,0,255);}\QPushButton{background-color:rgb(50,100,170)}\ QPushButton:hover{background-color:rgb(50, 50, 150)}")
        self.LaunchButton.setToolTip('<b>点此启动游戏</b>')
        self.LaunchButton.clicked.connect(Launcher.launch)
        self.LaunchButton.resize(128, 72)
        self.LaunchButton.move(675, 400)

def OpenGUI():
    app = QApplication(sys.argv)
    mg = MainGUI()
    sys.exit(app.exec_())