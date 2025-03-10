# come testare un modulo
# e creo delle stampe
from voto.voto import Voto, Libretto
v1 = Voto("Trasfigurazioni", 24, 2022-2-13, True) # lo zero nel mese non va con questa versione
v2 = Voto("Pozioni", 30, 2022-2-13, True)
v3 = Voto("Difewsa", 27, 2022-2-13, False)

myLib = Libretto(None, [v1, v2])
print(myLib)
myLib.append(v3)
print(myLib)

