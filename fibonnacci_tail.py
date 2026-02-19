def fibonnaci_tail(n, actual = 0, next = 1):
    if n == 0:
        return actual
    return fibonnaci_tail(n-1, next, actual + next)

import time
inicio = time.time()

print(fibonnaci_tail(100))

fin = time.time()-inicio
