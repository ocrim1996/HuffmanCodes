# HuffmanCodes

Per eseguire il codice è necessario avere il file Python `Node.py`, nel quale viene definita la classe Node e i suoi relativi metodi. Per importarlo nel progetto non è necessario eseguire nessuna azione particolare in quanto viene importato automaticamente nel codice tramite lo statement:

```python
from Node import *
```

L’unica accortezza è quella di mettere entrambi i file Python nella stessa cartella.

Inoltre è stata utilizzata la seguente libreria:

- `numpy`

Una volta eseguito il codice, l’utente può scegliere tra una lista di funzioni disponibili che vengono stampate a schermo, semplicemente inserendo il numero corrispondente.

![Schermata 2021-05-27 alle 23.35.50.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/D4A4FBF0-616F-47A6-AF5C-E38238449640/F49BFFFC-A8F6-4638-BE5B-E1AF102904C3_2/Schermata%202021-05-27%20alle%2023.35.50.png)

Mostriamo dunque adesso una breve descrizione delle seguenti funzioni e cosa richiedono in input.

## 1. Generare un codice istantaneo ottimo

Funzione che serve per generare un codice istantaneo (o *prefix-free*) ottimo.

All’utente viene richiesto in input:

- il **numero di lettere** dell’alfabeto inglese da utilizzare.

Dato il numero di lettere ad ognuna viene assegnata una propria distribuzione di probabilità, tramite la seguente funzione:

```python
def alphabet_distribution(n_letter, choice):
	'''some code'''
	return distribution
```

Quando viene chiamato questo metodo l'utente può decidere se assegnare all'alfabeto la distribuzione dell'alfabeto inglese oppure una distribuzione randomica generata tramite `random.rand(…)`, nel seguente modo:

![Schermata 2021-05-28 alle 17.28.52.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/D4A4FBF0-616F-47A6-AF5C-E38238449640/F2A38743-6D21-4305-882F-D28238C360CC_2/Schermata%202021-05-28%20alle%2017.28.52.png)

Una volta selezionata una delle due opzioni, la funzione restituisce in output il **codice di Huffman** generato, il quale è un codice *prefix-free* ottimo.

Nel codice la funzione che genera il codice di Huffman prendendo in input i nodi è la seguente:

```python
def huffman_code(nodes):
	'''some code'''
	return code
```

Mentre la funzione che imposta i valori dei parametri in input è:

```python
def set_huffman_code():
	'''some code'''
```

### Test di Esempio

Generare un codice prefix-free ottimo composto dalle prime 10 lettere dell’alfabeto, utilizzando come distribuzione per ogni singola lettera quella relativa all’alfabeto inglese:

![Schermata 2021-05-28 alle 17.48.18.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/D4A4FBF0-616F-47A6-AF5C-E38238449640/F4413F57-B27E-4346-A5E5-35D23AFC28AF_2/Schermata%202021-05-28%20alle%2017.48.18.png)

![Schermata 2021-05-28 alle 17.48.36.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/D4A4FBF0-616F-47A6-AF5C-E38238449640/CD392CEC-607A-4E21-BEBA-C89C528465B7_2/Schermata%202021-05-28%20alle%2017.48.36.png)

## 2. Decoding

Funzione che implementa una procedura di decodifica.

La funzione chiede all’utente di inserire il numero di lettere dell’alfabeto per poter andare a genererare un codice *prefix-free*.

Dopo aver inserito il numero di lettere, sempre all’utente viene chiesto che tipo di codice prefix-free vuole generare:

1. Un codice di Huffman
2. Un generico codice prefix-free ottenuto tramite una personale scelta implementativa.

![Schermata 2021-05-29 alle 15.17.01.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/D4A4FBF0-616F-47A6-AF5C-E38238449640/038EFC6A-6B58-4F98-9BAF-67B47C3124CB_2/Schermata%202021-05-29%20alle%2015.17.01.png)

Se viene scelto di generare un codice di Huffman, all’utente viene inoltre richiesto, come nel caso del **punto 1.**, con quale distribuzione si vuole generare tale codice:

![Schermata 2021-05-29 alle 15.40.01.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/D4A4FBF0-616F-47A6-AF5C-E38238449640/B2E82710-B17A-4193-B055-09DEEE2B3D07_2/Schermata%202021-05-29%20alle%2015.40.01.png)

Una volta generato il codice è possibile passare alla decodifica di una stringa binaria.

Nel codice la funzione che esegue la procedura di decodifica è la seguente:

```python
def binary_strign_decoding(prefix_free_code, binary_string):
	'''some code'''
	return plaintext
```

Mentre la funzione che imposta i valori dei parametri in input è:

```python
def set_decoding():
	'''some code'''
```

### Test di Esempio

Decodificare la parola “***edifici***” con un codice di Huffman composto dalle prime 10 lettere dell'alfabeto, generato utilizzando una distribuzione casuale per ogni singola lettera:

![Schermata 2021-05-31 alle 12.06.01.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/D4A4FBF0-616F-47A6-AF5C-E38238449640/26DC6FFA-E9FB-442F-931A-14E2991CEA12_2/Schermata%202021-05-31%20alle%2012.06.01.png)

![Schermata 2021-05-31 alle 12.06.42.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/D4A4FBF0-616F-47A6-AF5C-E38238449640/5A3FCCC8-CE6C-42CB-B391-F592350EEAEE_2/Schermata%202021-05-31%20alle%2012.06.42.png)

![Schermata 2021-05-31 alle 12.07.06.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/D4A4FBF0-616F-47A6-AF5C-E38238449640/DA072DE0-F348-42E0-97FE-B7AE0AB1E88E_2/Schermata%202021-05-31%20alle%2012.07.06.png)

### Osservazione

Se l’utente sceglie di utilizzare un generico codice prefix-free (“*Generic Prefix-Free Code*”) come codice per il test di esempio, il consiglio è quello di non utilizzare un numero di lettere superiore a 22, in quanto impiegherebbe molto tempo per generarlo a causa di una alta complessità computazionale, dovuta alla mia personale scelta implementativa.

