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
		names . append ( " Jhayc " )
		names . append ( " Haycj " )
		names . append ( " Ayhj " )
		names . append ( " Yhja " )
		names . append ( " Jane " )
	
		self . model = QtGui . QStringListModel ( names )

	def initUI ( self ):
		lv = QtGui . QListView ( self )
		lv . setModel ( self . model )

		layout = QtGui . QVBoxLayout ()
		layout . addWidget ( lv )
		self . setLayout ( layout )


app = QtGui . QApplication ([])
ex = Example ()
ex . show ()
app . exec_ ()
