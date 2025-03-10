# costruiamo il modulo voto
# che dovrebbe contenere solo le def e non eseguire codice
# per non creare casini quando la importo
from dataclasses import dataclass


@dataclass #decoratore che va a chiamare una funzione (importata automaticamente)
                # e costruisce una classe che contiene i metodi minimmi indispensabili
                # repr, init, eq, hash
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto):
        self.voti.append(voto)
    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario} \n"
        for v in self.voti:
            mystr += str(v)+"\n"
        return mystr

    def __len__(self):
        return len(self.voti)
    def calcolaMedia(self):
        """restituisce la media dei voti attualmente presente nel libretto
            :return valore numerico della media, oppure Valueerror
        """
       # media = sommaVoti / numeroEsami
       #v = []
       #for v in self.voti:
       #   v.append(v.punteggio)
        if len(self.voti) == 0 :
            raise ValueError("Attenzione, lista esami Vuota!!")
        v = [v1.punteggio for v1 in self.voti] # ciclo sui voti e vado a prendere il punteggio
        return sum(v)/len(v) # non va bene se la lista è vuota

    def getVotiByPunti(self, punti, lode):
        """
        restituisce una lista di esami con punteggio uguale a punti
        :param punti: variabile di tipo intero che rappresenta il punteggio
        :param lode: boolean indica se presente la lode
        :return: lista di voti
        """
        votiFiltrati = []
        for v in self.voti:
            if v.punteggio == punti & v.lode == lode: # il dataclass già ha in metodo __eq__
                votiFiltrati.append(v)
        return votiFiltrati
    def getVotoByNameMateria(self, nome):
        for v in self.voti :
            if v.materia == nome :
                return v


def testVoto():
    v1 = Voto("Trasfigurazioni", 24, 2022 - 2 - 13, True)  # lo zero nel mese non va con questa versione
    v2 = Voto("Pozioni", 30, 2022 - 2 - 13, True)
    v3 = Voto("Difewsa", 27, 2022 - 2 - 13, False)

    myLib = Libretto(None, [v1, v2])
    print(myLib)
    myLib.append(v3)

# crea variabile __name__ quando eseguo un modulo che può avere due valori
if __name__ == "__main__":  # per capire se il modulo che esguo un file che importa voto allora vale voto se invece non lo importo e lo eseguo allora name vale name
    testVoto()
# cosi uso queste stampe solo se uso il modulo da solo senza che sia importato in un'altro modulo;
# si usa epr testare e poter mettere le print senzache diano fastidio quando lo si esegue importandolo

'''
class Voto:
    # si presta ad essere una dataclasse
    def __init__(self, materia, punteggio, data, lode):
        if punteggio == 30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = lode
        elif punteggio <30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = False
        else:
            raise  ValueError(f"Attenzione, lode non applicabile")
    def __str__(self):
        if self.lode:
            return f"in {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"in {self.materia} hai preso {self.punteggio} il {self.data}"
'''