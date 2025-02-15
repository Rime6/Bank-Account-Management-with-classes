"""Définissez une classe CompteBancaire(), qui permette 
d’instancier des objets tels que compte1, compte2, etc. 
Le constructeur de cette classe initialisera deux 
attributs d’instance nom et solde, avec les valeurs par 
défaut ’Dupont’ et 1000.
 • Trois autres méthodes seront définies :
 • depot(somme) permettra d’ajouter une certaine somme 
au solde ;
 • retrait(somme) permettra de retirer une certaine 
somme du solde ;
 • affiche() permettra d’afficher le nom du titulaire et le 
solde de son compte.
"""

class CompteBancaire(object):
    def __init__(self, nom="Dupont", solde=1000):
        self.nom = nom
        self.solde = solde
    def depot(self, somme):
        self.solde += somme
    def retrait(self, somme):
        self.solde -= somme
    def affiche(self):
        print(f"Le solde du compte bancaire de {self.nom} est de {self.solde} dollars.")
compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()

class CompteEpargne(CompteBancaire):
    def __init__(self, nom="Dupont", solde=1000):
        self.nom = nom
        self.solde = solde
        self.taux = 0.3
    def changeTaux(self, valeur):
        self.taux = valeur
    def capitalisation(self, nombreMois):
        self.nombreMois = nombreMois
        for m in range(self.nombreMois):
            self.solde *= ((100+self.taux)/100)
        print(f"Capitalisation sur {self.nombreMois} mois au taux mensuel de {self.taux}%")
    
c1 = CompteEpargne('Duvivier', 600)
c1.depot(350)
c1.affiche()
c1.capitalisation(12)
c1.affiche()
c1.changeTaux(.5)
c1.capitalisation(12)
c1.affiche()
