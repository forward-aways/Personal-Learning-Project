import xml.dom.minidom
# ============== chain ==============
# 将多个序列连接成一个序列
from itertools import chain
from operator import itruediv

a = [1, 2, 3]
b = ["x", "y"]
c = (True, False)

print(list(chain(a, b, c)))

# ============== product ==============

# 计算多个序列的笛卡尔积
from itertools import product

colors = ["红", "蓝"]
sizes = ["S", "M"]

for color, size in product(colors, sizes):
    print(color, size)


# ============== permutations, combinations ==============
# 计算序列的全排列和组合

from itertools import permutations, combinations

items = ["A", "B", "C"]
# 计算序列的全排列, 顺序有关
print(list(permutations(items, 2)))
# 计算序列的组合, 顺序无关
print(list(combinations(items, 2)))


# ============== groupby ==============
# 对序列进行分组

from itertools import groupby

data = [
    {"name": "Alice", "dept": "IT"},
    {"name": "Bob", "dept": "IT"},
    {"name": "Cindy", "dept": "HR"},
    {"name": "David", "dept": "HR"},
    {"name": "Eve", "dept": "Sales"},
]

data.sort(key=lambda x: x["dept"])

for dept, group in groupby(data, key=lambda x: x["dept"]):
    names = [p["name"] for p in group]
    print(dept, names)

# ============== count, cycle, repeat, islice ==============

from itertools import count, cycle, repeat, islice

# count: 从 0 开始无穷数
for i in count(10):
    if i > 15:
        break
    print(i)

# cycle: 循环一个序列
count_c = 0
for x in cycle("AB"):
    if count_c >= 10:
        break
    count_c += 1
    print(x)

# repeat: 重复同一个值
print(list(repeat("hi", 3)))

# 配合islice 取前n个
print(list(islice(count(0), 5)))


# ============== accumulate ==============
# 前缀和，累积统计

from itertools import accumulate

nums = [1, 2, 3, 4, 5]

# 累计和(默认)
print(list(accumulate(nums)))

# 累积乘
import operator
print(list(accumulate(nums, operator.mul)))


# ============== islice ==============
# 切片迭代器


from itertools import islice

def infinite():
    n = 0
    while True:
        yield n
        n += 1

# 取前5个
print(list(islice(infinite(), 5)))
# 取第3到第8个
print(list(islice(infinite(), 3, 8)))


# ============== zip_longest ==============
# 长度不等时补齐


# 普通zip
print(list(zip([1, 2, 3], ["a", "b"])))

from itertools import zip_longest

print(list(zip_longest([1, 2, 3], ["a", "b"])))

# 指定填充值
print(list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="x")))




# 实战
# 假设有一批订单，按城市分组，算总金额，取前3名的城市
from itertools import groupby, islice

orders = [
    {"city": "北京", "amount": 100},
    {"city": "上海", "amount": 200},
    {"city": "北京", "amount": 150},
    {"city": "广州", "amount": 80},
    {"city": "上海", "amount": 120},
    {"city": "北京", "amount": 90},
]
# 按城市分组前必须排序
orders.sort(key=lambda x: x["city"])

city_total = []
# 计算每个城市的总金额
for city, group in groupby(orders, key=lambda x: x["city"]):
    total = sum(o["amount"] for o in group)
    city_total.append((city, total))

# 按总金额排序
city_total.sort(key=lambda x: x[1], reverse=True)
# 取前3名
print(list(islice(city_total, 3)))
