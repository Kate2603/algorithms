# обчислення чисел Фібоначчі з мемоізацією
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = value
        return value

# Функція lru_cache є декоратором у стандартній бібліотеці Python, 
# який можна застосувати до функцій для кешування їхніх результатів

from functools import lru_cache

@lru_cache(maxsize=None)  # Unbounded cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(25)