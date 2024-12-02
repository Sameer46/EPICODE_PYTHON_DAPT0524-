# ESERCIZIO QUIZ TEORIA

risultati_partite = ["1","X","1","2","X","X"]
risultati_partite.append("2")
if risultati_partite(-1) == "X":
        print("l'ultima partita e' finita in pareggio")
else:
        print("Nessun Pareggio per l'ultima partita")

# ESERCIZIO QUIZ TEORIA 2

numero1= 1
numero2= 2

fibo = [1,1]
conteggio= 3
while conteggio <=10:
       prossimo_numero= numero1+numero2
       fibo.append(prossimo_numero)
       numero2=prossimo_numero
       numero1=numero2
       conteggio+=1
       print(f"I primi 10 numeri di fibonacci sono {fibo} " )


numero1= 1
numero2= 2

fibo = [1,1]
conteggio= 3
while conteggio <=10:
       prossimo_numero= numero1+numero2
       fibo.append(prossimo_numero)
       numero1=numero2
       numero2=prossimo_numero
       conteggio+=1
       print(f"I primi 10 numeri di fibonacci sono {fibo} " )

# 1 Esercizio Abbiamo la stringa: 
# nome_scuola = "Epicode" Stampare ogni carattere della stringa, 
# uno su ogni riga, utilizzando un costrutto while.


nome_scuola = "Epicode"
lunghezza=0
while len(nome_scuola)<=lunghezza:
    print(nome_scuola[lunghezza])
    lunghezza +=1



# 2 Esercizio Stampare a video tutti i numeri da 0 a 20 
# utilizzando il costrutto while. Utilizzeremo: 
# • un ciclo while • la funzione print() 
# • una variabile, che dovrà essere inizializzata 
# • una procedura di incremento

i = 0


while i <= 20:
    print(i)     
    i += 1  


# 3 Esercizio Calcolare e stampare tutte le prime 10 potenze di 2 
# (e.g., 2⁰, 2¹, 2², …) utilizzando un ciclo while


i=0
numero = 2
while i<10:
      print(numero**i)
      i+=1


# 4 Esercizio Calcolare e stampare tutte le prime N potenze 
# di 2 utilizzando un ciclo while, domandando all'utente di inserire N.

n = input()
i = 0
while i <= int(n):
      print(2**i)
      i+=1

# 5 Esercizio Calcolare e stampare tutte le potenze di 2 minori di 25000.

potenza = 1
while potenza < 25000:
    print(potenza)
    potenza *= 2

# 6 Esercizio (1/2) Abbiamo due liste, 
# una di studenti e una di corsi: 
# studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
# corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]



studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]

corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]


# Aggiungere i dati mancanti alla lista corsi, 
# sapendo che Emma segue Data Analyst Faith segue Backend Grace segue 
# Frontend Henry segue Cybersecurity Aggiungeremo i dati mancanti uno 
# alla volta con il metodo per appendere in coda alle liste, poi verificheremo
#  che sono della stessa lunghezza e se lo sono stamperemo la lista corsi.
#  Se alcuni dati sono già presenti non vanno aggiunti di nuovo.








# 7 Esercizio Scriviamo un programma che chiede in input
# all'utente una stringa e visualizza i primi 3 caratteri, 
# seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri, 
# similmente all'esercizio della lezione scorsa. Stavolta facciamo attenzione 
# a tutti i casi particolari, ovvero implementare soluzioni ad hoc per stringhe 
# di lunghezza inferiore a 6 caratteri.

stringa = input()

print(stringa[0:3], stringa[-3:], sep="...")


# 8 Esercizio Memorizza e stampa tutti i fattori di un numero dato in input.
# Esempio: • input: 150 • output: [2, 3, 5, 5]

def trova_fattori_primi(n):
    fattori = []
    # Inizia dividendo per 2 per trovare tutti i fattori di 2
    while n % 2 == 0:
        fattori.append(2)
        n = n // 2
    
    # Ora cerca i fattori dispari
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            fattori.append(i)
            n = n // i

    # Se n è un numero primo maggiore di 2, aggiungilo alla lista
    if n > 2:
        fattori.append(n)
    
    return fattori

# Input dall'utente
numero = int(input("Inserisci un numero: "))
print("Fattori primi:", trova_fattori_primi(numero))


# 9 Esercizio Abbiamo la stringa: 
# nome_scuola = "Epicode" Stampare ogni carattere della stringa,
# uno su ogni riga, utilizzando un costrutto for

nome_scuola = "Epicode"

for lettera in nome_scuola:
    print(lettera)

# 10 Esercizio Calcolare e stampare tutte le prime 10 potenze di 2 
# utilizzando un ciclo. Utilizzeremo: • un ciclo per generare i primi 10 numeri,
# e.g.: range_numerico = list()  # init num = 1  
# # init while num <= 10: range_numerico.append(num) num += 1

range_numerico = list() 
num = 0  
potenza = int(input())
while num <= 10: 
    risultato = potenza**num
    print(risultato)
    range_numerico.append(num) 
    num += 1


# 11 Esercizio Calcolare (ma non stampare) le prime N potenze di K;
# ognuna di esse andrà memorizzata in coda a una lista. 
# Alla fine, stampare la lista risultante. 
# Proviamo con diversi valori di K, oppure facciamola inserire all'utente. 
# Realizzare due versioni: • con un ciclo while, • con un ciclo for.

k = int(input("inserisci il numero per le quali vuoi le potenze"))
n = int(input("quante potenze vuoi ?"))
range = list()
rangefor = list()
i = 0 

while i < n:
    risultato = k**i
    range.append(risultato)
    i+=1

print(range)


for x in range(n):
    risultatox= k**x
    rangefor.append(risultatox)

print(rangefor)




# 12 Esercizio Abbiamo una lista con i guadagni degli ultimi 12 mesi:\
# guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] 
# usando un costrutto for, calcolare la media dei guadagni e stamparla a video.
    

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] 
somma = 0
for mese in guadagni:
    somma += mese

mesi_di_lavoro = len(guadagni)
media = somma / mesi_di_lavoro

print(f"La media dei guadagni è: {media}")




# 13 Esercizio Abbiamo una lista di parole: 
# parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"] 
# stampiamo, per ogni parola, quante volte appare la lettera "e"; 
# facciamo attenzione al fatto che appare sia maiuscola che minuscola.

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"] 

for parola in parole:
    count_e = parola.lower().count('e')
    print(f"nella {parola} la lettera e appare {count_e} volte")


# 14 Esercizio Creiamo un dizionario che assegni ad ogni proprietario la sua auto, 
# sapendo che:
# • Ada guida una Punto 
# • Ben guida una Multipla 
# • Charlie guida una Golf 
# • Debbie guida una 107 Stampiamo il dizionario per intero, 
# e poi l'auto associata a Debbie.

db = [{"nome":"Ada", "auto" :"Punto"},
        {"nome":"Ben", "auto" :"Multipla"},
        {"nome":"Charlie", "auto" :"Golf"},
        {"nome":"Debbie", "auto" :"107"}]
trovato = False

for auto in db:
    if auto['nome']=='Debbie':
        print(auto["auto"])
        trovato = True
        break


if not trovato:
    print("Debbie non e' presente")


# 15 Esercizio Abbiamo un dizionario che assegna ad ogni proprietario 
# la sua auto: 
# dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"} 
# Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto che non sono una Multipla.

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"} 

for auto in dizionario_auto.values():
    if auto != "Multipla":
        print(auto)


# 16 Esercizio Abbiamo due dizionari che assegnano ad ogni proprietario la 
# propria auto: 
# dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"} 
# nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}
# Aggiornare il dizionario dizionario_auto con i dati contenuti in nuovi_proprietari e stamparlo. Cosa è successo a Ben?


dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

print(f"il dizionario prima dell'aggiornamento {dizionario_auto}")
dizionario_auto.update(nuovi_proprietari)

print(f"il dizionario dopo l-aggiornamento {dizionario_auto}")



# 17 Esercizio Scrivere un programma che, data una lista di numeri,
# fornisca in output il minimo e il massimo (possiamo usare o meno le 
# funzioni built-in min() e max()).

numeri = [10, 5, 20, 8, 15]

minimo = numeri[0]
massimo = numeri[0]  

for numero in numeri:
    if numero < minimo:
        minimo = numero
    if numero > massimo:
        massimo = numero


print(f"Minimo: {minimo}")
print(f"Massimo: {massimo}")


# 18 Esercizio Scrivere un programma che, data una lista di numeri, 
# fornisca in output i tre numeri più grandi; gestire il caso in cui la 
# lista sia più corta di tre, e quando uno o più dei numeri selezionati sono uguali.

numeri = [10, 5, 20, 8, 15, 20, 10]


numeri_ordinati = sorted(numeri, reverse=True)


numeri_unici = []
for num in numeri_ordinati:
    if num not in numeri_unici:
        numeri_unici.append(num)
    if len(numeri_unici) == 3:
        break

# Gestire il caso in cui la lista ha meno di 3 numeri
if len(numeri_unici) < 3:
    print(f"I numeri più grandi (fino a 3) sono: {numeri_unici}")
else:
    print(f"I tre numeri più grandi sono: {numeri_unici}")


# versione piu completa con l-utente che inserici i numeri 


numeri_input = input("Inserisci una lista di numeri separati da spazio: ")

# Convertiamo l'input in una lista di numeri interi
numeri = list(map(int, numeri_input.split()))

# Verifica che ci siano almeno 3 numeri
if len(numeri) < 3:
    print("La lista deve contenere almeno 3 numeri.")
else:
    quanti_numeri = int(input("Quanti numeri vuoi selezionare? (deve essere almeno 3): "))
    
    if quanti_numeri > len(numeri):
        print(f"Ci sono solo {len(numeri)} numeri nella lista. Verranno selezionati tutti.")
        quanti_numeri = len(numeri)
    
    numeri_ordinati = sorted(numeri, reverse=True)
    
    numeri_unici = []
    for num in numeri_ordinati:
        if num not in numeri_unici:
            numeri_unici.append(num)
        if len(numeri_unici) == quanti_numeri:
            break
    
    # Stampiamo il risultato
    print(f"I {quanti_numeri} numeri più grandi sono: {numeri_unici}")

# 19 Esercizio Scrivere un programma che 
# • in input acquisisce una lista di numeri e un numero K 
# • in output, dovrà restituire la media di tutti i numeri nella lista 
# maggiori o uguali a K • se non ce ne dovesse essere nessuno,
# dovrà stampare a schermo un messaggio adeguato.

numeri_input = input("Inserisci una lista di numeri separati da spazio: ")
numeri = list(map(int, numeri_input.split()))  # Converting the string input into a list of integers

# Input the value K
K = int(input("Inserisci il numero K: "))

# Filter the list for numbers >= K
numeri_filtrati = [num for num in numeri if num >= K]

# Check if there are any numbers greater than or equal to K
if numeri_filtrati:
    # Calculate the average of the filtered numbers
    media = sum(numeri_filtrati) / len(numeri_filtrati)
    print(f"La media dei numeri maggiori o uguali a {K} è: {media}")
else:
    # If no numbers are >= K, print an appropriate message
    print(f"Non ci sono numeri maggiori o uguali a {K} nella lista.")

# 20 Esercizio Scrivere un programma che, data una lista di numeri, 
# come output stamperà lo stesso numero di asterischi su righe diverse, 
# ottenendo una semplice visualizzazione grafica Esempio, 
# supponendo di avere il seguente input: numeri = [5, 2, 3, 4] 
# L'output sarà: ***** ** *** ****   





# 21 Esercizio Abbiamo una lista di codici fiscali: 
# lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
# • trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine stamparla; 
# • inoltre, per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al cognome.

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

cf_95=[]

for cf in lista_cf:
    if "95" in cf:
        cf_95.append(cf)

print("Codici fiscali che contengono '95':")
print(cf_95)


for cf in cf_95:
    cognome = cf[:3]  # I primi 3 caratteri sono il cognome
    nome = cf[3:6]  # I successivi 3 caratteri sono il nome
    print(f"Codice Fiscale: {cf} -> Cognome: {cognome}, Nome: {nome}")



# 22 Esercizio Abbiamo tre liste della stessa lunghezza, dove ogni elemento nella
# medesima posizione si riferisce ai dati dello stesso studente: 
# studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
# corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"] 
# edizioni = [1, 2, 3, 2, 2, 1, 3, 3] 
# • Stampare a video tutti e soli gli studenti che frequentano una prima edizione;
# non tutti i dati potrebbero essere necessari. 
# • Riuscite a vedere una similarità con la logica che si usa in SQL e le tabelle relazionali?
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]


for i in range(len(studenti)):
    if edizioni[i] == 1:  # Controlliamo se l'edizione è la prima
        print(studenti[i])  # Stampiamo il nome dello studente



# 23 Esercizio Abbiamo una lista di stringhe di prezzi in dollari, 
# che erroneamente sono stati scritti con il simbolo dell'euro: 
# prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"] 
# cambiare il simbolo dell'euro (€) in quello del dollaro ($) 
# per ogni stringa nella lista; il risultato sarà memorizzato in un'altra lista.

prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]

prezzi_in_dollari = []

for prezzo in prezzi:
    # Sostituire il simbolo dell'euro (€) con il simbolo del dollaro ($)
    prezzo_in_dollaro = prezzo.replace("€", "$")
    # Aggiungere il prezzo modificato alla nuova lista
    prezzi_in_dollari.append(prezzo_in_dollaro)

# Stampare la lista dei prezzi in dollari
print(prezzi_in_dollari)



# 24 Esercizio Abbiamo una lista di studenti: 
# studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]
# vogliamo dividere gli studenti in due squadre per un campionato di Uno nel seguente modo:
# selezioneremo i nomi in posizione pari per un squadra, 
# e i nomi in posizione dispari per l'altra. Creiamo due liste per ogni squadra, 
# e alla fine visualizziamole.



studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]

squadra1 = studenti[::2]

squadra2 = studenti[1::2]

print("Squadra 1 (posizioni pari):", squadra1)
print("Squadra 2 (posizioni dispari):", squadra2)



#25 Esercizio Abbiamo una lista con i guadagni degli ultimi 12 mesi 
# (supponiamo da Gennaio a Dicembre): 
# guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] 
# dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con la media dei guadagni precedenti,
# e specificare nell'output se il guadagno attuale è maggiore o minore della media dei precedenti.
# Esempio di un possibile output: Mese 1: 100 € Mese 2: 90 € (media prec: 100 € - il guadagno attuale è minore) Mese 3: 70 € (media prec: 95 € - il guadagno attuale è minore)
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]


for i in range(1, len(guadagni)):  # Inizia dal mese 2 (indice 1)
    mese_corrente = guadagni[i]
    guadagni_precedenti = guadagni[:i]  # Guadagni precedenti al mese corrente
    media_precedenti = sum(guadagni_precedenti) / len(guadagni_precedenti)  # Calcola la media dei guadagni precedenti
    
    if mese_corrente > media_precedenti:
        risultato = "il guadagno attuale è maggiore"
    else:
        risultato = "il guadagno attuale è minore"
    
    print(f"Mese {i+1}: {mese_corrente} € (media prec: {media_precedenti:.2f} €) - {risultato}")









