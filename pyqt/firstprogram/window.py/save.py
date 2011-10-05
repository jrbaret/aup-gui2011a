#!/usr/bin/python
# -*- coding: utf-8 -*-

# sender.py

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
  
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()
        
    def initUI(self):
      
        button1 = QtGui.QPushButton("New", self)
        button1.move(30, 50)

        button2 = QtGui.QPushButton("Edit", self)

        button2.move(150, 50)
    
        button3 = QtGui.QPushButton("Delete", self)
        button3.move(270, 50)

        button4 = QtGui.QPushButton("Save", self)
        button4.move(390, 50)
      
        self.connect(button1, QtCore.SIGNAL('clicked()'), 
            self.buttonClicked)
            
        self.connect(button2, QtCore.SIGNAL('clicked()'), 
            self.buttonClicked)            

        self.connect(button3, QtCore.SIGNAL('clicked()'), 
            self.buttonClicked)
            
        self.connect(button4, QtCore.SIGNAL('clicked()'), 
            self.buttonClicked)

        self.statusBar().showMessage('Ready?')
        self.setWindowTitle('Event sender')
        self.resize(500, 150)


    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar()

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
