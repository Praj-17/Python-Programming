from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

xpos = 200; # x position where you want to start you main window
ypos = 200; # y position where you want to start you main window
width = 544;
height = 600;

class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow,self).__init__()
        self.initUI()
        self.setGeometry(xpos,ypos, width, height)
        self.setWindowTitle("Student Management System")
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50,50)
        self.b1 =QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked) 
    def clicked(self):
        self.label.setText("you pressed the text")
        self.update()
    def update(self):
        self.label.adjustSize()
        

def window():
    app = QApplication(sys.argv) #mandatory line to run a pyqt5 code
    win = Mywindow()
    
    
    win.show()
    sys.exit(app.exec_())
window()