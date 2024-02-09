def Legendre(n, x):
    t = [-1] * (n + 1)
    t[0] = 1
    t[1] = 2 * x - 1
    for i in range(2, n + 1):
        t[i] = ((2 * i - 1) * x * t[i - 1] - (i - 1) * t[i - 2]) / i
    return t[n]
    
if __name__ == '__main__':
    n = 100
    x = 2

    result = Legendre(n, x)
    print(result)
