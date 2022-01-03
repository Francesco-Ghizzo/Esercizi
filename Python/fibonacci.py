# opzione 1

def Fibonacci(num):
    if num < 3:
        return 1
    else:
        a = b = 1
        for i in range(2, num):
            a, b = b, a + b
        return b


# opzione 2

def fib(n):
     a, b = 0, 1
     for i in range(n):
         tmp = a
         a = b
         b = tmp + b
     return a
