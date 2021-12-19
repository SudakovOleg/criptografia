def generator(A,C,D,X,X2,N,iterations):
    p1 = -1
    p2 = -1
    A  = 0
    C  = 2
    D  = 3
    X  = 12
    X2 = 0
    N  = 12111
    iterations  = 100

    for i in range (2, iterations):
        X2=(D*(int(pow(X,2)))+(A*X)+C) % N
        if (p1 == -1 and i == iterations / 4):
            p1 = X2
        elif (X2 == p1):
            p2= i - iterations / 4
            p1 = -2
        X = X2
        print(i, " = ", X2)
    print("Период ", " = ", p2)
