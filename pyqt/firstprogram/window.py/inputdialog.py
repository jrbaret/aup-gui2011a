# inputdialog.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):
  
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

        
    def initUI(self):

        self.button = QtGui.QPushButton('Enter Name', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button.move(60, 20)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), 
            self.showDialog)
        self.setFocus()

        
        self.button = QtGui.QPushButton('Delete', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button.move(160, 20)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), 
            self.buttonClicked)
        self.setFocus()
        
        self.setWindowTitle('InputDialog')
        self.setGeometry(300, 300, 300, 80)


        
    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')    
    
    
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter Information:')
        
        if ok:
            self.label.setText(str(text))


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
