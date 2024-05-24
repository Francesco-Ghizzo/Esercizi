def sumFirstN(n):
    return n*(n+1)//2

def recSumFirstN(n):
    if n == 0:
        return 0
    else:
        return recSumFirstN(n-1) + n
