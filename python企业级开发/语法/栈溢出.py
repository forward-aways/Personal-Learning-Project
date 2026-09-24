import sys
import psutil
# 打印当前进程的内存使用（单位：MB）

def recurse(n):
    print(f"当前进程内存使用: {psutil.Process().memory_info().rss / 1024 / 1024:.1f} MB")
    print(f"当前递归深度: {n}")
    return recurse(n + 1)

print("默认限制:", sys.getrecursionlimit())

try:
    recurse(0)
except RecursionError as e:
    print("栈溢出被接住:", e)
    print("程序还能继续跑")

print("程序正常结束")