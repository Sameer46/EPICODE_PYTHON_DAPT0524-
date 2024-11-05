# 1 Esercizio Individuiamo tre task di qualsiasi tipo (fare la spesa, studiare un concetto, riempire il serbatoio dell'auto, 
# acquistare uno snack da un distributore automatico, o qualunque altra cosa); Scriviamo un algoritmo (in forma testuale), 
# cioè i passi necessari, per ognuno dei task selezionati.

lista_spesa = ["sale", "uova", "pasta"]

print("Andiamo al Supermercato")

print("Prendere il carrello")

for articolo in lista_spesa:
    print(f"Trovare {articolo} nel supermercato")

    print(f"Mettere {articolo} nel carello")

print("Andare alla cassa")

print("Pagare")

print("Tornare a casa")


#2 Esercizio Abbiamo 25 studenti; memorizzare questo dato in una variabile.
#  Utilizzeremo: • l'operatore di assegnazione =


studenti = 25
print(f"La classe è composta da {studenti} studenti")

studenti += 3


print(f"La classe è composta da {studenti} studenti")


#3 Esercizio Abbiamo 25 studenti; memorizzare questo dato in una variabile. 
# Arrivano altri 3 studenti; memorizzare questo dato in un'altra variabile.
# Creare un'altra variabile ancora che conterrà la somma delle prime due, 
# poi stamparla a video. Utilizzeremo: • la funzione print() per stampare a
# video

studenti= 25

nuovistudenti= 3

totale_studenti = studenti + nuovistudenti

print(f"Il numero totale di studenti è {totale_studenti}")


# 4 Esercizio Creare una variabile che contiene la stringa "Epicode", 
# quindi stamparla a video.


testo = "Epicode"

print(testo)

#5 Esercizio Abbiamo la variabile: x = 10 Incrementarla di
# 2 e poi moltiplicarla per 3 Usare due metodi diversi (ad esempio,
# uno utilizzando gli operatori di assegnazione, e uno senza)

x= 10
x+= 2
x*=3
print(f"Il risultato finale (metodo 1) è {x}")



# Secondo metodo 
y = 10
y = y + 2
y = y * 3

print(f"Il risultato finale (metodo 2) è {x}")


#Esercizio Verificare, per ognuna delle seguenti stringhe,
#  se il numero di caratteri è compreso tra 5 e 8: 
# • str1 = "Windows" • str2 = "Excel" • str3 = "Powerpoint" • str4 = "Word"


str1 = "Windows"
str2 = "Excel"
str3 = "Powerpoint"
str4 = "Word"

def verifica_lunghezza(stringa):
    return 5 <= len(stringa) <= 8

print(f"str1 ('{str1}') ha una lunghezza tra 5 e 8? {verifica_lunghezza(str1)}")
print(f"str2 ('{str2}') ha una lunghezza tra 5 e 8? {verifica_lunghezza(str2)}")
print(f"str3 ('{str3}') ha una lunghezza tra 5 e 8? {verifica_lunghezza(str3)}")
print(f"str4 ('{str4}') ha una lunghezza tra 5 e 8? {verifica_lunghezza(str4)}")

#secondo metodo

array = ["Windows", "Excel", "Powerpoint", "Word"]

for parole in array:
    if 5 <= len(parole) <= 8:
        print(f"La stringa '{parole}' ha una lunghezza tra 5 e 8 caratteri: True")
    else:
        print(f"La stringa '{parole}' ha una lunghezza tra 5 e 8 caratteri: False")


#Esercizio Calcolare e stampare a video quanti secondi ci sono in un anno non bisestile.

print(f"Ci sono {365 * 24 * 60 * 60} secondi in un anno non bisestile.")



#Esercizio Abbiamo la seguente stringa: my_string = "I am studying Python"
# • Trasformarla in modo che tutti i caratteri siano maiuscoli (uppercase) 
# • Trasformarla in modo che tutti i caratteri siano minuscoli (lowercase) 
# • Sostituire la sottostringa "Python" con la stringa "a lot" 
# • Usare il metodo .strip(); cambia qualcosa? Perché?

my_string = "I am studying Python "


uppercase_string = my_string.upper()
print("Maiuscolo:", uppercase_string)

lowercase_string = my_string.lower()
print("Minuscolo:", lowercase_string)

replaced_string = my_string.replace("Python", "a lot")
print("Sostituzione:", replaced_string)


#Questo metodo rimuove gli spazi bianchi all'inizio e alla fine della stringa.
#Se non ci sono spazi bianchi, la stringa rimarrà invariata.
stripped_string = my_string.strip()
print("Stringa con strip:", stripped_string)

print("Originale:", repr(my_string))
print("Dopo strip:", repr(stripped_string))

