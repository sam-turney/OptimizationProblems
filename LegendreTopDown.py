def Legendre(n, x, t):
    if t[n-1] != -1:
        return t[n-1]
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x - 1
    else:
        t[n-1] = ((2 * n - 1) * x * Legendre(n - 1, x, t) - (n - 1) * Legendre(n - 2, x, t)) / n
        return t[n-1]
    
if __name__ == '__main__':
    n = 100
    x = 2
    t = [-1] * n

    result = Legendre(n, x, t)
    print(result)
