# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecupererationET.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import Etudiant as ET
from Exporting_Etudiant import RecupererTXT,RecupererCSV

class Ui_RecupererationEtudiant(object):
    def setupUi(self, RecupererationEtudiant):
        RecupererationEtudiant.setObjectName("RecupererationEtudiant")
        RecupererationEtudiant.resize(585, 466)
        self.centralwidget = QtWidgets.QWidget(RecupererationEtudiant)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 701, 771))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.893, y2:0, stop:0 rgba(92, 37, 141, 255), stop:1 rgba(67, 137, 162, 255))\n"
" }")
        self.widget.setObjectName("widget")
        self.Icon = QtWidgets.QLabel(self.widget)
        self.Icon.setGeometry(QtCore.QRect(30, 40, 101, 101))
        self.Icon.setObjectName("Icon")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(150, 50, 461, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(390, 200, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.NomFichier = QtWidgets.QLineEdit(self.widget)
        self.NomFichier.setGeometry(QtCore.QRect(150, 199, 221, 21))
        self.NomFichier.setObjectName("NomFichie")
        self.ButtonRecuperer = QtWidgets.QPushButton(self.widget)
        self.ButtonRecuperer.setGeometry(QtCore.QRect(404, 300, 101, 31))
        self.ButtonRecuperer.setStyleSheet("")
        self.ButtonRecuperer.setObjectName("ButtonRecuperer")
        self.ButtonRecuperer.clicked.connect(lambda: self.Recuperer())
        self.TaperLeNom = QtWidgets.QLabel(self.widget)
        self.TaperLeNom.setGeometry(QtCore.QRect(150, 160, 221, 31))
        self.TaperLeNom.setObjectName("TaperLeNom")
        RecupererationEtudiant.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(RecupererationEtudiant)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
        self.menubar.setObjectName("menubar")
        RecupererationEtudiant.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RecupererationEtudiant)
        self.statusbar.setObjectName("statusbar")
        RecupererationEtudiant.setStatusBar(self.statusbar)
        self.retranslateUi(RecupererationEtudiant)
        QtCore.QMetaObject.connectSlotsByName(RecupererationEtudiant)

    def retranslateUi(self, RecupererationEtudiant):
        _translate = QtCore.QCoreApplication.translate
        RecupererationEtudiant.setWindowTitle(_translate("RecupererationEtudiant", "Recupereration Etudiant"))
        self.Icon.setText(_translate("RecupererationEtudiant", "<html><head/><body><p><img src=\":/newPrefix/etudiant.png\"/></p></body></html>"))
        self.label.setText(_translate("RecupererationEtudiant", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Recupereration de tableau etudiant</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("RecupererationEtudiant", ".csv"))
        self.comboBox.setItemText(1, _translate("RecupererationEtudiant", ".txt"))
        self.ButtonRecuperer.setText(_translate("RecupererationEtudiant", "Recuperer"))
        self.TaperLeNom.setText(_translate("RecupererationEtudiant", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Taper le nom du fichier</span></p></body></html>"))

    
    def SuccesssMsg (self):
        msg=QMessageBox ()
        msg.setWindowTitle ("Recupereration validée")
        msg.setText("Le tableau est récupéré")
        msg.setStandardButtons(QMessageBox.Ok)
        x=msg.exec_()
    def FailedMsg (self):
        msg=QMessageBox ()
        msg.setWindowTitle ("Recupereration echouée")
        msg.setText("Recupereration echouée !")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setIcon(QMessageBox.Critical)
        msg.setDetailedText("Impossible d'accéder au fichier. Essayez l'une des opérations suivantes :\n-Vérifiez que le dossier spécifié existe. \n-Vérifiez que le dossier contenant le fichier n'est pas en lecture seule.")
        x=msg.exec_()
    
    def Recuperer (self):
        NomFichier=self.NomFichier.text()
        type = self.comboBox.currentText()


        if (type ==".txt"):
            ET.Etudiants=RecupererTXT(NomFichier)
        else:
            ET.Etudiants=RecupererCSV(NomFichier)
        if (ET.Etudiants != False ):
            self.SuccesssMsg()
           
        else :
            self.FailedMsg()
        


import icons_rc



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('ISIMM_LOGO.png'))
    RecupererationEtudiant = QtWidgets.QMainWindow()
    ui = Ui_RecupererationEtudiant()
    ui.setupUi(RecupererationEtudiant)
    RecupererationEtudiant.show()
    sys.exit(app.exec_())