# -*- coding: utf-8 -*- 
from PyQt4.QtCore import SIGNAL
import sys 

class Mi_Programa(QtGui.QWidget): 
  
  def __init__(self, parent=None): 
    
    QtGui.QWidget.__init__(self, parent)
    self.setWindowTitle('Calculadora')
    self.resize(192,248) # Tamaño

   
    
    self.lineEdit = QtGui.QLineEdit("",self)
    self.lineEdit.setGeometry(QtCore.QRect(10, 10, 171, 41))
    
    self.pushButton = QtGui.QPushButton("1",self)
    self.pushButton.setGeometry(QtCore.QRect(10, 70, 31, 31))
    
    self.pushButton_2 = QtGui.QPushButton("8",self)
    self.pushButton_2.setGeometry(QtCore.QRect(50, 150, 31, 31))
    
    self.pushButton_3 = QtGui.QPushButton("7",self)
    self.pushButton_3.setGeometry(QtCore.QRect(10, 150, 31, 31))
    
    self.pushButton_4 = QtGui.QPushButton("6",self)
    self.pushButton_4.setGeometry(QtCore.QRect(90, 110, 31, 31))
    
    self.pushButton_5 = QtGui.QPushButton("5",self)
    self.pushButton_5.setGeometry(QtCore.QRect(50, 110, 31, 31))
    
    self.pushButton_6 = QtGui.QPushButton("4",self)
    self.pushButton_6.setGeometry(QtCore.QRect(10, 110, 31, 31))
    
    self.pushButton_7 = QtGui.QPushButton("3",self)
    self.pushButton_7.setGeometry(QtCore.QRect(90, 70, 31, 31))
   
    self.pushButton_8 = QtGui.QPushButton("2",self)
    self.pushButton_8.setGeometry(QtCore.QRect(50, 70, 31, 31))
    
    self.pushButton_9 = QtGui.QPushButton("9",self)
    self.pushButton_9.setGeometry(QtCore.QRect(90, 150, 31, 31))
   
    self.pushButton_10 = QtGui.QPushButton("0",self)
    self.pushButton_10.setGeometry(QtCore.QRect(50, 190, 31, 31))
   
    self.pushButton_11 = QtGui.QPushButton(".",self)
    self.pushButton_11.setGeometry(QtCore.QRect(10, 190, 31, 31))
   
    self.pushButton_12 = QtGui.QPushButton("=",self)
    self.pushButton_12.setGeometry(QtCore.QRect(90, 190, 31, 31))
    
    self.pushButton_13 = QtGui.QPushButton("+",self)
    self.pushButton_13.setGeometry(QtCore.QRect(130, 70, 51, 31))
    
    self.pushButton_14 = QtGui.QPushButton("/",self)
    self.pushButton_14.setGeometry(QtCore.QRect(130, 190, 51, 31))
    
    self.pushButton_15 = QtGui.QPushButton("*",self)
    self.pushButton_15.setGeometry(QtCore.QRect(130, 150, 51, 31))
    
    self.pushButton_16 = QtGui.QPushButton("-",self)
    self.pushButton_16.setGeometry(QtCore.QRect(130, 110, 51, 31))
  
      

    #Le damos la funcionalidad a los botones y llamamos a los def sumando, limpiando 
    #self.connect(self.sumar, QtCore.SIGNAL('clicked()'), self.sumando)
    #self.connect(self.restar, QtCore.SIGNAL('clicked()'), self.restando)
    #self.connect(self.multiplicar, QtCore.SIGNAL('clicked()'), self.multiplicando)
    #self.connect(self.dividir, QtCore.SIGNAL('clicked()'), self.dividiendo)
    #self.connect(self.limpiar, QtCore.SIGNAL('clicked()'), self.limpiando) 

    self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.uno)
    self.connect(self.pushButton_8, QtCore.SIGNAL('clicked()'), self.dos)
    self.connect(self.pushButton_7, QtCore.SIGNAL('clicked()'), self.tres)
    self.connect(self.pushButton_6, QtCore.SIGNAL('clicked()'), self.cuatro)
    self.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.cinco)
    self.connect(self.pushButton_4, QtCore.SIGNAL('clicked()'), self.seis)
    self.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'), self.siete)
    self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.ocho)
    self.connect(self.pushButton_9, QtCore.SIGNAL('clicked()'), self.nueve)
    self.connect(self.pushButton_10, QtCore.SIGNAL('clicked()'), self.cero)
    self.connect(self.pushButton_11, QtCore.SIGNAL('clicked()'), self.punto)
  
  def uno(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"1") 

  def dos(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"2") 

  def tres(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"3") 

  def cuatro(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"4") 

  def cinco(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"5") 

  def seis(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"6") 

  def siete(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"7") 

  def ocho(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"8") 

  def nueve(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"9")

  def cero(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+"0")

  def punto(self):
    cad=self.lineEdit.text()
    self.lineEdit.setText(cad+".")  


  def sumando(self): 
    primer_numero = int(self.primernumero.text())
    segundo_numero = int(self.segundonumero.text())
    lasuma=primer_numero+segundo_numero

    self.sumita.setText(str(lasuma))
    print "El resultado es totalmente correcto...!!!"

  def restando(self):
    primer_numero = int(self.primernumero.text())
    segundo_numero = int(self.segundonumero.text())
    laresta=primer_numero-segundo_numero
    self.sumita.setText(str(laresta))
    print "El resultado es totalmente correcto...!!!"

  def multiplicando(self): 
    primer_numero = int(self.primernumero.text())
    segundo_numero = int(self.segundonumero.text())
    lamultiplicacion=primer_numero*segundo_numero

    self.sumita.setText(str(lamultiplicacion))
    print "El resultado es totalmente correcto...!!!"

  def dividiendo(self): 
    primer_numero = int(self.primernumero.text())
    segundo_numero = int(self.segundonumero.text())
    ladivision=primer_numero/segundo_numero

    self.sumita.setText(str(ladivision))
    print "El resultado es totalmente correcto...!!!"

  def limpiando(self):
    self.sumita.setText("")
    self.primernumero.setText("")
    self.segundonumero.setText("")
    print "se limpio correctamente...!!!"
    
aplicacion = QtGui.QApplication(sys.argv) 
formulario = Mi_Programa() 
formulario.show() 
aplicacion.exec_() 