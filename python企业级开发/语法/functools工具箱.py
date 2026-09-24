# ============== cache ==============
from functools import cache

# 使用 cache 装饰器缓存函数结果
@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))

# ============== partial ==============
from functools import partial

def power(base, exp):
    return base ** exp
# 把 power 函数的 exp 参数固定为 2，创建一个新的函数 square
square = partial(power, exp=2)
# 把 power 函数的 exp 参数固定为 3，创建一个新的函数 cube
cube = partial(power, exp=3)

print(square(5))
print(cube(5))


# ============== reduce ==============

from functools import reduce

nums = [1, 2, 3, 4, 5]

# 求和，(((1+2)+3)+4)+5
total = reduce(lambda a, b: a + b, nums)
print(total)

# 求最大值
max_val = reduce(lambda a, b: a if a > b else b, nums)
print(max_val)

# 字符串拼接
words = ["hallo", " ", "world"]
sentence = reduce(lambda a, b: a + b, words)
print(sentence)


# ============== wraps ==============

import functools

# 定义一个装饰器函数，并使用 wraps 装饰器保留被装饰函数的元信息
def my_decorator(func):
    @functools.wraps(func)   # 写装饰器，无脑加
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def hello():
    """打个招呼"""
    print("hi")

print(hello.__name__)
print(hello.__doc__)



# ============== total_ordering ==============

from functools import total_ordering

# 使用 total_ordering 装饰器自动生成缺失的比较方法
@total_ordering
class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)


v1 = Version(1, 2)
v2 = Version(1, 10)

print(v1 < v2)
print(v1 > v2) # 自动生成
print(v1 <= v2)

# ============== singledispatch ==============

from functools import singledispatch

# 根据参数类型执行不同函数，实现多态
@singledispatch
def show(x):
    return f"未知类型: {x}"

@show.register(int)
def _(x):
    return f"整数: {x}"

@show.register(str)
def _(x):
    return f"字符串: {x}"

@show.register(list)
def _(x):
    return f"列表: {x}"

print(show(42))         # 整数: 42
print(show("hi"))       # 字符串: hi
print(show([1, 2, 3]))  # 列表，长度 3
print(show(3.14))       # 未知类型: 3.