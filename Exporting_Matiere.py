

entete=["Code","Designation","Section","Coefficient","Semestre"]
from PyQt5.QtWidgets import QMessageBox
import Matiere as Mat
import tkinter as tk
from tkinter import filedialog

def EnregistrerCSV (Matiere,ch):
    f=open(ch+".csv","w")
    for ch in entete:
        f.write(ch+",")
    f.write("\n")
    for cle,val in Matiere.items():
        line=cle+","
        for info in val:
            line=line+info+","
        f.write(line+"\n")
    f.close ()

def RecupererCSV (ch):
    Matiere={}
    L=[]
    try :
        f=open(ch + ".csv","r")
    except:
        return(False)
    f.readline()
    L=f.readlines()
    for ch in L:
        info=ch.split(",")
        info[4]=info[4].replace("\n","")
        Matiere.update({info[0]:info[1:5]})
    for keys in Matiere :
        if (len (keys) > 5) :
            FailBox()
            return
    return(Matiere)

def EnregistrerTXT(Matiere,ch):
    f=open(ch+".txt","w") 
    f.write(" "+"-"*90+"\n")
    ChEntete="| "+" "*4+entete[0]+" "*4+" | "+5*" "+entete[1]+ " " *5 + " | "+ 7*" "+entete[2]+7*" "+" | "+" "+entete[3]+" "+" | "+" "+entete[4]+" "+"|"  
    
    f.write(ChEntete+"\n")
    
    f.write(" "+"-"*90+"\n")
    Entete=ChEntete.split("|") 
    for cle,val in Matiere.items():
        line= "| "+ str(cle) + " "*(13-len(cle)) + "|"
        k=2
        for info in val:
            line= line +" " +info +" "*(len(Entete[k])-len(info)-1)+ "|"
            k+=1
        f.write(line+"\n")
        f.write(" "+"-"*90+"\n")
    f.close ()
    
def RecupererTXT (ch):
    Matiere={}
    try:
        f = open(ch + ".txt", "r")
    except:
        return (False)

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
            Mat.Matieres.update({info[1]: info[2:6]})

            Matiere.update({info[1]:info[2:6]})
    for keys in Matiere :
        if (len (keys) > 5) :
            FailBox()
            return
    return(Matiere)    

def NomFichierValide(NomFichier):
    tab =["<",">",":",'"',"/","|","?","*"]
    for i in tab:
        if i in NomFichier :
            return False
    if (len(NomFichier)>220) or(len(NomFichier)==0)  :
        return False
    return True


def Enregistrersous(Matiere):
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap('ISIMM_LOGO.ico')
    textContenttxt = " " + "-" * 90 + "\n"
    ChEntete = "| " + " " * 4 + entete[0] + " " * 4 + " | " + 5 * " " + entete[1] + " " * 5 + " | " + 7 * " " + entete[
        2] + 7 * " " + " | " + " " + entete[3] + " " + " | " + " " + entete[4] + " " + "|"

    textContenttxt = textContenttxt + ChEntete + "\n"

    textContenttxt = textContenttxt + " " + "-" * 90 + "\n"
    Entete = ChEntete.split("|")
    for cle, val in Matiere.items():
        line = "| " + str(cle) + " " * (13 - len(cle)) + "|"
        k = 2
        for info in val:
            line = line + " " + info + " " * (len(Entete[k]) - len(info) - 1) + "|"
            k += 1
        textContenttxt = textContenttxt + line + "\n"
        textContenttxt = textContenttxt + " " + "-" * 90 + "\n"

    textContentcsv =""
    for ch in entete:
        textContentcsv =textContentcsv + ch + ","
    textContentcsv =textContentcsv+"\n"
    for cle,val in Matiere.items():
        line=cle+","
        for info in val:
            line=line+info+","
        textContentcsv = textContentcsv + line+"\n"

    filename = filedialog.asksaveasfilename(initialdir='/', title='Save as File', filetypes=(
        ('Text Files', '*.txt'), ('Excel Files', '*.csv'), ('All Files', '*.*')), defaultextension=(
        ('Text Files', '*.txt'), ('Excel Files', '*.csv')), initialfile='Matiere.txt')
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

    filename = filedialog.askopenfilename(initialdir='/', title='Open Matiere', filetypes=(
        ('Text Files', '*.txt'), ('Excel Files', '*.csv'), ('All Files', '*.*')), defaultextension=(
        ('Text Files', '*.txt'), ('Excel Files', '*.csv')))

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



