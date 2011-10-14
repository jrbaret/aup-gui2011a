#!/usr/bin/python

# QListView.py

from PyQt4 import QtGui , QtCore

class Example ( QtGui . QMainWindow ):
	def __init__ ( self ):
		super (  Example , self ). __init__ ()
		self . setGeometry (350 , 350 , 350 , 350)
		self . setWindowTitle ( " Final " )
		
	
		self . initData ()
		self . initUI ()
	
	def initData ( self ):
		names = QtCore . QStringList ()
		names . append ( " JhayC " )
		names . append ( " Baret " )
		
		self . model = QtGui . QStringListModel ( names )
		self . filterModel = QtGui . QSortFilterProxyModel ( self )
		self . filterModel . setSourceModel ( self . model )


	

	def initUI ( self ):
		
		
		self.add = QtGui . QPushButton ( " Add " , self )
		self.add.setFocusPolicy(QtCore.Qt.NoFocus)
		self.add . move (240 , 20)
		self.connect(self.add, QtCore.SIGNAL('clicked()'), 
            self.showDialog)
		self.setFocus()
		
		self.delete = QtGui . QPushButton ( " Delete " , self )
		self.delete . move (240 , 60)
		
		self.edit = QtGui . QPushButton ( " Edit " , self )
		self.edit . move (240 , 100)

		self . lv = QtGui . QListView ( self )
		self . lv . setModel ( self . model )
		self . lv . setGeometry (20 , 20 , 200 , 170)
		self . lv . move (10 , 150)

	def showDialog(self):
		text, ok = QtGui.QInputDialog.getText(self, 'ADD', 
            'Enter Information:')
        
		if ok:
			names.append.setText(str(text))		
		
app = QtGui . QApplication ([])
ex =  Example ()
ex.show ()
app . exec_ ()

