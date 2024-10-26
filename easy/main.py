from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication,QInputDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = Image.open('fg.webp')        
        self.update_image()
        self.ui.btn_left.clicked.connect(self.rotate_left)
        self.ui.btn_right
        self.clicked.connect(self.rotate_right)
    def update_image(self):
        self.ui.label.hide()
        pixmap = QPixmap('fg.webp')
        w, h = self.ui.label.width(), self.ui.label.height()
        pixmap = pixmap.scaled(w, h)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.show()
    def rotate_left(self):
        self.image = self.image.rotate(90)
        self.update_image()
        
    def rotate_right(self):
        self.image = self.image.rotate(-90)
        self.update_image()


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()