# 1 Esercizio Abbiamo una lista di liste: 
# mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]] 
# Che tipo di struttura dati o matematica potrebbe rappresentare? 
# Notare che tutte le liste "interne" sono della stessa dimensione 
# Come facciamo per accedere ad un elemento in particolare?

mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

# 2 Per accedere a un elemento specifico in una lista di liste come questa,
#  dobbiamo fornire due indici:
#Il primo indice indica la riga.
# Il secondo indice indica la colonna all'interno di quella riga.

x= 1
y= 2

print(mat[x][y])


# 2 Esercizio Importiamo il modulo math e proviamo a usare le funzioni 
# .sin() .cos() .factorial() e la variabile .pi la riconoscete?

import math

print(math.pi)

n = 5
print("fattoriale")
print(math.factorial(n))



x = math.pi  # 180 gradi in radianti
print(math.cos(x))  # Risultato: -1.0


seno = math.sin(math.pi / 4)
coseno = math.cos(math.pi / 4)

# Calcolare il fattoriale di 6
fattoriale = math.factorial(6)

# Stampare i risultati
print("Seno di π/4:", seno)
print("Coseno di π/4:", coseno)
print("Fattoriale di 6:", fattoriale)
print("Valore di pi greco:", math.pi)


# 3 Esercizio Proviamo a eseguire math.degrees(math.pi) 
# Qual è e cosa significa il risultato? Per saperne di più su questa 
# funzione possiamo usare help(math.degrees)

# serve per convertire un angolo espresso in radianti in gradi.

print(math.degrees(math.pi) )



# 4 Esercizio L'azienda Object SpA ha creato una lista di quanti oggetti 
# ha venduto ogni mese nell'ultimo anno: 
# lst = [2000, 5500, 7200, 4320, 1280, 1900, 2500, 3900, 6410, 8150, 7100, 5350]
# trasformiamola in un array NumPy (casting): lst = np.array(lst)
# e rispondiamo alle domande del CEO della Object SpA: 
# • qual è stata la vendita massima mensile? E quella minima? 
# • quali sono le vendite mensili maggiori di 4999 oggetti? E quante ne sono? 
# • quali sono le vendite minori di 3000 oggetti? 
# 5 • in media quanti oggetti sono stati venduti al mese?

import numpy as np

lst = [2000, 5500, 7200, 4320, 1280, 1900, 2500, 3900, 6410, 8150, 7100, 5350]


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


list_month = [(months[i], lst[i]) for i in range(len(months))]

#convert in np array

nparray= np.array([value for month, value in list_month])

max_value= np.max(nparray)
max_month_index= np.argmax(nparray)
max_month = list_month[max_month_index][0]


min_value = np.min(nparray)
min_month_index=  np.argmin(nparray)
min_month = list_month[min_month_index][0]

# 1. Filtrare vendite maggiori di 4999 usando NumPy
mask_maggiori_4999 = nparray > 4999
vendite_maggiori_4999 = nparray[mask_maggiori_4999]
vendite_maggiori_4999 = [list_month[i] for i in range(len(list_month)) if mask_maggiori_4999[i]]

#2 Filtro vendite minori di 3000 
mask_maggiori_3000 = nparray <3000
vendite_minori_3000 = nparray[mask_maggiori_3000]
vendite_minori_3000= [ list_month[i] for i in range(len(list_month)) if mask_maggiori_3000[i]]

media_vendite_mensili = np.mean(nparray)



print(f"Maximum value is {max_value}, which corresponds to {max_month})")
print(f"Minimum value is {min_value}, which corresponds to {min_month})")
print("")
print("")
print("")
print("Vendite maggiori di 4999 oggetti:")
for month, value in vendite_maggiori_4999:
    print(f"{month}: {value} oggetti")
print("")
print("")
print("")
print("Vendite minori di 3000 oggetti:")
for month, value in vendite_minori_3000:
    print(f"{month}: {value} oggetti")


print(f"Media mensile delle vendite: {media_vendite_mensili:.2f} oggetti")





# 5 Esercizio Consideriamo il seguente dizionario: 
# fatturati_dict = {1997: 12_000, 1998: 15_000, 1999: 20_000, 2000: 23_000, 2001: 25_000, 2002: 17_000, 2003: 14_000, 2004: 21_000} 
# Consideriamo ora la seguente Series: fatturati_series = pd.Series([12_000, 15_000, 20_000, 23_000, 25_000, 17_000, 14_000, 21_000], 
# index=range(1997, 2005)) Possiamo accedere alle stesse informazioni nello 
# stesso modo: fatturati_dict[1997] fatturati_series[1997] Dunque qual è la 
# differenza tra i due tipi di dato? Cosa potremmo fare con la Series che non 
# possiamo fare con il dizionario?

import pandas as pd

fatturati_dict = {1997: 12_000, 1998: 15_000, 1999: 20_000, 2000: 23_000, 2001: 25_000, 2002: 17_000, 2003: 14_000, 2004: 21_000} 
fatturati_series = pd.Series([12_000, 15_000, 20_000, 23_000, 25_000, 17_000, 14_000, 21_000],index=range(1997, 2005))

#sono simili ma sulla serie di pandas io posso effeturare operazione aggiunitve come 
# somma .sum .mean mentre su dict non posso effetturare queste opeazioni
# posso effetuare anche il filtro come su numpy fatturati_series[ fatturati_series > 20000]

# usiamo list() perche stiamo operando su un dizionario e .item() permette di accedere facilmente a tutte le coppie di chiavi 
# columns ci permette di assegnare il nome alle colonne 
fatturati_df = pd.DataFrame(list(fatturati_dict.items()), columns=['Anno', 'Fatturato'])
# .set_index ci permette di riordinarle in ordine tempolare


#fatturati_df.set_index('Anno', inplace=True)
#pd.set_option('display.colheader_justify', 'left')  

print(fatturati_df)




# 6 Esercizio L'azienda Object SpA ha un dataset con tutti gli stipendi dei 
# dipendenti, memorizzato in un ndarray: import numpy as np 
# stipendi = np.array( [100, 200, 300, 400, 500,  600, 700, 800, 900, 1000] ) 
# L'azienda ci chiede di raddoppiare tutti gli stipendi; facciamolo in due modi:
# • con un ciclo for 7 • con il masking


import numpy as np

stipendi = np.array( [100, 200, 300, 400, 500,  600, 700, 800, 900, 1000] ) 
stipendi_old= np.copy(stipendi)
stipendi_masking = np.copy(stipendi) #cosi non fanno riferimento allo stesso oggetto in memoria

for i in range(len(stipendi)):
    stipendi[i]= stipendi[i]*2


stipendi_masking*= 2

print("Stipendi raddopiati tramire l'uso del ciclo for ",stipendi)
print("Stipendi raddopaito con il masking ",stipendi_masking)



