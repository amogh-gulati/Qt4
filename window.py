import sys
from PyQt4 import QtGui
#we are inheriting here
class Window(QtGui.QMainWindow): 
    def __init__(self):
        #super returns the parent object
        super(Window,self).__init__() 
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("pyQt")
        self.setWindowIcon(QtGui.QIcon('img.jpg'))
        self.show()
app = QtGui.QApplication(sys.argv) 
GUI = Window()
sys.exit(app.exec_())