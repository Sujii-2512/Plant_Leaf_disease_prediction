# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

label=""" MainWindow{

font-size:500px;

    
}
"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 1200)  


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.centralwidget.setStyleSheet("QFrame{background:transparent;}")
        self.frame.setGeometry(QtCore.QRect(100, 0, 821, 250))
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtWidgets.QLabel(self.frame)

        #self.label.setGeometry(QtCore.QRect(1100, 2100, 10700, 42000)) 
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setGeometry(QtCore.QRect(335, 20, 250, 265))
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.label1 = QtWidgets.QLabel(self.frame)

        #self.label.setGeometry(QtCore.QRect(1100, 2100, 10700, 42000)) 
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1.setGeometry(QtCore.QRect(650, 20, 500, 265))
        self.label1.setFont(font)
        self.label1.setObjectName(_fromUtf8("label1"))
     
        self.label_2 = QtWidgets.QLabel(self.frame)

        self.label_2.setGeometry(QtCore.QRect(180, 50, 850, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        
        font.setPointSize(20)
        font.setItalic(True)
        font.setWeight(75)
        
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.browse = QtWidgets.QPushButton(self.frame)
    #    self.browse.setStyleSheet("QPushButton{background:transparent;}")
        self.browse.setGeometry(QtCore.QRect(440, 200, 200, 51))
        self.browse.setObjectName(_fromUtf8("PREDICT"))
        font.setWeight(7500)
        font.setFamily(_fromUtf8("URW"))
        font.setPointSize(4000)

        

        MainWindow.setCentralWidget(self.centralwidget)
    
        self.setStyleSheet(label)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
  
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:white; font-size:38px; font-family: Arial\">PLANT LEAF DISEASE DETECTION:</span></p></body></html>", None))
        self.browse.setText(_translate("MainWindow", "PREDICT",  None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:white; font-size:28px; font-family: Arial; margin-bottom:200px; margin-top:200px;margin-right:100px;margin-left:150px; \">Tensorflow</span></p></body></html>", None))
        self.label1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:white; font-size:28px; font-family: Arial; margin-bottom:200px; margin-top:200px;margin-right:100px;margin-left:150px; \">Pytorch</span></p></body></html>", None))



        