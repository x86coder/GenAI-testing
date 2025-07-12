def gfactorial(x):
    if x < 0:
        raise ValueError("El factorial no esta definido para numeros negativos")
    else:
        if x == 0:
            return 1
        else:
            return x * gfactorial(x-1)

if __name__ == '__main__':
    print("##################### gfactorial v0.1 #####################")
    import sys
    a = int(sys.argv[1])
    print("gfactorial(" + str(a) + ") = " + str(gfactorial(a)))