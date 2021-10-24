# en Python 3, il n'y a pas de limite sur les int.
# en Python 2, il y a des entiers en 32 et 64 Attention les nombres en sciences c'est important

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibs = []
    fibs.append(1)
    fibs.append(1)
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    print(fibs)
    return fibs[n]



print(fibo(2021))