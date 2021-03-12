def Fibonacci(num):
    if num < 3:
        return 1
    a = b = 1
    for i in range(2, num):
        a, b = b, a+b
    return b

