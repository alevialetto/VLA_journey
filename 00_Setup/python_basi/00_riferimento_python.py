"""Promemoria Python - lezioni 1-6. Righe di codice con spiegazione a fianco."""
import math
import numpy as np

# ===================== LEZIONE 1 - SINTASSI E TIPI =====================
x = 5                       # int
x = 5.0                     # float (come double)
x = True                    # bool (maiuscola)
x = "N/D"                   # str
x = None                    # come NULL
type(x)                     # tipo del valore (dentro print per vederlo)
if x == 1:                  # niente parentesi, ':' apre il blocco, rientro 4 spazi
    pass
elif x == 2:                # else if
    pass
else:
    pass
7 / 2                       # 3.5  divisione sempre reale
7 // 2                      # 3    divisione intera
-7 // 2                     # -4   arrotonda verso -infinito (in C darebbe -3)
7 % 2                       # 1    resto
2 ** 3                      # 8    potenza
a = 1; a += 1               # a++ non esiste
True and not False          # and, or, not (no &&, ||, !)
err = 2.5
print(f"err: {err:.2f}")    # f-string: {} calcola, :.2f = 2 decimali
print(f"{err * 2}")         # dentro {} va qualsiasi espressione
d = {"nome": "enc"}
print(f"{d['nome']}")       # apici diversi dentro la f-string
abs(0.1 + 0.2 - 0.3) < 1e-9 # float: confronto con tolleranza, mai ==



# ===================== LEZIONE 2 - LISTE E DIZIONARI =====================
q = [0.0, 30.0, 45.0, 60.0]
q[0]                        # primo (indici da 0)
q[-1]                       # ultimo
q[-2]                       # penultimo
q[1:3]                      # [30.0, 45.0]  inizio incluso, fine ESCLUSA
q[:3]                       # primi 3
q[-2:]                      # ultimi 2
len(q)                      # lunghezza
q.append(90.0)              # aggiunge in fondo (non fare q = q.append(..))
45.0 in q                   # True/False
b = q                       # NON copia: due etichette sulla stessa lista
b = q.copy()                # copia vera
q[0] = 1.0                  # modifica l'oggetto (si vede da tutte le etichette)
q = [9.0]                   # sposta solo l'etichetta q su una lista nuova

pid = {"kp": 2.0, "ki": 0.5}
pid["kp"]                   # lettura (KeyError se manca)
pid["kd"] = 0.1             # scrittura; se la chiave non c'e' la crea
pid.get("kff", 0.0)         # lettura con default, non aggiunge la chiave
"kp" in pid                 # controlla le CHIAVI
vuoto = {}                  # dizionario vuoto, riempito dopo
# pid["kd"] = 0,5           # ERRORE SILENZIOSO: la virgola crea una tupla. Decimali col punto
sensori = [{"nome": "t", "valore": 1.0}, {"nome": "p", "valore": 2.0}]
sensori[1]["nome"]          # prima indice della lista, poi chiave



# ===================== LEZIONE 3 - CICLI =====================
for ang in q:               # scorre gli ELEMENTI
    print(ang)
for k in range(5):          # 0..4 (fine esclusa, solo interi)
    t = k * 0.1             # tempo campionato: k*dt, non sommare dt
for i, ang in enumerate(q): # indice e valore insieme
    print(i, ang)
for chiave in pid:          # chiavi del dizionario
    print(chiave)
for chiave, val in pid.items():  # chiavi e valori
    print(chiave, val)
for s in sensori:
    if s["valore"] < 0:
        continue            # salta al giro dopo
    if s["valore"] > 100:
        break               # esce dal ciclo
xx, sp, kp, passi = 0.0, 10.0, 0.5, 0
while abs(sp - xx) > 0.01 and passi < 100:  # abs + limite passi
    xx = xx + kp * (sp - xx)                # P discreto: e[k+1] = (1-kp) e[k], converge se 0<kp<2
    passi += 1
while True:                 # do-while non esiste: while True + break
    break



# ===================== LEZIONE 4 - FUNZIONI =====================
def saturazione(u, u_max=10.0):   # default senza spazi attorno a '='
    """Limita u in [-u_max, u_max]."""
    if u > u_max:
        return u_max
    elif u < -u_max:
        return -u_max
    return u

saturazione(50.0)           # 10.0
saturazione(50.0, u_max=5)  # argomento per nome
def stat(v):
    return min(v), max(v), sum(v) / len(v)   # piu' valori di ritorno
mn, mx, media = stat([1.0, 2.0, 3.0])        # si spacchettano
min([1, 2]); max([1, 2]); sum([1, 2]); len([1, 2]); abs(-3)   # funzioni pronte
def azzera_primo(lista):
    lista[0] = 0.0          # modifica l'oggetto: si vede fuori
def sostituisci(lista):
    lista = [0.0]           # sposta solo l'etichetta locale: fuori non cambia
# parametri e variabili create nella funzione sono LOCALI
# mai liste come default (def f(l=[])): usa None e crea la lista dentro



# ===================== LEZIONE 5 - CLASSI =====================
# Classe = stampo: dice quali dati (attributi) e quali funzioni (metodi) avra' l'oggetto.
# Da una classe crei quanti oggetti vuoi, ognuno con i PROPRI dati.
class Giunto:                                   # CamelCase
    def __init__(self, nome, posizione=0.0, limite=180.0):
        # __init__ parte da solo quando scrivi Giunto(...). self = l'oggetto che si sta creando
        self.nome = nome            # sinistra = nome con cui lo leggi da fuori (g.nome)
        self.posizione = posizione  # destra = il PARAMETRO (se non lo copi in self, si perde)
        self.limite = limite
        self.storico = []           # valore fisso, non e' un parametro: lista nuova per ogni oggetto

    def muovi(self, delta):         # metodo: 'self' sempre primo parametro, non lo passi tu
        self.posizione += delta     # dentro la classe gli attributi si leggono con self.
        self.posizione = saturazione(self.posizione, self.limite)
        self.storico.append(self.posizione)

    def stato(self):
        return f"{self.nome}: {self.posizione:.1f}"   # restituisce, la print la fai fuori

class ControlloreP:
    def __init__(self, kp, u_max=10.0):
        self.kp = kp
        self.u_max = u_max

    def calcola(self, setpoint, misura):
        errore = setpoint - misura                    # variabile locale: niente self.
        return saturazione(self.kp * errore, self.u_max)

g = Giunto("g1")                    # crea l'oggetto (niente 'new'): __init__ gira da solo
g.muovi(30.0)                       # metodo: con le parentesi
g.posizione                         # attributo: senza parentesi
g.nome = "altro"                    # si puo' modificare da fuori
g.storico                           # attributo interno: da fuori si legge comunque
ctrl = ControlloreP(2.0)
g2 = Giunto("g2")                   # oggetto indipendente da g: stato separato
# anello chiuso: giunto = integratore x[k+1]=x[k]+u[k], controllore = P (come in lezione 3)
setpoint, passi = 90.0, 0
while abs(setpoint - g2.posizione) > 0.01 and passi < 100:
    g2.muovi(ctrl.calcola(setpoint, g2.posizione))
    passi += 1
# Errori tipici:
#   metodo senza self           -> TypeError alla chiamata
#   kp invece di self.kp        -> NameError
#   metodo rientrato in __init__-> non e' un metodo (AttributeError)
#   g.posizone = 3 (refuso)     -> nessun errore: crea un attributo nuovo



# ===================== LEZIONE 6 - IMPORT, NUMPY, RANDOM =====================
# import: come #include, ma le funzioni si usano col nome del modulo.
# math = un numero alla volta, radianti. np = array interi.
math.sqrt(16)                       # 4.0
math.cos(math.radians(30))          # radians converte gradi->rad (cos/sin vogliono rad)
# from utils import saturazione    # importa da utils.py nella STESSA cartella dello script
#                                  # (nome file: niente cifre iniziali, niente '&')
# if __name__ == "__main__":       # blocco che gira solo se lanci il file direttamente,
#     ...                          # non quando lo importi: ci metti le prove
ang = np.array([10.0, 20.0, 30.0])  # lista -> array NumPy (un solo tipo)
ang * 2                             # opera su ogni elemento (una lista * 2 la duplicherebbe)
np.cos(np.radians(ang))             # versione array di math: niente for
ang.shape                           # forma: (3,) vettore; (2,3) = 2 righe 3 colonne. ATTRIBUTO, no ()
ang.mean()                          # METODO, con (). Equivale a np.mean(ang)
np.linspace(0.0, 1.0, 11)           # 11 punti da 0 a 1, estremo INCLUSO (passo 0.1)

rng = np.random.default_rng(42)     # generatore pseudocasuale con stato interno; 42 = seme
                                    # stesso seme = stessa sequenza; ogni chiamata fa avanzare lo stato.
                                    # Crealo UNA volta e passalo alle funzioni (non ricrearlo dentro)
rng.normal(loc=0.0, scale=0.5)      # un numero da gaussiana: loc = media, scale = deviazione standard (sigma)
rng.normal(0.0, 0.5, size=1000)     # array di 1000 campioni indipendenti
rng.uniform(-1.0, 1.0, size=5)      # densita' costante in [-1, 1) (1 escluso)
np.mean(rng.normal(0, 0.5, 1000))   # media dei campioni: ~0 (non esatta: campione finito)
np.std(rng.normal(0, 0.5, 1000))    # deviazione standard dei campioni: ~0.5 (stesse unita' dei dati)
def misura_rumorosa(valore_vero, sigma, rng):
    return valore_vero + rng.normal(loc=0.0, scale=sigma)   # modello sensore: y = y_vero + v
