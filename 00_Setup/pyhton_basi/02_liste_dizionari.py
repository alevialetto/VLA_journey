# %% Punto 1
t = [10.0, 20.1, 30.2, 40.3, 50.4]  # t = traiettoria
print(f"primo el: {t[0]:.1f}")
print(f"ultimo el: {t[-1]:.1f}")
print(f"lunghezza t: {len(t)}")

# %% Punto 2
t.append(60.5)
print(t[:3])
print(t[-2:])

#3
print(10.0 in t)
print(20.5 in t)

#4
backup = t                  # stessa lista, due etichette
t[0] = 0.0                  # caso A: modifico l'oggetto
print(f"A  t: {t}\n   backup: {backup}")      # backup cambiato anche lui

t = [1.0, 2.0, 3.0]         # caso B: sposto l'etichetta t su una lista nuova
print(f"B  t: {t}\n   backup: {backup}")      # backup resta la lista vecchia

backup = t.copy()           # copia vera: oggetto distinto
t[0] = 99.0
print(f"copy  t: {t}\n      backup: {backup}")  # backup intatto

#5
pid={"kp":2.0, "ki":2.5, "kd":0.1}
print(pid["kp"])
pid["kd"] = 0.5
pid["saturazione"] = 5
print(f"dizionario completo: {pid}")
#pid["kff"]  errore: KeyError: 'kff'
pid.get("kff",0.0)
print(pid.get("kff",0.0))

#6
sensori=[
    {"nome":"temp", "valore":10.4, "ok":True },
    {"nome":"press", "valore":105.8, "ok":False }
]

print(sensori[1]["nome"])
setpoint = 90
errore = setpoint - sensori[0]["valore"]
print(errore)

