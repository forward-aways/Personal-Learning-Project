from collections import deque

# 双端队列，可以从前端和后端添加和删除元素
queue = deque()

# 入队， deque底层使用双向链表实现
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# 出队，从左边
front = queue.popleft()

print(front)
print(queue)



# 队列的链表实现

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None   # 队头指针，初始为None
        self.rear = None    # 队尾指针，初始为None
        self._size = 0      # 队列的大小，初始为0

    # 入队，从队尾入队
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:             # 队列为空
            self.front = new_node         # 队列为空，新节点同时作为队头和队尾
            self.rear = new_node
        else:
            self.rear.next = new_node     # 新节点添加到队尾
            self.rear = new_node          # 更新队尾指针

        self._size += 1

    # 出队，从队头出队
    def dequeue(self):

        if self.front is None:           # 队列为空
            return None

        data = self.front.data           # 获取队头元素的数据
        self.front = self.front.next     # 更新队头指针
        if self.front is None:           # 队列为空
            self.rear = None             # 队列为空，队尾指针也为空
        self._size -= 1

        return data

    # 查看队头元素
    def peek(self):
        if self.front is None:           # 队列为空
            return None
        return self.front.data           # 返回队头元素的数据

    # 队列是否为空
    def is_empty(self):              # 队列是否为空
        return self.front is None    # 队列为空，返回True，否则返回False

    # 队列的大小
    def size(self):
        return self._size



q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.size())

