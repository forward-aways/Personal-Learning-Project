from sympy import print_fcode

stack = []

# 入栈

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

# 看栈顶
print(stack[-1])

# 出栈
top = stack.pop()

print(top)
print(stack)




# 用链表实现栈

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:
    def __init__(self):
        self.top = None     # 栈顶指针，初始为None
        self._size = 0

    # 入栈
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top    # 新节点的next指针指向当前栈顶
        self.top = new_node         # 栈顶指针上移
        self._size += 1

    # 出栈
    def pop(self):
        if self.top is None:
            return None
        data = self.top.data        # 获取栈顶数据
        self.top = self.top.next    # 栈顶指针下移
        self._size -= 1

        return data

    # 看栈顶
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    # 判断栈是否为空
    def is_empty(self):
        return self.top is None

    # 获取栈的大小
    def size(self):
        return self._size


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.size())
print(s.is_empty())
