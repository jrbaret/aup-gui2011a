from PyQt4 import QtGui , QtCore
class Example ( QtGui.QWidget ):

	row = 0

	def __init__ ( self ):
		super ( Example , self ). __init__ ()
		self.resize(430,350)
		self.setWindowTitle ( " Final Program " )
		self.initData ()
		self.initUI ()
		row=0;
		col=0;

	def initData ( self ):
		data = ("" )
		self.model = QtGui.QStandardItemModel (12 , 2)

		col = 0
		for i in data :
			item = QtGui.QStandardItem(str((i)))
			self.model.setItem(self.row,col,item )
			self.row = self.row + 1
			self.col = self.col + 1
			 
	def initUI ( self ):
		self . model = QtGui . QStandardItemModel ()
		labels = QtCore . QStringList (( " Acitivity " , " Grade " ))
		self . model . setHorizontalHeaderLabels ( labels )
		
		self.tv=QtGui.QTableView(self)
		self.tv.setModel(self.model)

		self.tv.move(20,80)
		self.tv.resize(205,150)
		vbox=QtGui.QVBoxLayout()
		vbox.addWidget(self.tv)
		

		col=0
		row=0
		
		add=QtGui.QPushButton("Add",self) #add button
		add.move(300,100)
		self.connect(add, QtCore.SIGNAL('clicked()'), self.showDialog)

        
		self.delete=QtGui.QPushButton("Delete",self) #delete button
		self.delete.move(300,130)
		
		self . connect ( self . delete , QtCore . SIGNAL ( " clicked () " ) , self . DeleteClicked )


		
		self.edit=QtGui.QPushButton("Edit",self) #edit button
		self.edit.move(300,160)
		self.connect(self.edit, QtCore.SIGNAL('clicked()'), self.editMode)

		self.name=QtGui.QLabel("Name:Baret Jestoni", self)
		self.name.move(15,10)

		self.year=QtGui.QLabel("SY :1st semester 2011-12", self)
		self.year.move(15,25)

		self.subject=QtGui.QLabel("Subject : Graphical User Interface", self)
		self.subject.move(200,10)

		self.teacher=QtGui.QLabel("Teacher : Israel Canasa", self)
		self.teacher.move(200,25)

		self.legend=QtGui.QLabel("Legend", self)
		self.legend.move(15,260)
		
		self.grade=QtGui.QLabel("Grade: A", self)
		self.grade.move(300,260)

	def showDialog(self): #Adding

		text, ok = QtGui.QInputDialog.getText(self, 'Add', 
				'Activity:')

		if ok:
			name=str(text)
			self.add(name)

			
	def add(self,name): 
		data=str(name)
		col=0
		if data != ("") :
			item = QtGui.QStandardItem(str((data)))
			self.model.setItem(self.row,col,item )
			self.row = self.row + 1

	def DeleteClicked(self):
        # Remove the currently selected item from the listview.
		self.listview.takeItem(self.listview.currentItem())
        
        # Check if the list is empty - if yes, disable the deletebutton.
		if self.listview.childCount() == 0: self.deletebutton.setEnabled(False)


	
	def editMode ( self ): # Editing
		
		self.row = QtGui.QLineEdit(self)
		
app=QtGui.QApplication([])
ex=Example()
ex.show()
app.exec_()
