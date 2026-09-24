# 节点类
class Node:
    def __init__(self, data):
        self.data = data    # 存数据
        self.next = None    # 指向下一个节点，初始为None


# 链表
class LinkedList:
    def __init__(self):
        self.head = None                # 头结点，默认空链表

    # 在链表头部插入节点
    def insert_at_head(self, data):
        new_node = Node(data)           # 创建新节点
        new_node.next = self.head       # 新节点指向当前头结点
        self.head = new_node            # 更新头结点为新节点

    # 在链表尾部插入节点
    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:              # 空链表
            self.head = new_node           # 更新头结点为新节点
            return

        current = self.head                # 指针
        while current.next is not None:    # 遍历链表
            current = current.next
        current.next = new_node            # 插入新节点

    # 查找
    def search(self, data):
        current = self.head

        while current.next is not None:
            if current.data == data:
                return True
            current = current.next

        return False

    # 删除节点
    def delete(self, data):
        if self.head is None:                    # 空链表
            return

        if self.head.data == data:               # 删除头结点
            self.head = self.head.next
            return

        current = self.head                         # 指针

        while current.next is not None:             # 遍历链表
            if current.next.data == data:            # 判断条件
                current.next = current.next.next    # 删除节点
                return

            current = current.next

    # 显示链表
    def display(self):
        elements = []
        current = self.head

        while current is not None:
               elements.append(str(current.data))
               current = current.next

        print(" -> ".join(elements) + " -> None")


    def __len__(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count



if __name__ == '__main__':
    lst = LinkedList()

    lst.insert_at_head(30)
    lst.insert_at_head(20)
    lst.insert_at_head(10)
    lst.display()


    lst.insert_at_tail(40)
    lst.display()

    print("查找 20: ", lst.search(20))
    print("查找 50: ", lst.search(50))


    lst.delete(20)
    lst.display()

    lst.delete(10)
    lst.display()

    print("长度: ", len(lst))