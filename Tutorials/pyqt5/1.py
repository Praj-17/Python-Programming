from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

xpos = 200; # x position where you want to start you main window
ypos = 200; # y position where you want to start you main window
width = 544;
height = 600;


        
def clicked():
    print("clicked")
def window():
    app = QApplication(sys.argv) #mandatory line to run a pyqt5 code
    win = QMainWindow()
    win.setGeometry(xpos,ypos, width, height)
    win.setWindowTitle("Student Management System")
    
    label = QtWidgets.QLabel(win)
    label.setText("my first label!")
    label.move(50,50)
    b1 =QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(clicked) 
    win.show()
    sys.exit(app.exec_())
window()