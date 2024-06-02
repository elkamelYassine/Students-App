# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModAdresseET.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
import Etudiant as ET

class Ui_ModAdresseET(object):
    
    def AdresseObjects (self,A):
        self.Adresse.setHidden(A)
        self.Adresse_2.setHidden(A)
        self.pushButtonModifer.setHidden(A)
    
    def NumInsritObjects (self,A):
        self.Numinscrit.setHidden(A)
        self.Numinscrit_2.setHidden(A)
        self.pushButtonChercher.setHidden(A)
        self.label.setHidden(A)
    
    def setupUi(self, ModAdresseET):
        ModAdresseET.setObjectName("ModAdresseET")
        ModAdresseET.resize(585, 466)
        self.centralwidget = QtWidgets.QWidget(ModAdresseET)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 701, 771))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.893, y2:0, stop:0 rgba(92, 37, 141, 255), stop:1 rgba(67, 137, 162, 255))\n"
" }")


        self.widget.setObjectName("widget")
        self.Numinscrit = QtWidgets.QLineEdit(self.widget)
        self.Numinscrit.setGeometry(QtCore.QRect(180, 180, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Numinscrit.setFont(font)
        self.Numinscrit.setObjectName("Numinscrit")
        self.pushButtonChercher = QtWidgets.QPushButton(self.widget)
        self.pushButtonChercher.setGeometry(QtCore.QRect(360, 300, 75, 23))
        self.pushButtonChercher.setObjectName("pushButtonChercher")
        self.pushButtonChercher.clicked.connect(self.buttonChercher)
        self.pushButtonChercher.clicked.connect(self.buttonChercher)
        
        self.Numinscrit_2 = QtWidgets.QLabel(self.widget)
        self.Numinscrit_2.setGeometry(QtCore.QRect(210, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Numinscrit_2.setFont(font)
        self.Numinscrit_2.setObjectName("Numinscrit_2")
        self.Icon = QtWidgets.QLabel(self.widget)
        self.Icon.setGeometry(QtCore.QRect(30, 50, 101, 101))
        self.Icon.setObjectName("Icon")
        self.Letudiantnexistepas = QtWidgets.QLabel(self.widget)
        self.Letudiantnexistepas.setGeometry(QtCore.QRect(140, 75, 261, 31))
        self.Letudiantnexistepas.setObjectName("Letudiantnexistepas")
        self.Letudiantnexistepas.setHidden(True)
        self.infoinvalideInscrit = QtWidgets.QLabel(self.widget)
        self.infoinvalideInscrit.setGeometry(QtCore.QRect(170, 210, 261, 31))
        self.infoinvalideInscrit.setObjectName("infoinvalideInscrit")
        self.infoinvalideInscrit.setHidden(True)
        self.Adresse = QtWidgets.QLineEdit(self.widget)
        self.Adresse.setGeometry(QtCore.QRect(180, 180, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Adresse.setFont(font)
        self.Adresse.setObjectName("Adresse")
        self.Adresse_2 = QtWidgets.QLabel(self.widget)
        self.Adresse_2.setGeometry(QtCore.QRect(190, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Adresse_2.setFont(font)
        self.Adresse_2.setObjectName("Adresse_2")
        self.infoinvalideAdresse = QtWidgets.QLabel(self.widget)
        self.infoinvalideAdresse.setGeometry(QtCore.QRect(170, 210, 261, 31))
        self.infoinvalideAdresse.setObjectName("infoinvalideAdresse")
        self.infoinvalideAdresse.setHidden(True)
        self.pushButtonModifer = QtWidgets.QPushButton(self.widget)
        self.pushButtonModifer.setGeometry(QtCore.QRect(360, 300, 75, 23))
        self.pushButtonModifer.setObjectName("pushButtonModifer")
        #Numinscrit=self.Numinscrit.text()
        self.pushButtonModifer.clicked.connect(self.buttonModifier)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(110, 40, 461, 21))
        self.label.setObjectName("label")
        ModAdresseET.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModAdresseET)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
        self.menubar.setObjectName("menubar")
        ModAdresseET.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModAdresseET)
        self.statusbar.setObjectName("statusbar")
        ModAdresseET.setStatusBar(self.statusbar)

        self.retranslateUi(ModAdresseET)
        QtCore.QMetaObject.connectSlotsByName(ModAdresseET)
        self.NumInsritObjects (False)   
        self.AdresseObjects (True)

       
    def retranslateUi(self, ModAdresseET):
        _translate = QtCore.QCoreApplication.translate
        ModAdresseET.setWindowTitle(_translate("ModAdresseET", "Modification d'une adresse d'un étudiant"))
        self.pushButtonChercher.setText(_translate("ModAdresseET", "Chercher"))
        self.Numinscrit_2.setText(_translate("ModAdresseET", "<html><head/><body><p><span style=\" color:#ffffff;\">Numero d\'inscription</span></p></body></html>"))
        self.Icon.setText(_translate("ModAdresseET", "<html><head/><body><p><img src=\":/newPrefix/etudiant.png\"/></p></body></html>"))
        self.Letudiantnexistepas.setText(_translate("ModAdresseET", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">L\'étudiant n\'existe pas</span></p></body></html>"))
        self.infoinvalideInscrit.setText(_translate("ModAdresseET", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Numero d\'inscription invalide</span></p></body></html>"))
        self.Adresse_2.setText(_translate("ModAdresseET", "<html><head/><body><p><span style=\" color:#ffffff;\">Nouvelle Adresse</span></p></body></html>"))
        self.infoinvalideAdresse.setText(_translate("ModAdresseET", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Adresse invalide</span></p></body></html>"))
        self.pushButtonModifer.setText(_translate("ModAdresseET", "Modifier"))
        self.label.setText(_translate("ModAdresseET", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Tapez le numero d\'inscription de l\'étudiant à modifer</span></p></body></html>"))


    
    def buttonChercher(self):
        global Numinscrit
        Numinscrit=self.Numinscrit.text()
        if (ET.SaisieNumInscrit(Numinscrit))and (Numinscrit in ET.Etudiants.keys()) :
            self.NumInsritObjects (True)   
            self.AdresseObjects (False)
            self.Letudiantnexistepas.setHidden(True)  
            self.infoinvalideInscrit.setHidden(True)     
        elif not(ET.SaisieNumInscrit(Numinscrit)):
            self.infoinvalideInscrit.setHidden(False)     
            self.Letudiantnexistepas.setHidden(True)
        elif not(Numinscrit  in ET.Etudiants.keys()):
            self.Letudiantnexistepas.setHidden(False) 
            self.infoinvalideInscrit.setHidden(True)
      

    
    def buttonModifier(self):
        Adresse=self.Adresse.text()
        if (ET.SaisieAdresse(Adresse)) :
            ET.Etudiants[Numinscrit][4]=Adresse  
            self.infoinvalideInscrit.setHidden(True)     
        else:
            self.infoinvalideAdresse.setHidden(False)



import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModAdresseET = QtWidgets.QMainWindow()
    ui = Ui_ModAdresseET()
    ui.setupUi(ModAdresseET)
    ModAdresseET.show()
    sys.exit(app.exec_())

