

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity    # 哈希表的容量
        self.table = [[] for _ in range(self.capacity)]    # 创建一个空列表，用于存储键值对
        self._size = 0

    # 哈希函数
    def _hash(self, key):
        return hash(key) % self.capacity

    # 插入键值对
    def put(self, key, value):
        idx = self._hash(key)                   # 计算哈希值
        bucket = self.table[idx]                # 拿到这个哈希值对应的桶

        for i, (k, v) in enumerate(bucket):     # 看key是否已存在
            if k == key:
                bucket[i] = (key, value)        # 存在就更新
                return

        bucket.append((key, value))             # 不存在就追加
        self._size += 1


    # 查找
    def get(self, key):
        idx = self._hash(key)           # 算下标
        bucket = self.table[idx]        # 拿到这个哈希值对应的桶

        for k, v in bucket:             # 遍历桶中的所有键值对
            if k == key:
                return v                # 返回对应的值

        raise KeyError(key)

    # 删除
    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]           # 删除对应的键值对
                self._size -= 1
                return

        raise KeyError(key)

    # 判断键是否存在
    def __contains__(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return True

        return False

    # 获取哈希表的大小
    def __len__(self):
        return self._size


ht = HashTable()

ht.put("apple", 1)
ht.put("banana", 2)
ht.put("cherry", 3)

print(ht.get("apple"))
print(ht.get("banana"))
print("cherry" in ht)
print("grape" in ht)


ht.delete("banana")
print("banana" in ht)
print(len(ht))