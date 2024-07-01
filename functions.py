def fib(n):
    """Returning the nth fibonacci number"""
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def isPrime(n):
    """Returning whether a function is prime or not"""
    if n <= 1:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i+=1
        return True
