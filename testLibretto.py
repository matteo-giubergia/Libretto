from scuola import Student
from voto.voto import Voto,Libretto

Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
myLib = Libretto(Harry, [])
#v1 = Voto
#v2 = Voto()
#myLib.append()
#myLib.append()

myLib.append(Voto("Pozioni", 21, 2022-6-13, False)) # meglio fare cosi
myLib.calcolaMedia()


votiFiltrati = myLib.getVotiByPunti(21, False)

print(votiFiltrati[0])


votoTrasfigurazione = myLib.getVotoByNameMateria("Pozioni")
if votoTrasfigurazione is None:
    print("Voto non trovato")
else:
    print(votoTrasfigurazione)