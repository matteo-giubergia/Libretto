from main import Person


class Student(Person):
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, animale, incantesimo="Non ancora definito"): # def __init__(self, *args) oppure __init__(self, **args)
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo) #accetta piu argomenti e li mette in una lista; col secodno modo usa le mappe
        self.animale = animale

    def __str__(self):
        return f"Student: {self.nome} - {self._cognome} - {self.casa} \n "

    def __repr__(self):
        return f"Student(nome, cognome, eta, capelli, occhi, casa, animale)"

    def prettyPrint(self):
        print("Voglio stampare meglio")

class Teacher(Person):
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, materia, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.materia = materia
    def __str__(self):
        return f"Teacher: {self.nome} - {self._cognome} - {self.materia} \n "
class Casa:
    def __init__(self, nome, studenti = [] ):
        self.nome = nome
        self.studenti = studenti

    def addStudente(self, studente):
        self.studenti.append(studente) # --> [ x,x,x [s1, s2]] aggiunge anche liste
        #self.studenti.extend(studente) # --> [ x,x,x, s1, s2 ]

    def __str__(self):
        if len(self.studenti) == 0:
            return f"La casa {self.nome} è vuota."

        mystr = f"\n Lista degli studenti iscritti alla casa {self.nome} \n"
        for s in self.studenti:
            mystr += str(s)

        return mystr
class Scuola:
    def __init__(self, nome, casa):
        self.casa = casa
    def __str__(self):
        mystr = ""
        for c in self.casa:
            mystr += str(c)
        return mystr