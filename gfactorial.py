'''
Authors: Claude 3.5 Sonnet & Amed Reyes
License: Corresponding copyright holders
Date: July 11th, 2025
'''
def gfactorial(x):
    if x < 0:
        raise ValueError("Error: factorial is not defined for negative numbers!")
    else:
        if x == 0:
            return 1
        else:
            return x * gfactorial(x-1)      # Copilot fixed a bug here (missing x factor)

if __name__ == '__main__':
    import sys
    param = int(sys.argv[1])
    print(" > Calculating factorial for " + str(param))
    print(" > gfactorial(" + str(param) + ") = " + str(gfactorial(param)))