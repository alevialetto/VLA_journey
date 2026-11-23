# %% 
import torch
import numpy as np
print(torch.__version__)

# %% cinque tensori

lista = [1, 2, 3]                       # 3 giunti
q = torch.tensor(lista)
q_float = torch.tensor([1, 2, 1.5])

np_array = np.array(lista)
q_np_tens = torch.from_numpy(np_array)

shape = (4, 3)
rand_tensor = torch.rand(shape)
zeros_tensor = torch.zeros(shape)

x_ones = torch.ones_like(q)             # shape e dtype di q
x_zeros = torch.zeros_like(q)

tensori = {
    "q": q,
    "q_float": q_float,
    "q_np_tens": q_np_tens,
    "rand_tensor": rand_tensor,
    "zeros_tensor": zeros_tensor,
    "x_ones": x_ones,
    "x_zeros": x_zeros,
}

for nome, t in tensori.items():
    print(nome, t.shape, t.dtype, t.device)


# %% 
t = torch.rand(4,3)
riga0 = t[0]                             # prima riga: un indice solo seleziona la riga intera
ultima_col = t[:, -1]                    # tutte le righe, ultima colonna (indice negativo)
mix = t[:2, -2:]                         # prime due righe (0 e 1), ultime due colonne (1 e 2)
elem = t[2, 1]                           # riga 2, colonna 1 (si parte da 0): tensore a zero dimensioni
valore = elem.item()                     # .item() estrae il numero Python puro:  tensore di 1 el. --> float

print(f"prima riga: {riga0}, shape {riga0.shape}")
print(f"ultima colonna: {ultima_col}, shape {ultima_col.shape}")
print(f"mix:\n{mix}\nshape {mix.shape}")
print(f"elemento: {elem}, come numero Python: {valore}, tipo {type(valore)}")

# %%
a = torch.zeros(3,)
b = torch.ones(3,)
c = torch.rand(3,)

t1 = torch.cat([a, b, c])         # dimensione prevista: (9,)
t2 = torch.stack([a, b, c], dim=0)        # dimensione prevista: (3,3)

# %%
# %% dinamica: q_next = A @ q + dt * u
# PREVISIONI:
# A @ q            -> shape (3,)     prodotto matriciale
# A * q            -> shape (3, 3)   nessun errore: q viene "ripetuto" su ogni riga (broadcasting)
# q_next           -> shape (3,)

q = torch.tensor([1.0, 2.0, 3.0])        # stato dei 3 giunti (float, serve per @ con A)
u = torch.tensor([0.5, -1.0, 2.0])       # ingresso di controllo
A = 0.9 * torch.eye(3)                   # matrice (3, 3): 0.9 sulla diagonale, 0 altrove
dt = 0.01                                # passo di integrazione

y_matmul = A @ q                         # prodotto matriciale
y_mul = A * q                            # prodotto elemento per elemento, con broadcasting
q_next = A @ q + dt * u                  # un passo della dinamica

print(f"A @ q: {y_matmul}, shape {y_matmul.shape}")
print(f"A * q:\n{y_mul}\nshape {y_mul.shape}")
print(f"q_next: {q_next}, shape {q_next.shape}")

# in place operation
print(f"{tensor} \n")                   #Un’operazione in-place scrive il risultato nello stesso tensore, invece di crearne uno nuovo.
print(tensor)                           # t.add_(1)	modifica la memoria di t	sì
tensor.add_(5)                          # t = t + 1	crea un tensore nuovo e sposta l’etichetta t su di esso	

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