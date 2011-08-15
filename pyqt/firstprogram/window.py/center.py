#!/usr/bin/python

# icon.py

import sys
from PyQt4 import QtGui, QtCore




class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

   
			

        self.setGeometry(600, 300, 111100, 1111350)
        self.setWindowTitle('Menu')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.resize(250,150)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-self.width())/2, (screen.height()-self.height())/2)
        
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(0, 0, 60, 35)
        quitgeo = quit.geometry();
        quit.move((size.width()/2) - (quitgeo.width()/2), (size.height()/2) - (quitgeo.height()/2))
        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))
            
        self.exit = QtGui.QAction(QtGui.QIcon('icon.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))



        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exit)

		


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
