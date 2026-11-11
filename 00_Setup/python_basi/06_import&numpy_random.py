import math
import numpy as np

# %%    ES 1
L = 0.5      # [m]
theta = 30   # [gradi]
x = L * math.cos(math.radians(theta))
y = L * math.sin(math.radians(theta))
print(f"x = {x:.4f} m")
print(f"y = {y:.4f} m")

# %% ES 2
l = 2
traiettoria = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
xs = l * np.cos(np.radians(traiettoria))
print(xs.mean(), xs.shape)

# %% ES 3
tempi = np.linspace(0.0, 1.0, 11)
print(tempi)

# %% ES 4
rng = np.random.default_rng(42)
misure = 90.0 + rng.normal(0.0, 0.5, size=5)
print(misure)
campioni = 90 +rng.normal(0.0, 0.5, size=1000)
print(np.mean(campioni), np.std(campioni) ,campioni.shape)

# %% ES 5
rng = np.random.default_rng(42)


def misura_rumorosa(valore_vero, sigma, rng):
    """Restituisce valore_vero più rumore gaussiano di deviazione sigma."""
    return valore_vero + rng.normal(loc=0.0, scale=sigma)


for i in range(5):
    misura = misura_rumorosa(90.0, 0.5, rng)
    print(f"misura {i}: {misura:.3f}")

# %%  ES 6
def saturazione(u, u_max):
    """Limita u nell'intervallo [-u_max, u_max]."""
    if u > u_max:
        return u_max
    elif u < -u_max:
        return -u_max
    else:
        return u


if __name__ == "__main__":
    print(saturazione(5.0, 10.0))      # 5.0
    print(saturazione(50.0, 10.0))     # 10.0
    print(saturazione(-50.0, 10.0))    # -10.0
