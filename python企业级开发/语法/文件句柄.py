from types import TracebackType


class MyFile:

    def __init__(self, name):
        print("__init__已执行，进行初始化")
        self.name = name

    def __enter__(self):
        print("__enter__已执行，进入with块，返回资源")
        return f"资源句柄 {self.name}"

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None):
        print("__exit__已执行，退出with块，释放资源")
        return False   # false表示不吞掉异常


print(">>>开始")
# 上下文管理器
with MyFile("test.txt") as f:
    print(f"在with块内部，拿到的f = {f}")

print(">>>结束")


