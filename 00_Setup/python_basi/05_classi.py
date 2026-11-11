# % FUNZIONI COMUNI
def saturazione(u, u_max):
    if abs(u) >  u_max:
        if u > 0:
            return u_max
        else:
            return -u_max
    else:
        return u

# % ES 1
class Giunto:
    def __init__(self, nome, posizione=0.0, limite=180.0):
        self.nome = nome
        self.storico = []
        self.posizione = posizione
        self.limite = limite

    def muovi(self, delta):
        self.posizione += delta
        self.posizione = saturazione(self.posizione, self.limite)
        self.storico.append(self.posizione)
    def stato(self):
        return f"{self.nome} : {self.posizione:.1f}"
        #print(f"{self.nome} : {self.posizione:.1f}")
# g1 = Giunto("giunto1",0.0)
# g2 = Giunto("giunto2",45.0)
# g1.muovi(100)
# g2.muovi(200)
# g2.muovi(-150)
# print(g1.stato())
# print(g2.stato())

# % ES 2   
class ControlloreP:
    def __init__(self, kp, u_max=10.0):
        self.kp = kp
        self.u_max = u_max

    def calcola(self, setpoint, misura):
        errore = setpoint - misura
        return saturazione(self.kp * errore, self.u_max)

# c = ControlloreP(2.0)
# print(c.calcola(20, 15))
# print(c.calcola(2, 100))

# % ES3
i=0
g = Giunto("giunto")
ctrl = ControlloreP(2.0)
setpoint = 90
tolleranza = 0.01
while abs(setpoint - g.posizione) > tolleranza and i < 100:
    i += 1
    g.muovi(ctrl.calcola(setpoint, g.posizione))
print(f"passi totali: {i}")
print(f"posizione finale: {g.posizione}")
print(len(g.storico))
print(g.storico[-3:])
