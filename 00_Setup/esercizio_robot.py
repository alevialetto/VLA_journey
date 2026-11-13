import numpy as np

class Robot:
    def __init__(self, nome, n_giunti, seed):
        self.nome = nome
        self.n_giunti = n_giunti
        self.rng = np.random.default_rng(seed)
        self.q = {}
        for i in range(1, self.n_giunti + 1):
            self.q[f"q{i}"] = 0.0

    def stato(self):
        return self.q.copy()
    
    def misura(self, sigma):
        y = {}
        for nome, valore in self.q.items():
            y[nome] = valore + self.rng.normal(0, sigma)
        return y
    
    def passo(self, riferimenti, kp, sigma, dt):  #riferimenti è un dizionario con gli obiettivi, es. {"q1": 1.0, "q2": -0.5, "q3": 0.3}
        y = self.misura(sigma)
        e = {}
        for nome in y:
            e[nome] = riferimenti[nome] - y[nome]
            u = e[nome] * kp
            self.q[nome] += u * dt
        return self.stato()
    
def simula(robot, riferimenti, n_passi, kp, sigma, dt):
    traiettoria = []
    for i in range(1, n_passi +1):
        traiettoria.append(robot.passo(riferimenti, kp, sigma, dt))
    return traiettoria

def estrai(traiettoria, nome):
    stat = []
    for stato in traiettoria:       # stato è il singolo dizionario
        stat.append(stato[nome])    # nome è il giunto di cui ti interessa lo stato es. q1
    return np.array(stat)



if __name__ == "__main__":
    r = Robot("braccio", 3, 0)
    print(r.q)

    # stato(): la copia non modifica il robot
    s = r.stato()
    s["q1"] = 99.0
    print(s)
    print(r.q)

    # misura(): valori rumorosi, stato vero invariato
    print(r.misura(0.1))
    print(r.q)

    # passo(): senza rumore, i giunti vanno verso i riferimenti
    rif = {"q1": 1.0, "q2": -0.5, "q3": 0.3}
    for _ in range(5):
        print(r.passo(rif, 1.0, 0.0, 0.1))

    r2 = Robot("braccio", 3, 0)
    traj = simula(r2, {"q1": 1.0, "q2": -0.5, "q3": 0.3}, 5, 1.0, 0.0, 0.1)
    print(len(traj))
    print(traj[0])
    print(traj[-1])
    r3 = Robot("braccio", 3, 0)
    traj = simula(r3, {"q1": 1.0, "q2": -0.5, "q3": 0.3}, 200, 1.0, 0.05, 0.1)
    serie = estrai(traj, "q1")
    print(serie.shape)
    print(serie[-1])

    # per l'errore a regime considero gli ultimi 50 campioni
    media_regime = serie[-50:].mean()
    errore_regime = 1.0 - media_regime
    print(f"errore a regime = {errore_regime:.4f}")

    deviazione_std = serie[-50:].std()
    print(f"deviazione standard = {deviazione_std:.4f}")