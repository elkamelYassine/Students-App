import re
import datetime

#global Etudiants
Etudiants={}
def SaisieNumInscrit(NumInscrit):
    return (NumInscrit.isnumeric())and(len(NumInscrit)==7)


def SaisieNom(Nom):
    liste=Nom.split()
    Nom=""
    for i in liste:
        Nom= Nom + i
    if (Nom.isalpha() and len(Nom)<15):
        return True
    else :
        print("Erreur saisie:Ce champs ne peut pas contient des symboles ou des entiers ou plus de 15 caracteres")
        return False

def SaisieDate(date):
    try:
        daychar, monthchar, yearchar = date.split(' ')
    except:
        return False
    day=int(daychar)
    month=int(monthchar)
    year=int(yearchar)
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year%4==0 and (year%100 != 0 or year%400==0):
        day_count_for_month[2] = 29
    return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])

def SaisieAdresse (Adresse):
    return (len(Adresse)<21)
    
def SaisieMail (Email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, Email)):
        return True
    else:
        return False

def SaisieTelephone(Telephone):
    if (Telephone.isnumeric() and len(Telephone)==8):
        return True
    else:
        return False

def SaisieSection(Section):
    if Section.isalpha():
        return True
    else:
        return False
    
def SaisieNiveauEtude(NiveauEtude):
    if (NiveauEtude.isnumeric()):
        return True
    else:
        return False
        
def SuppressionEtudiantDonné  (Etudiants,NumInscrit):
    Etudiants.pop(NumInscrit)

def SuppressionSection(Etudiant,section):
    return({key:val for key, val in Etudiant.items() if val[6]!=section})

def SuppressionNiveau(Etudiant,niv):
    return({key:val for key, val in Etudiant.items() if val[7]!=niv})

def SupprimerNiveauSection(Etudiant,section,niv):
    return(SuppressionSection(SuppressionNiveau(Etudiant,niv),section))


def Afficher (Etudiant):
    ChEntete="| "+"Numeros d'inscriptions"+" | "+6*" "+"Noms"+ " " *6 + " | "+ 4*" "+"Prenoms"+5*" "+" | "+"Dates de Naissances"+" | "+" "*6+"Adresses"+" "*6+" | "+" "*8+ "Mails" + " "*8 +" | "+"Telephones"+" | "+"Sections"+" | "+ "Niveaux"+" |" 
    print (" "+"-"*165+"\n"+ChEntete+"\n"+" "+"-"*165)
    Entete=ChEntete.split("|")
    for cle,val in Etudiant.items():
        line= "| "+ str(cle) + " "*16 + "|"
        k=2
        for info in val:
            line= line +" " +info +" "*(len(Entete[k])-len(info)-1)+ "|"
            k+=1
        print(line+"\n"+" "+"-"*165)

def RechercheParNumInscrit(Etudiant):
    NumInscrit=input("Donner le numero d'inscription de l'etudiant que vous cherchez :")
    return({cle:val for cle, val in Etudiant.items() if cle==NumInscrit})


def RechercheParSection(Etudiant,section):
    return({cle:val for cle, val in Etudiant.items() if val[6]==section})

def AffichageRechParSection (Etudiant,Section):
    DicSection=RechercheParSection(Etudiant,Section)
    if DicSection :
        Afficher(DicSection)
    else:
        print("Il n'existe pas des etudiants de cette section.")    

def RechercheParNiveau(Etudiant,Niveau):
    return ({cle:val for cle, val in Etudiant.items() if val[7]==Niveau})

def AffichageRechParNiveau (Etudiant):
    DicNiveau=RechercheParNiveau(Etudiant)
    if DicNiveau :
        Afficher(DicNiveau)
    else:
        print("Il n'existe pas des etudiants de ce niveau.") 

def RechercheParSection_Niveau(Etudiant,Section,Niveau):
    return(RechercheParNiveau(RechercheParSection(Etudiant,Section),Niveau))

def AffichageRechParNiveau (Etudiant):
    DicSecNiv=RechercheParNiveau(RechercheParSection(Etudiant))
    if DicSecNiv :
        Afficher(DicSecNiv)
    else:
        print("Il n'existe pas des etudiants de ce niveau et cette section en meme temps.")
