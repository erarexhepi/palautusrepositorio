# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

<<<<<<< HEAD
logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")  # muutos bugikorjaus-branchissa
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}")  # muutos bugikorjaus-branchissa
=======
logger("aloitetaan ohjelma")  # yhdistetty muutos

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}")  # muutos mainissa
print(f"{x} - {y} = {erotus(x, y)}")  # muutos mainissa
>>>>>>> main

logger("lopetetaan ohjelma")
print("goodbye!")
