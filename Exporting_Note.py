entete = ["Numeros d'inscriptions", "Code Matiere", "Note DS", "Note examen"]

import Note as NT
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtWidgets import QMessageBox

def EnregistrerTXT(Notes, ch):
    f = open(ch + ".txt", "w")
    f.write(" " + "-" * 78 + "\n")
    ChEntete = "| " + entete[0] + " | " + 3 * " " + entete[1] + " " * 3 + " | " + 4 * " " + entete[2] + 5 * " " + " | " + entete[3] + " | "

    f.write(ChEntete + "\n")

    f.write(" " + "-" * 78 + "\n")
    Entete = ChEntete.split("|")
    for cle, val in Notes.items():
        line = "| " + str(cle[0]) + " " * 16 + "|"
        line += " "+str(cle[1]) + " " * (19-len(str(cle[1]))) + "|"

        k = 3
        for info in val:
            line = line + " " + info + " " * (len(Entete[k]) - len(info) - 1) + "|"
            k += 1
        f.write(line + "\n")
        f.write(" " + "-" * 78 + "\n")
    f.close()


def RecupererTXT(ch):
    Notes = {}
    try:
        f = open(ch + ".txt", "r")
    except:
        return (False)
    f.readline()  # il faut sauter les deux ligne de l'entete
    f.readline()
    while (True):
        f.readline()  # sauter la ligne de "-"
        ch = f.readline()
        info = ch.split("|")
        for i in range(len(info)):
            info[i] = info[i].strip()  # suppression des espaces
        if info == ['']:
            break
        else:
            NT.Notes.update({(info[1], info[2]): info[3:5]})

            Notes.update({(info[1],info[2]): info[3:5]})
        for keys in Notes:
            if (len(keys[1]) > 4):
                FailBox()
                return
    return (Notes)


def EnregistrerCSV(Notes, ch):
    f = open(ch + ".csv", "w")
    for ch in entete:
        f.write(ch + ",")
    f.write("\n")
    for cle, val in Notes.items():
        line = cle[0] + ","
        line += cle[1] + ","

        for info in val:
            line += info + ","
        f.write(line + "\n")
    f.close()


def RecupererCSV(ch):
    Notes = {}
    L = []
    try:
        f = open(ch + ".csv", "r")
    except:
        return (False)
    f.readline()
    L = f.readlines()
    for ch in L:
        info = ch.split(",")
        info[3] = info[3].replace("\n", "")
        Notes.update({(info[0],info[1]): info[2:4]})
    for keys in Notes:
        if (len(keys[1]) > 4):
            FailBox()
            return
    return (Notes)


def NomFichierValide(NomFichier):
    tab = ["<", ">", ":", '"', "/", "|", "?", "*"]
    for i in tab:
        if i in NomFichier:
            return False
    if (len(NomFichier) > 220) or (len(NomFichier) == 0):
        return False
    return True

def Enregistrersous(Notes):
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap('C:/Users/elkam/Desktop/1st year CPI ISIMM/MINI PROJET/python/ISIMM_LOGO.ico')
    textContenttxt=" " + "-" * 78 + "\n"
    ChEntete = "| " + entete[0] + " | " + 3 * " " + entete[1] + " " * 3 + " | " + 4 * " " + entete[
        2] + 5 * " " + " | " + entete[3] + " | "

    textContenttxt=textContenttxt + ChEntete + "\n"

    textContenttxt = textContenttxt + " " + "-" * 78 + "\n"
    Entete = ChEntete.split("|")
    for cle, val in Notes.items():
        line = "| " + str(cle[0]) + " " * 16 + "|"
        line += " " + str(cle[1]) + " " * (19 - len(str(cle[1]))) + "|"

        k = 3
        for info in val:
            line = line + " " + info + " " * (len(Entete[k]) - len(info) - 1) + "|"
            k += 1
        textContenttxt +=    line + "\n"
        textContenttxt +=  " " + "-" * 78 + "\n"
    textContentcsv =""
    for ch in entete:
        textContentcsv +=  ch + ","
    textContentcsv += "\n"
    for cle, val in Notes.items():
        line = cle[0] + ","
        line += cle[1] + ","

        for info in val:
            line += info + ","
        textContentcsv +=line + "\n"

    filename = filedialog.asksaveasfilename(initialdir='/', title='Save as File', filetypes=(
        ('Text Files', '*.txt'), ('Excel Files', '*.csv'), ('All Files', '*.*')), defaultextension=(
        ('Text Files', '*.txt'), ('Excel Files', '*.csv')), initialfile='Note.txt')
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
    filename = filedialog.askopenfilename(initialdir='/', title='Open Note', filetypes=(
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


