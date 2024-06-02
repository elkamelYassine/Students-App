# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TaperLeNumInscritET.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from AffichageNote import Ui_AffichageNote
import Etudiant as ET
import Note as NT


def Dicts (NumInscrit):
    dicts={}
    T=list(NT.Notes.keys())
    for i in T :
        if i[0]==NumInscrit:
            dicts.update({i:NT.Notes[i]})
    return dicts
class Ui_RechNumInscritNT(object):


    
    def openAffichageNote(self,dict):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_AffichageNote()
        self.ui.setupUi(self.window,dict)
        self.window.show()

    def setupUi(self, RechNumInscritET):

        
        RechNumInscritET.setObjectName("RechNumInscritET")
        RechNumInscritET.resize(556, 444)
        self.centralwidget = QtWidgets.QWidget(RechNumInscritET)
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
        self.pushButtonChercher.clicked.connect(self.getInfos)
        
        self.Numinscrit_2 = QtWidgets.QLabel(self.widget)
        self.Numinscrit_2.setGeometry(QtCore.QRect(180, 140, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Numinscrit_2.setFont(font)
        self.Numinscrit_2.setObjectName("Numinscrit_2")
        self.Icon = QtWidgets.QLabel(self.widget)
        self.Icon.setGeometry(QtCore.QRect(30, 50, 101, 101))
        self.Icon.setObjectName("Icon")
        self.Letudiantnexistepas = QtWidgets.QLabel(self.widget)
        self.Letudiantnexistepas.setGeometry(QtCore.QRect(130, 70, 261, 31))
        self.Letudiantnexistepas.setObjectName("Letudiantnexistepas")
        self.Letudiantnexistepas.setHidden(True)
        self.infoinvalideInscrit = QtWidgets.QLabel(self.widget)
        self.infoinvalideInscrit.setGeometry(QtCore.QRect(170, 210, 251, 31))
        self.infoinvalideInscrit.setObjectName("infoinvalideInscrit")
        self.infoinvalideInscrit.setHidden(True)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(130, 40, 361, 21))
        self.label.setObjectName("label")
        RechNumInscritET.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RechNumInscritET)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 21))
        self.menubar.setObjectName("menubar")
        RechNumInscritET.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RechNumInscritET)
        self.statusbar.setObjectName("statusbar")
        RechNumInscritET.setStatusBar(self.statusbar)

        self.retranslateUi(RechNumInscritET)
        QtCore.QMetaObject.connectSlotsByName(RechNumInscritET)

    def retranslateUi(self, RechNumInscritET):
        _translate = QtCore.QCoreApplication.translate
        RechNumInscritET.setWindowTitle(_translate("RechNumInscritET", "Recherche par numero d'inscription"))
        self.pushButtonChercher.setText(_translate("RechNumInscritET", "Chercher"))
        self.Numinscrit_2.setText(_translate("RechNumInscritET", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Numero d\'inscription</span></p></body></html>"))
        self.Icon.setText(_translate("RechNumInscritET", "<html><head/><body><p><img src=\":/newPrefix/183338.png\"/></p></body></html>"))
        self.Letudiantnexistepas.setText(_translate("RechNumInscritET", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ff0000;\">L\'étudiant n\'existe pas</span></p></body></html>"))
        self.infoinvalideInscrit.setText(_translate("RechNumInscritET", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ff0000;\">Numero d\'inscription invalide</span></p></body></html>"))
        self.label.setText(_translate("RechNumInscritET", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Tapez le numero d\'inscription de l\'étudiant</span></p></body></html>"))
    def getInfos(self):
        Numinscrit=self.Numinscrit.text()
        T=[]
        for i in list(NT.Notes.keys()) :
            T.append( list (i)[0])
            
        print (T)
        if (ET.SaisieNumInscrit(Numinscrit)) and (Numinscrit in T):
            dict=Dicts(Numinscrit)
            self.openAffichageNote(dict)
            self.Letudiantnexistepas.setHidden(True)
            self.infoinvalideInscrit.setHidden(True)     
        elif not(ET.SaisieNumInscrit(Numinscrit)):
            self.infoinvalideInscrit.setHidden(False)
      
            self.Letudiantnexistepas.setHidden(True)
        elif not(Numinscrit  in NT.Notes.keys()):
            self.Letudiantnexistepas.setHidden(False)
           
            self.infoinvalideInscrit.setHidden(True)
        
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('ISIMM_LOGO.png'))
    RechNumInscritET = QtWidgets.QMainWindow()
    ui = Ui_RechNumInscritNT()
    ui.setupUi(RechNumInscritET)
    RechNumInscritET.show()
    sys.exit(app.exec_())