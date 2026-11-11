setpoint = 90
misura = 87.5
tolleranza = 2

#1
print(f"tipo setpoint: {type(setpoint)}\ntipo misura: {type(misura)}\ntipo tolleranza: {type(tolleranza)}")

#2
errore = setpoint - misura
print(f"valore errore: {errore:.2f}")
print(f"tipo errore: {type(errore)}")

#3
if abs(errore) <= tolleranza:
    print("a regime")
elif errore > 0:
    print("Sotto il setpoint: aumenta")
else:
    print("Sopra il setpoint: diminuisci")

#4
durata_ms = 7350
durata_sec = durata_ms/1000
durata_sec_int = durata_ms//1000
resto_ms = durata_ms%1000
print(f"durata_sec: {durata_sec:.2f}s")
print(f"durata_sec_int: {durata_sec_int}s")
print(f"resto_ms: {resto_ms}ms")

#5
misura = "N/D"
#print(misura + 1) TypeError: can only concatenate str (not "int") to str
print(f"tipo misura: {type(misura)}")
