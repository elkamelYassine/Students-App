
import Note as NT
import Etudiant as ET
import Matiere as Mat


def CalculMoyenneMat(self,keys):
    return ((float(NT.Notes[keys][0][::3])) * 0.25 + (float(NT.Notes[keys][1][::3])) * 0.75)


def CalculMoyenneGen(Numinscrits):
    Moy = 0
    Coefficinets = 0
    for keys in NT.Notes:
        if keys[0] == Numinscrits:
            Coefficinets += float(Mat.Matieres[keys[1]][2])
            Moy += CalculMoyenneMat(keys) * float(Mat.Matieres[keys[1]][2])
    Moy /= Coefficinets
    return (Moy)


def CalculRang(Numinscrit):
    dict = {}
    for keys in NT.Notes:
        if keys not in NT.Notes:
            NT.Notes.update({keys: CalculMoyenneGen(keys)})
    T = sorted(NT.Notes.items(), key=lambda x: x[1])
    return (T.index((Numinscrit, CalculMoyenneGen(Numinscrit))) + 1)


def ResultatISIMM():
    dict = {}
    for i in NT.Notes:
        Rang = CalculRang(i)
        Moyenne = CalculMoyenneGen(i)
        if Moyenne < 10:
            dict.update({i: [ET.Etudiants[i][0], ET.Etudiants[i][1], Rang, Moyenne]})
    return dict
