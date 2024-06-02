import Etudiant
import Matiere
Notes={}
def Ajout (Note,Etudiants,Matieres):
    while True:
        while True : 
            NumInscrit=input("Donner le numero inscription de l'etudiant :")
            if (NumInscrit in Etudiants.keys()):
                break
            

        while True:
            Code=input("Donner le code de la matiere :")
            if (Code in Matieres.keys()):
                break
        if (Etudiants[NumInscrit][6]==Matieres[Code][1]):            #check la section de la matiere et de l'etudiant sont equivalentes
            break
        
    while True :   
        NoteDS=float(input("Donner la note de DS de l'etudiant :"))
        if (SaisieNote(NoteDS)):
            break
      
        
    while True :   
        NoteEX=float(input("Donner la note de l'examen de l'etudiant :"))
        if (SaisieNote(NoteEX)):
            break
    Note.update({(NumInscrit,Code):[NoteDS,NoteEX]})

def SaisieNote (note):
    if (int(note)<=20)and (int (note)>=0):
        return True
    else:
        return False
    
def SupprimerNote(Note):
    NumInscrit=input("Donner le numero d'inscription de l'etudiant de la note à supprimée :")
    Code=input("Donner le code de la matière de la note à supprimeé :")
    if ((NumInscrit,Code) in Note.keys()):
        Note.pop(NumInscrit,Code)
    else :
        print ('il faut donné un element qui existe')
def ModificationNoteDS (Note):
    NumInscrit=input("Donner le numero d'inscription de l'etudiant de la note à modifiée :")
    Code=input("Donner le code de la matière de la note à modifiée :")
    Note[NumInscrit,Code][0]=input("Donner la nouvelle note de DS :")

def ModificationNoteDS (Note):
    NumInscrit=input("Donner le numero d'inscription de l'etudiant de la note à modifiée :")
    Code=input("Donner le code de la matière de la note à modifiée :")
    Note[NumInscrit,Code][1]=input("Donner la nouvelle note d'EX :")

def Afficher (Matiere):
    ChEntete="| "+" "*4+"Code"+" "*4+" | "+5*" "+"Designation"+ " " *5 + " | "+ 7*" "+"Section"+7*" "+" | "+" "+"Coefficient"+" "+" | "+" "+"Semestre"+" "+"|" 
    print (" "+"-"*90+"\n"+ChEntete+"\n"+" "+"-"*90)
    Entete=ChEntete.split("|")
    for cle,val in Matiere.items():
        line= "| "+ str(cle) + " "*(13-len(cle)) + "|"
        k=2
        for info in val:
            line= line +" " +info +" "*(len(Entete[k])-len(info)-1)+ "|"
            k+=1
        print(line+"\n"+" "+"-"*90)
        
