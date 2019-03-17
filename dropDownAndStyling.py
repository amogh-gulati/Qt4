#toolbar popup checkbox progress bar
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
        # alpahbet following & will become the 
        #shortcut

        #creating shortcut
        extractAction.setShortcut('Ctrl+Q')
        #here we have hardcoded shorcuts
        extractAction.setStatusTip('Leave')
        #adding the function
        extractAction.triggered.connect(self.close_application)

        #action 2
        extractAction2 = QtGui.QAction('&lYEET',self)
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
        # toolbar specific to the page
        btn = QtGui.QPushButton('Quit',self)
        btn.resize(100,100)
        #btn.resize(btn.sizeHint()) :qt figures out the size
        #btn.resize(btn.minimumSizeHint()) : min
        btn.move(100,100)

        #toolbar shits

        extractAction = QtGui.QAction(QtGui.QIcon('img.jpg'),'flee',self)
        extractAction.triggered.connect(self.close_application)
        #note : if we write close_application() with
        #paranthesis application will close as soon as its 
        #loaded in ram because that function will be callled


        #create toolbar
        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        #this would connect a method to a button
        #we can pass the inbuilt method too 
        #btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.close_application)

        #checkbox shit

        checkBox  = QtGui.QCheckBox('Enlarge Window',self)
        #checkBox.toggle to keep the checkbox checked by 
        #default
        checkBox.stateChanged.connect(self.enlargeWindow) 
        checkBox.move(70,40)

        #progress bar shit

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QtGui.QPushButton("fake progress",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.prog)

        #drop down shit

        #to get the default style
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Windows Vista",self)
        #the above is to change style

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("CleanLooks")
        comboBox.addItem("WindowsVista")
        #ideadlly the style setting should be done in init
        #but here we are also using it with combo box so its 
        #here

        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)
        self.show()
    
    def close_application(self):
        #pop up shit here
        choice = QtGui.QMessageBox.question(self,
        'exit','exit?',QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No)
        #now choice will either be yes 
        #object or no object
        if choice==QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def enlargeWindow(self,state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)

    def prog(self):
        self.completed = 0
        while(self.completed<100):
            self.completed+=0.0001
            self.progress.setValue(self.completed)

    def style_choice(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

def run():
    #this is the main running function
    app = QtGui.QApplication(sys.argv) 
    #creating a window oject
    GUI = Window()
    sys.exit(app.exec_())

run()