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
		
		
		self . sortType = QtGui . QPushButton ( " Add " , self )
		self . sortType . move (240 , 10)
		
		self . sortType = QtGui . QPushButton ( " Delete " , self )
		self . sortType . move (240 , 40)
		
		sortB = QtGui . QPushButton ( " Edit " , self )
		
		sortB . move (240 , 70)


		self . lv = QtGui . QListView ( self )
		self . lv . setModel ( self . model )
		self . lv . setGeometry (20 , 20 , 200 , 150)
             
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
app = QtGui . QApplication ([])
ex =  Example ()
ex.show ()
app . exec_ ()

