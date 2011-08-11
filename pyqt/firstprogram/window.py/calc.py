#!/usr/bin/env python
# test ui.py
''' Calculator '''

import sys
from PyQt4.QtGui import QMainWindow, QApplication 
from PyQt4.QtCore import QObject, SIGNAL
from ui import Ui_Calcluator
from functools import partial

def is_digit(string):
    '''check if the given string is a digit or a dot'''
    ordc = ord(string)
    return 0x30 <= ordc <= 0x39 or string == '.'

def is_number(string):
    '''check if the given string is a number'''
    try:
        float(string)
        return True
    except TypeError:
        return False

class Main(QMainWindow):
    ''' Calculator Class '''
    def __init__(self, parent=None):
        ''' initialization of the Calculator ''' 
        QMainWindow.__init__(self, parent)
        self.ui = Ui_Calcluator()
        self.ui.setupUi(self)

        self.numllowkeys = set([0x2a, 0x2b, 0x2d, 0x2e, 0x2f, 0x30, 0x31, \
                0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3d, ] )

        for i in xrange(10):
            eval('QObject.connect(self.ui.button_%d, SIGNAL("clicked()"), \
                    partial(self.process, "%d"))' % (i, i))

        sig = SIGNAL('clicked()')
        QObject.connect(self.ui.button_dot, sig, partial(self.process, '.'))
        QObject.connect(self.ui.button_add, sig, partial(self.process, '+'))
        QObject.connect(self.ui.button_sub, sig, partial(self.process, '-'))
        QObject.connect(self.ui.button_mul, sig, partial(self.process, '*'))
        QObject.connect(self.ui.button_div, sig, partial(self.process, '/'))
        QObject.connect(self.ui.button_cls, sig, partial(self.process, 'c'))
        QObject.connect(self.ui.button_bck, sig, partial(self.process, 'b'))
        QObject.connect(self.ui.button_eval, sig, partial(self.process, '='))

        self.num = self.operator = self.result = None

    def keyPressEvent(self, event):
        ''' override the keyPressEvent method '''
        if event.key() in self.numllowkeys:
            self.process(chr(event.key()))

    def process(self, c):
        text = self.ui.output_area.text()
        c_is_digit = is_digit(c)
        if c == '=':
            if self.operator:
                self.result = eval(str(self.num + self.operator + text))
                self.ui.output_area.setText(str(self.result))
                msg = self.num + self.operator + text + '=' + str(self.result)
                self.ui.statusBar.showMessage(msg)
                self.num = self.result
                self.operator = None
        elif c == 'c':
            self.num = self.operator = None
            self.ui.output_area.setText('0')
            self.ui.statusBar.showMessage('')
        elif c == 'b':
            self.operator = None
            if len(text) <= 1:
                self.ui.output_area.setText('0')
            else:
                self.ui.output_area.setText(text[:-1])
        elif not c_is_digit:
            self.num = text
            self.operator = c
            self.ui.output_area.setText('0')
            self.ui.statusBar.showMessage(text + ' ' + c)
        elif text == '0':
            self.ui.output_area.setText(c)
        else:
            self.ui.output_area.setText(self.ui.output_area.text() + c)

app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
