import sys
from PyQt4 import QtGui,QtCore
#QtCore is for event handling
#we are inheriting here
class Window(QtGui.QMainWindow): 
    def __init__(self):
        #we would but the main menu here
        super(Window,self).__init__() 
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("pyQt")
        self.setWindowIcon(QtGui.QIcon('img.jpg'))
        #self.show()

        #main menu shit

        extractAction = QtGui.QAction('&Yeah',self)
        # &is for shortcuts
        #creating shortcut
        extractAction.setShortcut('Ctrl+Q')
        #here we have hardcoded shorcuts
        extractAction.setStatusTip('Leave')
        #adding the function
        extractAction.triggered.connect(self.close_application)

        #action 2
        extractAction2 = QtGui.QAction('&YEET',self)
        extractAction2 .setShortcut('Ctrl+C')
        extractAction.setStatusTip('leeve')
        extractAction2.triggered.connect(self.close_application)


        #status bar
        #we dont need the reference to this
        self.statusBar()

        #main menui
        #we need the reference to it becuase we would
        #modify this object
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(extractAction2)
 
        self.home()

    def home(self):
        #specific to the page
        btn = QtGui.QPushButton('Quit',self)
        btn.resize(100,100)
        #btn.resize(btn.sizeHint()) :qt figures out the size
        #btn.resize(btn.minimumSizeHint()) : min
        btn.move(100,100)
        #this would connect a method to a button
        #we can pass the inbuilt method too 
        #btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.close_application)
        self.show()
    
    def close_application(self):
        print("something")
        sys.exit()

def run():
    #this is the main running function
    app = QtGui.QApplication(sys.argv) 
    #creating a window oject
    GUI = Window()
    sys.exit(app.exec_())

run()