# %% punto 1
def errore(setpoint, misura):
    return setpoint - misura

# %% punto 2
def saturazione(u, u_max = 10.0):
    if abs(u) >  u_max:
        if u > 0:
            return u_max
        else:
            return -u_max
    else:
        return u

# %% punto 3 
def controllo_p(setpoint, misura, kp=1.0, u_max=10.0):
    u = kp * errore(setpoint, misura)
    return saturazione(u, u_max)

# %% punto 4
def stat(measures):
    return min(measures), max(measures), sum(measures)/len(measures)

# %% punto 5  (considero kp come un vettore di valori)
def simula_p(kp, setpoint=10.0, tol=0.01, max_passi=100):
    for val in kp:
        x = 0.0
        i = 0
        while abs(setpoint - x) > tol and i < max_passi:
           x = x + val * (setpoint - x)
           i+=1
        print(f"numero passi: {i}")
        print(f"valore x raggiunto: {x:.2f}")


# %% punto 6
def azzeraPrimo(lista):
    lista[0] = 0