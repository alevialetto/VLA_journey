
# %% punto 1
traiettoria = [10, 20, 30, 40, 50]
for angolo in traiettoria:
    print(angolo)

# %% punto 2
for i, angolo in enumerate(traiettoria):
    print(f"waypoint {i}: {angolo:.1f}°")

# %% punto 3
dt = 0.1                     # passo di campionamento [s]
tempi = []
for k in range(11):          # k = 0, 1, ..., 10  → 11 campioni (11 escluso)
    tempi.append(k * dt)     # tempo calcolato dall'indice intero
print(tempi)

# %% punto 4
pid = {"kp": 2.0, "ki": 0.5, "kd": 0.1}
for chiave, valore in pid.items():
    print(f"{chiave} = {valore}")

# %% punto 5
sensori=[
    {"nome":"temp", "valore":10.0, "ok":True },
    {"nome":"press", "valore":273.1, "ok":True },
    {"nome":"magn", "valore":105.8, "ok":False }
]
setpoint = 90
i = 0
for s in sensori:
    if not s["ok"]:
        print(f"{s["nome"]} GUASTO, salto")
    else:
        errore = setpoint - s["valore"]
        print(f"Errore = {errore:.2f}")
        i+=1
print(f"contatore: {i}")

# %% punto 6
x = 0.0
setpoint = 10.0
kp = 0.5
i = 0
tolleranza = 0.01
while abs(setpoint - x) > tolleranza and i < 100:
       x = x + kp * (setpoint - x)
       i+=1
print(f"numero passi: {i}")
print(f"valore x raggiunto: {x:.2f}")



# %%
