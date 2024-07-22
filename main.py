import re
from typing import Callable


def caching_fibonacci():
    cache_fibonacci = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache_fibonacci:
            return cache_fibonacci[n]
        else:
            cache_fibonacci[n] = fibonacci(n - 1) + fibonacci(n - 2) 
            return cache_fibonacci[n]
    return fibonacci

# print(caching_fibonacci()(50))

def generator_numbers(text: str):
    text_list = text.split(' ')
    reg = re.compile(r'\d+(?:\.\d*)')
    floats_generator = (float(el) for el in text_list if reg.match(el))
    return floats_generator

def sum_profit(text: str, func: Callable):        
    numbers_generator = func(text)
    number = next(numbers_generator)
    res = 0
    try:
        while number:
            res += number
            number = next(numbers_generator)
    except StopIteration:
        return res
    

print(sum_profit('Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів. ', generator_numbers))