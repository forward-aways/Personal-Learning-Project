from collections import deque

from sympy.series import order


def bfs(graph, start):
    visited = set()               # 记录访问过的节点
    queue = deque([start])        # 使用队列记录待访问的节点
    visited.add(start)

    order = []                    # 记录访问顺序

    while queue:
        node = queue.popleft()          # 从队列中取出一个节点
        order.append(node)              # 记录访问顺序

        for neighbor in graph[node]:        # 遍历当前节点的邻居
            if neighbor not in visited:     # 如果邻居节点未访问过
                visited.add(neighbor)       # 标记邻居节点为已访问
                queue.append(neighbor)      # 将邻居节点加入队列

    return order


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"],
}

print(bfs(graph, "A"))