# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SupMatiere.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Matiere as Mat
import Note as NT


class Ui_SupMatiere(object):
    def setupUi(self, SupMatiere):
        SupMatiere.setObjectName("SupMatiere")
        SupMatiere.resize(540, 466)
        self.centralwidget = QtWidgets.QWidget(SupMatiere)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 701, 771))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.893, y2:0, stop:0 rgba(92, 37, 141, 255), stop:1 rgba(67, 137, 162, 255))\n"
" }")
        self.widget.setObjectName("widget")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(150, 60, 461, 21))
        self.label.setObjectName("label")
        self.Code = QtWidgets.QLineEdit(self.widget)
        self.Code.setGeometry(QtCore.QRect(180, 180, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Code.setFont(font)
        self.Code.setObjectName("Code")
        self.pushButtonSupprimer = QtWidgets.QPushButton(self.widget)
        self.pushButtonSupprimer.setGeometry(QtCore.QRect(360, 300, 75, 23))
        self.pushButtonSupprimer.setObjectName("pushButtonSupprimer")
        self.pushButtonSupprimer.clicked.connect(self.getInfos)
        self.Code_2 = QtWidgets.QLabel(self.widget)
        self.Code_2.setGeometry(QtCore.QRect(260, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Code_2.setFont(font)
        self.Code_2.setObjectName("Code_2")
        self.Icon = QtWidgets.QLabel(self.widget)
        self.Icon.setGeometry(QtCore.QRect(50, 50, 101, 101))
        self.Icon.setObjectName("Icon")
        self.Matiereinexistante = QtWidgets.QLabel(self.widget)
        self.Matiereinexistante.setGeometry(QtCore.QRect(160, 80, 261, 31))
        self.Matiereinexistante.setObjectName("Matiereinexistante")
        self.Matiereinexistante.setHidden(True)
        self.SuppressionErreur = QtWidgets.QLabel(self.widget)
        self.SuppressionErreur.setGeometry(QtCore.QRect(160, 260, 180, 101))
        self.SuppressionErreur.setObjectName("SuppressionErreur")
        self.SuppressionErreur.setHidden(True)
        self.infoinvalide = QtWidgets.QLabel(self.widget)
        self.infoinvalide.setGeometry(QtCore.QRect(230, 210, 261, 31))
        self.infoinvalide.setObjectName("infoinvalide")
        self.infoinvalide.setHidden(True)
        SupMatiere.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SupMatiere)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        SupMatiere.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SupMatiere)
        self.statusbar.setObjectName("statusbar")
        SupMatiere.setStatusBar(self.statusbar)

        self.retranslateUi(SupMatiere)
        QtCore.QMetaObject.connectSlotsByName(SupMatiere)

    def retranslateUi(self, SupMatiere):
        _translate = QtCore.QCoreApplication.translate
        SupMatiere.setWindowTitle(_translate("SupMatiere", "Suppression d'une matiere"))
        self.pushButtonSupprimer.setText(_translate("SupMatiere", "Supprimer"))
        self.Code_2.setText(_translate("SupMatiere", "<html><head/><body><p><span style=\" color:#ffffff;\">Code</span></p></body></html>"))
        self.Icon.setText(_translate("SupMatiere", "<html><head/><body><p><img src=\":/newPrefix/livre.png\"/></p></body></html>"))
        self.Matiereinexistante.setText(_translate("SupMatiere", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Matiere inexistante</span></p></body></html>"))
        self.SuppressionErreur.setText(_translate("SupMatiere", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Suppression Invalide</span></p></body></html>"))
        self.infoinvalide.setText(_translate("SupMatiere", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Code invalide</span></p></body></html>"))

        self.label.setText(_translate("SupMatiere",
                                  "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Tapez le code de la matiere</span></p></body></html>"))

    def getInfos(self):
        Code=self.Code.text()
        T=[]
        for i in list(NT.Notes.keys()):

            if i[1]==Code:
                T.append(i)

        if (Mat.SaisieCode(Code))and (Code in Mat.Matieres.keys()) :
            for i in T:
                NT.Notes.pop(i)

            Mat.Matieres.pop(Code)
            self.Matiereinexistante.setHidden(True)
            self.SuppressionErreur.setHidden(True)
            self.infoinvalide.setHidden(True)     
        elif not(Mat.SaisieCode(Code)):
            self.infoinvalide.setHidden(False)
            self.SuppressionErreur.setHidden(False)
            self.Matiereinexistante.setHidden(True)
        elif not(Code in Mat.Matieres.keys()):
            self.Matiereinexistante.setHidden(False)
            self.SuppressionErreur.setHidden(False)
            self.infoinvalide.setHidden(True)
       

import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('ISIMM_LOGO.png'))

    SupMatiere = QtWidgets.QMainWindow()
    ui = Ui_SupMatiere()
    ui.setupUi(SupMatiere)
    SupMatiere.show()
    sys.exit(app.exec_())
