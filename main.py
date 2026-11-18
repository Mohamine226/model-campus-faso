class Etudiant:
    def presentation(self, nom, prenom, age):
        if age > 23:
            print("Non eligible")
        else:
            self.nom = nom
            self.prenom= prenom
            ine = str(input("Entrez l'INE:"))
            mot_de_passe = str(input("Entrez un mot de passe:"))
            liste = [
                self.nom  ,
                self.prenom  ,
                ine,
                mot_de_passe
                ]
            return liste

    
    def compte(self, liste):
        mot_de_passe = str(input("Entrez votre mot de passe:"))
        while mot_de_passe != liste[3]:
            print("Mot de passe incorect.")
            mot_de_passe = str(input(" veuillez ressayer a nouveau: "))
        if(mot_de_passe == liste[3]):
            print(f"{liste[1]} {liste[0]}, vous êtes connecté avec succes")
            return 1

filieres =[
    ['1','Langues moderne'],
    ['2','Sociaulogie'],
    ['3','Histoire et archeologie'],
    ['4','Linguistique'],
    ['5','Geographie'],
    ['6','Anglais'],
    ['7','Almande'],
    ['8','Philosophie'],
    ['9','sphycologie'],
    ]
filieres1 =[
    ['1','Droit'],
    ['2','Langues moderne'],
    ['3','Sociaulogie'],
    ['4','Histoire et archeologie'],
    ['5','Linguistique'],
    ['6','Geographie'],
    ['7','Anglais'],
    ['8','Almande'],
    ['9','Philosophie'],
    ['10','sphycologie'],
    ]
filieres2 = [
    ['1','MPCI'],
    ['2','SVT'],
    ['3','Science economie et de gestion'],
    ['4','Langues moderne'],
    ['5','Sociaulogie'],
    ['6','Histoire et archeologie'],
    ['7','Linguistique'],
    ['8','Geographie'],
    ['9','Anglais'],
    ['10','Almande'],
    ['11','Philosophie'],
    ['12','sphycologie'],
]

filieres3 = [
    ['1','Medecine'],
    ['2','Pharmacie'],
    ['3','Chirgie dentaire'],
    ['4','MPCI'],
    ['5','SVT'],
    ['6','Science economie et de gestion'],
    ['7','Langues moderne'],
    ['8','Sociaulogie'],
    ['9','Histoire et archeologie'],
    ['10','Linguistique'],
    ['11','Geographie'],
    ['12','Anglais'],
    ['13','Almande'],
    ['14','Philosophie'],
    ['15','sphycologie'],
]

class campus(Etudiant):
    def Mettre_a_jour_compte(self, liste , ok):
        while ok != 1:
            break
        bac = float(input("Entrez la moyenne du bac:"))
        while (bac <= 0 or bac > 20):
            bac = float(input("Entrez la moyenne du bac exate:"))
        serie = str(input("Entrez la serie du bac( Ex D): "))
        while(serie != 'A' and serie != 'D' and serie !=  'C' and serie !=  'E' ):
            serie = str(input("Entrez la serie du bac exate ( Ex D): "))
        liste.append(bac)
        liste.append(serie)
        #print(liste)
        return liste

    def matieres(self, liste):
        maths= float(input("Entrez votre note en maths:"))
        pc= float(input("Entrez votre note en pc:"))
        svt= float(input("Entrez votre note en svt:"))
        fr= float(input("Entrez votre note en francais:"))
        ang= float(input("Entrez votre note en anglais:"))
        matiere = [liste[2], maths, pc, svt, fr, ang]
        #print(matiere)
        return matiere

    def eligible(self, liste):
        if liste[5] == 'A':
            if liste[4] < 13:
                return filieres
            else:
                return filieres1
        else:
            if liste[4] < 13:
                return filieres2
            else:
                return filieres3            

    def inscription(self, filiere):
        listes = []
        numb = []
        i = 9
        n = len(filiere)
        print("Chacun doit obligatoirement faire 9 choix")
        while (i !=0):
            if i == 12:
                choix = int(input(f"Entrez le numero du filere pour le {10 - i}er choix: "))
                while(choix<=0 or choix > n):
                    choix = int(input(f"Entrez le numero du filere pour le {10 - i}er choix: "))
            else:
                choix = int(input(f"Entrez le numero du filere pour le {10 - i} eme choix: "))           
                while(choix<=0 or choix > n):
                    choix = int(input(f"Entrez le numero du filere pour le {10 - i} eme choix: "))
            while choix in numb:
                print(filiere[choix -1],"est de ja pris.")
                choix = int(input(f"Entrez un autre numero d'un filere pour le {10 - i} eme choix: ")) 
            numb.append(choix)
            listes.append(filiere[choix - 1])
            if (10-i) == 1:
                listes[0].insert(9-i, '1er choix')
            else:
                listes[9-i].insert(0, f'{10-i}eme choix')
            i -= 1
        return listes


    
        

##etudiant1 = Etudiant()
etudiant1 = campus()
liste1 = etudiant1.presentation("Gnambre", "Mohamine", 18)
ok = etudiant1.compte(liste1)
liste2 = etudiant1.Mettre_a_jour_compte(liste1, ok)
matiere1 = etudiant1.matieres(liste1)
filiere = etudiant1.eligible(liste2)
print()
for x in filiere:
    print(x)
print()
listes = etudiant1.inscription(filiere)
print()
for x in listes:
    print(x, sep="\n")
    print("----------------------------------")
