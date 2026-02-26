def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_memo(n, cache={}):
    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci_memo(n-1, cache)+ fibonacci_memo(n-2, cache)
    return cache[n]