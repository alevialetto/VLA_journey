import torch                             # importa la libreria PyTorch: da qui in poi si usa con il prefisso torch.
import numpy as np                       # importa numpy con il nome breve np (serve per creare l'array di partenza)
print(torch.__version__)                 # print() scrive a schermo; torch.__version__ è la stringa della versione installata (verifica che il venv funzioni)

# %% TENSORI                  
# PREVISIONI:
# q (solo interi)      -> torch.int64
# q_float (con 1.5)    -> torch.float32
# q_np_tens            -> torch.int64 (eredita il dtype dell'array numpy)
# device               -> cpu

lista = [1, 2, 3]                        # lista Python normale con 3 interi (le posizioni dei 3 giunti): non è ancora un tensore
q = torch.tensor(lista)                  # torch.tensor(dati): crea un tensore COPIANDO i dati; il dtype è dedotto (interi -> int64)
q_float = torch.tensor([1, 2, 1.5])      # basta un valore con la virgola perché tutta la lista diventi float (float32, il default di PyTorch)

print(q.sum())                           # somma tutti gli elementi di q, in "()" ci si può mettere la dimensione in sui commarw (dim=0, dim=1, ...)
       .pow(2)                           # same as q**2, eleva alla seconda elemento per elemento, anche su matrici

np_array = np.array(lista)               # np.array(lista): crea un ndarray numpy dalla lista (con numpy 2 su Windows gli interi sono int64)
q_np_tens = torch.from_numpy(np_array)   # torch.from_numpy(arr): tensore che CONDIVIDE la memoria con arr (nessuna copia, stesso dtype)

shape = (4, 3)                           # dimensioni: 4 righe e 3 colonne (per esempio 4 stati di un robot a 3 giunti)
rand_tensor = torch.rand(shape)          # torch.rand(shape): numeri casuali uniformi in [0, 1), dtype float32
zeros_tensor = torch.zeros(shape)        # torch.zeros(shape): tensore di soli zeri, dtype float32

x_ones = torch.ones_like(q)              # torch.ones_like(t): tensore di uni con la stessa shape E lo stesso dtype di q (qui int64)
x_zeros = torch.zeros_like(q)            # torch.zeros_like(t): come sopra ma di zeri
tensor = torch.ones(4, 4)                # tensore 4x4 di soli 1

tensori = {                              # dizionario {nome: tensore}: così posso stampare tutto con un solo ciclo
    "q": q,                              # chiave = stringa col nome, valore = l'oggetto tensore
    "q_float": q_float,                  # ogni coppia chiave: valore è separata da una virgola
    "q_np_tens": q_np_tens,              # ...
    "rand_tensor": rand_tensor,          # ...
    "zeros_tensor": zeros_tensor,        # ...
    "x_ones": x_ones,                    # ...
    "x_zeros": x_zeros,                  # ...
}                                        # fine del dizionario

for nome, t in tensori.items():          # .items() restituisce coppie (chiave, valore); "nome, t" le spacchetta a ogni giro
    print(nome, t.shape, t.dtype, t.device)  # .shape = dimensioni, .dtype = tipo dei numeri, .device = dove vive il tensore (cpu o gpu)


# %% OPERAZIONI TRA TENSORI
A = 0.9 * torch.eye(3)                   # matrice (3, 3): 0.9 sulla diagonale, 0 altrove

t = torch.rand(4,3)
riga0 = t[0]                             # prima riga: un indice solo seleziona la riga intera
ultima_col = t[:, -1]                    # tutte le righe, ultima colonna (indice negativo)
mix = t[:2, -2:]                         # prime due righe (0 e 1), ultime due colonne (1 e 2)
elem = t[2, 1]                           # riga 2, colonna 1 (si parte da 0): tensore a zero dimensioni
valore = elem.item()                     # .item() estrae il numero Python puro

print(f"prima riga: {riga0}, shape {riga0.shape}")
print(f"ultima colonna: {ultima_col}, shape {ultima_col.shape}")
print(f"mix:\n{mix}\nshape {mix.shape}")
print(f"elemento: {elem}, come numero Python: {valore}, tipo {type(valore)}")

# torch.stat --> allunga un asse
# se ho shape = (3,) ho 0 dimensioni, non posso mettere 1
t1 = torch.ones(2,3)               # torch.cat unisce più tensori modificando la dimansione indicata e lasciando invariata l'altra/e
t2 = torch.cat([t1, t1], dim=1)    # dim = 0 --> attacca le righe una sotto l’altra senza aumentare le colonne --> t2 è 4x3
print(t2)                          # dim = 1 --> attacca le colonne una accanto all’altra senza aumentare le righe --> t2 è 2x6


#torch.stack --> mette tensori dello stesso tipo uno accanto all’altro lungo una dimensione nuova
v = torch.ones(2)
torch.stack([v, v, v], dim=0)	           #asse nuovo davanti, un v per riga	(3, 2) 
torch.stack([v, v, v], dim=1)	           #asse nuovo in seconda posizione, un v per colonna	(2, 3)


# prodotto matriciale tra tensori, y1, y2, y3 will have the same value, " tensor.T " returns the transpose of a tensor
# se tensor ha shape (n, m), la trasposta ha shape (m, n) e il risultato y ha shape (n, n)
y1 = tensor @ tensor.T                    # più comodo
y2 = tensor.matmul(tensor.T)

y3 = torch.rand_like(y1)                  #Di solito l’operazione crea un tensore nuovo per il risultato.
torch.matmul(tensor, tensor.T, out=y3)    #Con out=y3 scrive il risultato in un tensore già esistente, y3, senza allocarne uno nuovo
                               

# prodotto elemento per elemento, cioè ogni elemento si moltiplica per quello nella stessa posizione. 
# il risultato ha la stessa shape degli ingressi.
z1 = tensor * tensor
z2 = tensor.mul(tensor)

z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)

# %% ponte con NumPy e operazioni in-place
# PREVISIONI (n o y cambia dopo la modifica?):
# 1) t.add_(1)      -> n CAMBIA   (stessa memoria)
# 2) from_numpy     -> y CAMBIA   (stessa memoria), dtype float64
# 3) torch.tensor   -> y NON cambia (è una copia)
# 4) t = t + 1      -> n NON cambia (t punta a un tensore nuovo)

# 1) tensore -> array, modifica in-place sul tensore
t1 = torch.ones(3)
n1 = t1.numpy()                          # condivide la memoria con t1 (solo per tensori su CPU)
t1.add_(1)                               # in-place: riscrive la memoria di t1
print(f"1) t1: {t1}, n1: {n1}")

# 2) array -> tensore con from_numpy, modifica sull'array
x2 = np.zeros(3)                         # numpy usa float64 di default
y2 = torch.from_numpy(x2)                # condivide la memoria con x2
x2[0] = 5                                # modifico l'array
print(f"2) x2: {x2}, y2: {y2}, dtype {y2.dtype}")

# 3) array -> tensore con torch.tensor, che copia i dati
x3 = np.zeros(3)
y3 = torch.tensor(x3)                    # copia: memoria separata
x3[0] = 5
print(f"3) x3: {x3}, y3: {y3}")

# 4) riassegnazione al posto dell'in-place
t4 = torch.ones(3)
n4 = t4.numpy()
t4 = t4 + 1                              # crea un tensore nuovo e sposta l'etichetta t4
print(f"4) t4: {t4}, n4: {n4}")

# %% GRADIENTI E DERIVATE
import torch

x = torch.tensor(2.0, requires_grad=True)   # requires_grad=True: "registra le operazioni su x per poterne calcolare la derivata" (solo tensori float, solo su ciò che vuoi derivare)
y = x**3                                    # y nasce da x, quindi eredita la registrazione

print(x.grad)                               # .grad: attributo di x dove finisce la derivata; vale None finché non chiami backward()
y.backward()                                # backward(): calcola dy/dx all'indietro (regola della catena) e la scrive in x.grad; y deve essere uno scalare
print(x.grad)                               # tensor(12.) = derivata di x**3 valutata in x = 2 (numero, non formula); stessa shape di x

y = x**3                                    # nuovo grafo: serve ricalcolare y se vuoi richiamare backward()
y.backward()                                # senza la riga sopra: RuntimeError (il grafo viene liberato dopo la prima chiamata)
print(x.grad)                               # tensor(24.): i gradienti si SOMMANO (12 + 12), non si sovrascrivono

x.grad.zero_()                              # zero_(): azzera .grad sul posto (il "_" finale indica un'operazione in-place); da fare prima di ogni nuovo giro

y = x**3
y.backward(retain_graph=True)               # retain_graph=True: conserva il grafo, così un secondo backward() sulla stessa y non dà errore (raramente serve)

a = torch.tensor(2.0)                       # tensore normale: requires_grad=False di default
a.requires_grad_(True)                      # requires_grad_(True): attiva la registrazione dopo la creazione (in-place)

q = torch.tensor([1.0, 2.0], requires_grad=True)
J = (q**2).sum()                            # backward() vuole uno scalare: .sum() riduce un vettore a un numero
J.backward()
print(q.grad)                               # tensor([2., 4.]) = [2·q1, 2·q2]; ha la shape di q (una derivata parziale per elemento)

print(y.grad_fn)                            # grad_fn: l'operazione che ha creato y (parte del grafo computazionale); è None per i tensori normali
x = torch.tensor(2.0, requires_grad=True)
y = x**3
z = y + 1

print(x.grad_fn)   # None: x l'hai creato tu, non nasce da nessuna operazione
print(y.grad_fn)   # <PowBackward0 ...>: y è nato da una potenza
print(z.grad_fn)   # <AddBackward0 ...>: z è nato da una somma

# % no_grad: calcola senza registrare la catena
w = torch.tensor(2.0, requires_grad=True)   # parametro con requires_grad=True: punto di partenza della catena di derivazione

y = w * 3                                   # calcolo normale: PyTorch registra il passaggio
print(y)                                    # tensor(6., grad_fn=<MulBackward0>)  grad_fn presente = catena registrata
print(y.requires_grad)                      # True

with torch.no_grad():                       # no_grad: le righe indentate qui sotto NON vengono registrate (fuori dal blocco il tracciamento riparte)
    y2 = w * 3                              # stesso calcolo, stesso valore, ma senza catena
print(y2)                                   # tensor(6.)  nessun grad_fn: il valore non cambia, cambia solo la registrazione
print(y2.requires_grad)                     # False
print(y2.grad_fn)                           # None

y.backward()                                # funziona: la catena c'è
print(w.grad)                               # tensor(3.)  = d(w*3)/dw
# y2.backward()                             # RuntimeError: y2 non ha catena, non c'è da dove risalire

