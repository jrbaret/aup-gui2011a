from PyQt4 import QtGui , QtCore
class Example ( QtGui . QWidget ):
	def __init__ ( self ):

		super ( Example , self ). __init__ ()

		self . setGeometry (300 , 300 , 250 , 200)
		self . setWindowTitle ( " QListView " )

		self . initData ()
		self . initUI ()

	def initData ( self ):

		names = QtCore . QStringList ()
		names . append ( " " )
		names . append ( " " )
		names . append ( "  " )
		names . append ( "  " )
		names . append ( "  " )


		self . model = QtGui . QStringListModel ( names )

	def initUI ( self ):

		lv = QtGui . QListView ( self )
		lv . setModel ( self . model )

		layout = QtGui . QVBoxLayout ()
		layout . addWidget ( lv )
		self . setLayout ( layout )

		self . button = QtGui.QPushButton('Dialog', self)
        self . button.setFocusPolicy(QtCore.Qt.NoFocus)

        self . button.move(20, 20)
        self . connect(self.button, QtCore.SIGNAL('clicked()'), 
            self . showDialog)
        self . setFocus()
        
        self . label = QtGui.QLineEdit( self )
        self . label.move(130, 22)
        
        self . setWindowTitle('InputDialog')
        self . setGeometry(300, 300, 350, 80)
		
	def showDialog( self ):
        
			text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
                
			if ok:
				self.label.setText(str(text))

app = QtGui . QApplication ([])
ex = Example ()
ex . show ()
app . exec_ ()
