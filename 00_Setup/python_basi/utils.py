def saturazione(u, u_max=10.0):
    """Limita u nell'intervallo [-u_max, u_max]."""
    if u > u_max:
        return u_max
    elif u < -u_max:
        return -u_max
    else:
        return u


if __name__ == "__main__":
    print(saturazione(5.0))              # 5.0
    print(saturazione(50.0))             # 10.0
    print(saturazione(-50.0))            # -10.0
    print(saturazione(50.0, u_max=5.0))  # 5.0