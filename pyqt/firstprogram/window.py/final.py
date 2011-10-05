#!/usr/bin/python

# QListView.py

from PyQt4 import QtGui , QtCore

class Example ( QtGui . QMainWindow ):
	def __init__ ( self ):
		super (  Example , self ). __init__ ()
		self . setGeometry (500 , 500 , 350 , 350)
		self . setWindowTitle ( " Grade Calcutaor chorvalu " )
		
	
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

		self.save = QtGui . QPushButton ( 'Save' , self )
		self.save . move (240 , 140)

		self . lv = QtGui . QListView ( self )
		self . lv . setModel ( self . model )
		self . lv . setGeometry (20 , 20 , 200 , 170)
             
		label2 = QtGui.QLabel('Grading System', self)
		label2.move(20, 190)
		
		grades = QtGui.QLabel('98-100	A', self)
		grades.move(20, 210)
		grades = QtGui.QLabel('95-97	A-', self)
		grades.move(20, 230)
		grades = QtGui.QLabel('92-94	B+', self)
		grades.move(20, 250)
		grades = QtGui.QLabel('89-91	B', self)
		grades.move(20, 270)
		grades = QtGui.QLabel('86-88	B-', self)
		grades.move(20, 290)
		grades = QtGui.QLabel('83-85	C+', self)
		grades.move(20, 310)
		grades = QtGui.QLabel('80-82	C', self)
		grades.move(150, 210)		
		grades = QtGui.QLabel('77-79	C-', self)
		grades.move(150, 230)
		grades = QtGui.QLabel('75-76	D', self)
		grades.move(150, 250)
		grades = QtGui.QLabel('BELOW	F', self)
		grades.move(150, 270)		

	def showDialog(self):
		text, ok = QtGui.QInputDialog.getText(self, 'ADD', 
            'Enter Information:')
        
		if ok:
			self.label.setText(str(text))		
		
app = QtGui . QApplication ([])
ex =  Example ()
ex.show ()
app . exec_ ()

