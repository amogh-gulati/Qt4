import sys
from PyQt4 import QtGui
#this is the major gui 
#three major aspects of gui applications
# 1) some app definition
app = QtGui.QApplication(sys.argv)
#sys the argv enables the application to run form parameters passed 
#by command line
# 2) now something to define the gui
window  = QtGui.QWidget()
#top left is 0,0
window.setGeometry(50,50,300,500)
window.setWindowTitle("PyQt")
# 3) we will always have window.show().
#graphics are made in memory first and then they are
#loaded onto the screen
window.show()
#we have to add this in ubuntu , execute the app maybe
sys.exit(app.exec_()) 