

entete=["Numeros d'inscriptions","Noms","Prenoms","Dates de Naissances","Adresses","Mails","Telephones","Sections","Niveaux"]

import Etudiant as ET
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtWidgets import QMessageBox

def EnregistrerTXT(Etudiants,ch):
    f=open(ch+".txt","w")
    f.write(" "+"-"*181+"\n")
    ChEntete="| "+entete[0]+" | "+5*" "+entete[1]+ " " *4 + " | "+ 3*" "+entete[2]+4*" "+" | "+entete[3]+" | "+" "*12+entete[4]+" "*13+" | "+" "*12+entete[5]+" "*12+" | "+entete[6]+" | "+entete[7]+" | "+entete[8]+" |"
    
    f.write(ChEntete+"\n")
    
    f.write(" "+"-"*181+"\n")
    Entete=ChEntete.split("|")
    for cle,val in Etudiants.items():
        line= "| "+ str(cle) + " "*16 + "|"
        k=2
        for info in val:
            line= line +" " +info +" "*(len(Entete[k])-len(info)-1)+ "|"
            k+=1
        f.write(line+"\n")
        f.write(" "+"-"*181+"\n")
    f.close ()

def RecupererTXT (ch):
    Etudiants={}  
    try :
        f=open(ch + ".txt","r")
    except:
        return(False)
    f.readline()                       #il faut sauter les deux ligne de l'entete
    f.readline()                     
    while (True):
        f.readline()                   #sauter la ligne de "-"
        ch=f.readline()
        info=ch.split("|")
        for i in range(len(info)):
            info[i]=info[i].strip()    #suppression des espaces
        if info==['']:
            break
        else :
            ET.Etudiants.update({info[1]:info[2:10]})
            Etudiants.update({info[1]:info[2:10]})
    return(Etudiants)
   
def EnregistrerCSV (Etudiants,ch):
    f=open(ch+".csv","w")
    for ch in entete:
        f.write(ch+",")
    f.write("\n")
    for cle,val in Etudiants.items():
        line=cle+","
        for info in val:
            line=line+info+","
        f.write(line+"\n")
    f.close ()

def RecupererCSV (ch):
    Etudiants={}
    L=[]
    try :
        f=open(ch+".csv","r")
    except:
        return(False)
    f.readline()
    L=f.readlines()
    for ch in L:
        info=ch.split(",")
        info[8]=info[8].replace("\n","")
        Etudiants.update({info[0]:info[1:9]})
    return(Etudiants)

def NomFichierValide(NomFichier) :
    tab =["<",">",":",'"',"/","|","?","*"]
    for i in tab:
        if i in NomFichier :
            return False
    if (len(NomFichier)>220) or(len(NomFichier)==0)  :
        return False
    return True

def Enregistrersous (Etudiants):
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap('C:/Users/elkam/Desktop/1st year CPI ISIMM/MINI PROJET/python/ISIMM_LOGO.ico')
    ChEntete = "| " + entete[0] + " | " + 5 * " " + entete[1] + " " * 4 + " | " + 3 * " " + entete[
        2] + 4 * " " + " | " + entete[3] + " | " + " " * 12 + entete[4] + " " * 13 + " | " + " " * 12 + entete[
                   5] + " " * 12 + " | " + entete[6] + " | " + entete[7] + " | " + entete[8] + " |"

    textContenttxt =" "+"-"*181+"\n"+ChEntete+"\n"+" "+"-"*181+"\n"

    Entete = ChEntete.split("|")
    for cle,val in Etudiants.items():
        line = "| "+ str(cle) + " "*16 + "|"
        k=2
        for info in val:
            line= line +" " +info +" "*(len(Entete[k])-len(info)-1)+ "|"
            k+=1
        textContenttxt=textContenttxt + line+"\n"
        textContenttxt=textContenttxt + " "+"-"*181+"\n"

    textContentcsv=''

    for ch in entete:
        textContentcsv= textContentcsv + ch + ","
    textContentcsv= textContentcsv+ "\n"
    for cle,val in Etudiants.items():
        line=cle+","
        for info in val:
            line=line+info+","
        textContentcsv = textContentcsv + line+"\n"

    filename = filedialog.asksaveasfilename(initialdir='/', title='Save as File', filetypes=(
        ('Text Files', '*.txt'), ('Excel Files', '*.csv'), ('All Files', '*.*')),defaultextension=(
        ('Text Files', '*.txt'), ('Excel Files', '*.csv')),initialfile='Etudiant.txt' )
    if (filename[-4:] != '.csv') and (filename[-4:] != '.txt'):
        filename= filename+".txt"


    if (filename[-4:] == '.csv' ):
        textContent = textContentcsv
    else :
        textContent = textContenttxt
    myfile = open(filename, "w+")
    myfile.write(textContent)

def FailBox ():
    msg = QMessageBox()
    msg.setWindowTitle("Recupereration echouée")
    msg.setText("Fichier incompatible")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()

def Importfrom ():
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap('C:/Users/elkam/Desktop/1st year CPI ISIMM/MINI PROJET/python/ISIMM_LOGO.ico')
    filename = filedialog.askopenfilename(initialdir='/', title='Open Etudiant', filetypes=(
        ('Text Files', '*.txt'), ('Excel Files', '*.csv'), ('All Files', '*.*')))
    if (filename == '') :
        return

    myfile = open(filename)


    if (filename[-4:] == '.txt'):
        try:
            RecupererTXT(filename[0:(len(filename)-4):1])
        except :
            FailBox()

    else :
        try:
            RecupererCSV(filename[0:(len(filename)-4):1])
        except :
            FailBox()


