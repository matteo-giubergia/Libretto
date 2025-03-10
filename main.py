# Harry = ["Harry", "Potter", 11,
#          "capelli castani", "occhi azzurri",
#          "Grifondoro", ""]
#
# print(Harry)
# print("Il nome è ", Harry[0])
#
# Harry[6] = "Expecto Patronum"
#
# print(Harry)
#
# Ron = ["Ron", "Weasley", 11,
#          "capelli rossi", "occhi marroni",
#          "Grifondoro", ""]
#
# Grifondoro = [Harry, Ron]
from dataclasses import dataclass
# import voto # importo un solo nome del modulo  e poi accedo alle classi
# con la notazione voto.Voto, voto.Libretto
from voto.voto import Voto,Libretto
import sys
print(sys.path)


# from voto import * importa tutto
from scuola import Student, Teacher, Casa, Scuola
class Person:
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, incantesimo="Non ancora definito"):
        self.nome = nome
        self._cognome = cognome
        self.eta = eta
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.__prova = None
        self.incantesimo = incantesimo

    def __str__(self):
        return f"Person: {self.nome} {self._cognome} \n"

    @property
    def cognome(self): # eq. GETTER
        return self._cognome
    @cognome.setter
    def cognome(self, value): # eq. SETTER
        #CONTROLLI per verificare che value sia compativile con _cognome
        self._cognome = value





# Grifondoro
Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
Hermione = Student(nome="Hermione", cognome="Granger", eta=11, capelli="castani", occhi="castani", casa="Grifondoro", animale="gatto", incantesimo="Wingardium Leviosa")
Ron = Student(nome="Ron", cognome="Weasley", eta=11, capelli="rossi", occhi="azzurri", casa="Grifondoro", animale="topo")
Neville = Student(nome="Neville", cognome="Paciock", eta=11, capelli="castani", occhi="castani", casa="Grifondoro", animale="rospo")
Ginny = Student(nome="Ginny", cognome="Weasley", eta=10, capelli="rossi", occhi="castani", casa="Grifondoro", animale="gatto")
Sirius = Person(nome="Sirius", cognome="Black", eta=36, capelli="neri", occhi="grigi", casa="Grifondoro") #Sirius non è ne studente ne professore ad Hogwarts
Remus = Teacher(nome="Remus", cognome="Lupin", eta=36, capelli="castani", occhi="verdi", casa="Grifondoro", materia="Difesa contro le arti oscure")
Minerva = Teacher(nome="Minerva", cognome="McGranitt", eta=70, capelli="neri", occhi="verdi", casa="Grifondoro", materia="Trasfigurazione", incantesimo="Trasfigurazione Animale")
Albus = Teacher(nome="Albus", cognome="Silente", eta=115, capelli="argento", occhi="azzurri", casa="Grifondoro", materia="Preside")
Rubeus = Person(nome="Rubeus", cognome="Hagrid", eta=60, capelli="neri", occhi="neri", casa="Grifondoro") #Rubeus non è ne studente ne professore ad Hogwarts
James = Person(nome="James", cognome="Potter", eta=23, capelli="neri", occhi="castani", casa="Grifondoro")
Lily = Person(nome="Lily", cognome="Evans", eta=23, capelli="rosso", occhi="verdi", casa="Grifondoro")
Fred = Student(nome = "Fred", cognome = "Weasley", eta = 16, capelli = "rossi", occhi = "castani", casa = "Grifondoro", animale="nessuno")
George = Student(nome = "George", cognome = "Weasley", eta = 16, capelli = "rossi", occhi = "castani", casa = "Grifondoro", animale="nessuno")

# Serpeverde
Draco = Student(nome="Draco", cognome="Malfoy", eta=11, capelli="biondi", occhi="grigi", casa="Serpeverde", animale="nessuno")
Severus = Teacher(nome="Severus", cognome="Snape", eta=45, capelli="neri", occhi="neri", casa="Serpeverde", materia="Pozioni", incantesimo="Sectumsempra")
Horace = Teacher(nome="Horace", cognome="Lumacorno", eta=65, capelli="brizzolati", occhi="verdi", casa="Serpeverde", materia="Pozioni", )
Bellatrix = Person(nome="Bellatrix", cognome="Lestrange", eta=47, capelli="neri", occhi="neri", casa="Serpeverde") #Bellatrix non è ne studente ne professore ad Hogwarts
Lucius = Person(nome="Lucius", cognome="Malfoy", eta=42, capelli="biondi", occhi="grigi", casa="Serpeverde") #Lucius non è ne studente ne professore ad Hogwarts
Narcissa = Person(nome="Narcissa", cognome="Malfoy", eta=41, capelli="biondi", occhi="azzurri", casa="Serpeverde") #Narcissa non è ne studente ne professore ad Hogwarts
Pansy = Student(nome="Pansy", cognome="Parkinson", eta=12, capelli="neri", occhi="castani", casa="Serpeverde", animale="nessuno")
Blaise = Student(nome = "Blaise", cognome = "Zabini", eta = 12, capelli = "neri", occhi = "castani", casa = "Serpeverde", animale="nessuno")
Tom_Riddle = Student(nome="Tom", cognome="Riddle", eta=16, capelli="neri", occhi="neri", casa="Serpeverde", animale="serpente", incantesimo="Avada Kedavra")

# Corvonero
Luna = Student(nome="Luna", cognome="Lovegood", eta=11, capelli="biondi", occhi="azzurri", casa="Corvonero", animale="nessuno")
Cho = Student(nome="Cho", cognome="Chang", eta=12, capelli="neri", occhi="castani", casa="Corvonero", animale="nessuno")
Gilderoy = Teacher(nome="Gilderoy", cognome="Allock", eta=33, capelli="biondi", occhi="azzurri", casa="Corvonero", materia="Difesa contro le Arti Oscure", incantesimo="Oblivion")
Filius = Teacher(nome="Filius", cognome="Vitious", eta=150, capelli="bianchi", occhi="azzurri", casa="Corvonero", materia="Incantesimi", incantesimo="Wingardium Leviosa")
Xenophilius = Person(nome="Xenophilius", cognome="Lovegood", eta=49, capelli="bianchi", occhi="azzurri", casa="Corvonero") #Xenophilius non è ne studente ne professore ad Hogwarts
Padma = Student(nome="Padma", cognome="Patil", eta=13, capelli="neri", occhi="castani", casa="Corvonero", animale="nessuno")
Michael = Student(nome = "Michael", cognome = "Corner", eta = 13, capelli = "neri", occhi = "castani", casa = "Corvonero", animale="nessuno")

# Tassorosso
Cedric = Student(nome="Cedric", cognome="Diggory", eta=16, capelli="castani", occhi="grigi", casa="Tassorosso", animale="nessuno")
Pomona = Teacher(nome="Pomona", cognome="Sprout", eta=60, capelli="grigi", occhi="castani", casa="Tassorosso", materia="Erbologia")
Hannah = Student(nome="Hannah", cognome="Abbott", eta=12, capelli="biondi", occhi="azzurri", casa="Tassorosso", animale="nessuno")
Ernest = Student(nome="Ernest", cognome="Macmillan", eta=13, capelli="biondi", occhi="castani", casa="Tassorosso", animale="nessuno")
Susan = Student(nome="Susan", cognome=" Bones", eta=12, capelli="rossi", occhi="verdi", casa="Tassorosso", animale="nessuno")
Ted = Person(nome="Ted", cognome="Tonks", eta=24, capelli="castano", occhi="neri", casa="Tassorosso") #Ted non è ne studente ne professore ad Hogwarts

print(Harry, Ron, Susan, Xenophilius, Remus)

personaggi = [Harry, Hermione, Ron, Neville, Ginny, Sirius, Remus, Minerva, Albus, Rubeus, James, Lily, Fred, George,
              Draco, Severus, Horace, Bellatrix, Lucius, Narcissa, Pansy, Blaise, Luna, Cho, Gilderoy, Filius, Xenophilius,
              Padma, Michael, Cedric, Pomona, Hannah, Ernest, Susan, Ted]
# print(Lily._cognome) # NOOOO!

# print(Lily._Person__prova) NOOOOOOO!
grifondoro = Casa("Grifondoro", [])
tassoRosso = Casa("Tassorosso", [])
corvoNero = Casa("Corvonero", [])
serpeVerde = Casa("Serpeverde", [])
for p in personaggi:
   # if p.casa == grifondoro.nome & isinstance(p, Student):
   #     grifondoro.addStudente(p)

    #if p.casa == corvoNero.nome & isinstance(p, Student):
     #   corvoNero.addStudente(p)

    #if p.casa == serpeVerde.nome & isinstance(p, Student):
     #   serpeVerde.addStudente(p)

    #if p.casa == tassoRosso.nome & isinstance(p, Student):
     #   tassoRosso.addStudente(p)
   match p.casa:
     case "Grifondoro":
           grifondoro.addStudente(p)
     case "Tassorosso":
           tassoRosso.addStudente(p)
     case "Corvonero":
           corvoNero.addStudente(p)
     case "Serpeverde":
           serpeVerde.addStudente(p)
     case _:
         print(f"Jumping {p}")

v1 = Voto("Trasfigurazioni", 24, 2022-2-13, True) # lo zero nel mese non va con questa versione
v2 = Voto("Pozioni", 30, 2022-2-13, True)
v3 = Voto("Difesa", 27, 2022-2-13, False)

myLib = Libretto(Harry, [v1, v2])
print(myLib)
myLib.append(v3)
print(grifondoro)
print(tassoRosso)
print(serpeVerde)
print(corvoNero)

