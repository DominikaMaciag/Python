# Zadanie 4 - Dominika Maciąg

import functools

dict = {}
def pamiec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        naszargument = args[0]
        if naszargument in dict:
            return dict[naszargument]
        else:
            dict[naszargument] = func(*args, **kwargs)
            return dict[naszargument]
    return wrapper

@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1000):
    print(fibonacci(i))
    
print(dict)