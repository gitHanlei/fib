# coding utf-8

"""
fab数列的多种实现方式
"""


# 常规模式
def fib(n):
    a, b = 0, 1
    while 1:
        print(a, end=' ')
        a, b = b, a + b
        if n <= 0:
            break
        n = n - 1


# 利用元组实现

def fib_tuple(n):
    fibs = [0, 1]
    for index in range(n):
        fibs.append(fibs[-2] + fibs[-1])
    print(fibs)


# 利用迭代器

def fib_iter():
    class Fibs:
        def __init__(self):
            self.a = 0
            self.b = 1

        def __next__(self):
            self.a, self.b = self.b, self.a + self.b
            return self.a

        def __iter__(self):
            return self

    fibs = Fibs()

    for f in fibs:
        # 防止生成一个无穷大的数列
        if f > 1000:
            print(f)
            break
        else:
            print(f)


# 利用列表推导式、递归(未加入缓存)
def fib_list(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib_list(n - 2) + fib_list(n - 1)


# 利用列表推导式 (加入缓存机制)
def fib_list_cache(n, cache=None):
    if cache is None:
        # 应用对象列表
        cache = {}
    if n in cache:
        return cache[n]
    if n == 1 or n == 0:
        return 1
    else:
        cache[n] = fib_list_cache(n - 2, cache) + fib_list_cache(n - 1, cache)
        return cache[n]
