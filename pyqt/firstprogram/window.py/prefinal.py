#!/usr/bin/python

# QListView.py

from PyQt4 import QtGui , QtCore

class Example ( QtGui . QMainWindow ):
	def __init__ ( self ):
		super (  Example , self ). __init__ ()
		self . setGeometry (350 , 350 , 350 , 350)
		self . setWindowTitle ( " Name List " )
		
	
		self . initData ()
		self . initUI ()
	
	def initData ( self ):
		data = ("" )
		self.model = QtGui.QStandardItemModel (12 , 2)


	

	def initUI ( self ):
		self.tv=QtGui.QTableView(self)
		self.tv.setModel(self.model)

		self.tv.move(20,80)
		self.tv.resize(205,150)
		vbox=QtGui.QVBoxLayout()
		vbox.addWidget(self.tv)
		
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
             
		

	def showDialog(self):
		text, ok = QtGui.QInputDialog.getText(self, 'ADD', 
            'Enter Information:')

		if ok:
			self.model.setText(str(text))		

	def add(self,name): 
		data=str(name)
		col=0
		if data != ("") :
			item = QtGui.QStandardItem(str((data)))
			self.model.setItem(self.row,col,item )
			self.row = self.row + 1
			
app = QtGui . QApplication ([])
ex =  Example ()
ex.show ()
app . exec_ ()

