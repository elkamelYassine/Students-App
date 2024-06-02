Matieres={}

def SaisieCode(Code):
    return ((Code.isnumeric()) and (len(Code)<12)) 

def SaisieDesignation(Designation):
    return ((Designation.isalpha())and (len(Designation)<10))

def SaisieSection(Section):
    return(Section.isalpha()and (len(Section)<20))

def SaisieCoefficient(Coefficient):
    try :
        test=float(Coefficient)
        return True
    except :
        return False


def SaisieSemestre(Semestre):
    return ((Semestre.upper()=='S1')or(Semestre.upper()=='S2'))

def SuppressionMatiere(Matiere):
    Code=input("Donner le code de la matière à supprimeé :")
    if (Code in Matiere.keys()):
        Matiere.pop(Code)
    else :
        print ('il faut donné un element qui existe')
def ModificationNomMatiere(Matiere):
    Code=input("Donner le code de la matière que vous modifierez son nom :")
    Matiere[Code][0]=input("Donner le nouveau nom.")
    
def ModificationCoefficientMatiere(Matiere):
    Code=input("Donner le code de la matière que vous modifierez son coefficient :")
    Matiere[Code][2]=input("Donner le nouveau coefficient.")

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
        
def RechercheParCode(Matiere):
    while True:
        Code=input("Donner le code de la matiere que vous cherchez :")
        if SaisieCode(Code) :
            break
    return({cle:val for cle, val in Matiere.items() if cle==Code})

def AffichageParCode (Matiere):
    DicCode=RechercheParCode(Matiere)
    if DicCode :
        Afficher(DicCode)
    else:
        print("Il n'existe pas une matiere ayant ce code.")

def RechercheParSection(Matiere,Section):
    if (SaisieSection(Section)):
        return({cle:val for cle, val in Matiere.items() if val[1]==Section})


def RechercheParSemestre(Matiere,Semestre):
    if (SaisieSemestre(Semestre)):
        return({cle:val for cle, val in Matiere.items() if val[3]==Semestre})


def RechercheParSection_Semestre(Matiere):
    while True :   
        Semestre=input("Donner la semestre de la matiere que vous cherchez :")
        if (SaisieSemestre(Semestre)) :
            break
    DicSemestre={cle:val for cle, val in Matiere.items() if val[3]==Semestre}
    return RechercheParSection(DicSemestre)
    
def AffichageRechParSection_Semestre (Matiere):
    DicSection_Semestre=RechercheParSection_Semestre(Matiere)
    if DicSection_Semestre :
        Afficher(DicSection_Semestre)
    else:
        print("Il n'existe pas une ayant cette section et ce semestre en meme temps.")
    
#Ajout (Matiere)
#print(Matiere)
#Matiere={'12345': ['Math', 'cpi', '2', 'S1']}
#Ajout (Matiere)
#Afficher (Matiere)
#AffichageParCode (Matiere)
#AffichageRechParSection_Semestre (Matiere)