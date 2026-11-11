import numpy as np

class Robot:
    def __init__(self, nome, n_giunti, seed):
        self.nome = nome
        self.n_giunti = n_giunti
        self.rng = np.random.default_rng(seed)

r = Robot("braccio", 3, 0)
print(r.nome, r.n_giunti, r.rng.normal())
print(r.rng.normal())
print(r.rng.normal())