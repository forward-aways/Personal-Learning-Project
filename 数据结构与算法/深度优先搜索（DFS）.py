

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()     # 记录访问过的节点

    visited.add(node)           # 标记当前节点为已访问
    print(node, end='')         # 输出当前节点

    for neighbor in graph[node]:                                   # 遍历当前节点的邻居
        if neighbor not in visited:                                # 如果邻居节点未访问过
            dfs(graph, neighbor, visited)      # 递归访问邻居节点


    return visited


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"],
}

dfs(graph, "A")
