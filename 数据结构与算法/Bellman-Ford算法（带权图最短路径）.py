"""
Bellman-Ford 算法（带权图最短路径）, 时间复杂度 O(V*E)
相比 Dijkstra 算法，Bellman-Ford 算法可以回头修正距离，因此可以处理负权边。
且可以处理负权环。
"""

def bellman_ford(edges, start, num_nodes):
    """
    Bellman-Ford 算法

    Args:
        edges:     边列表，每条边是 (起点, 终点, 权重)
        start:     起点
        num_nodes: 节点总数

    Returns:
        距离字典，或 None（如果存在负权环）
    """

    # 初始化距离为无穷大
    distances = {}
    for u, v, w in edges:
        distances[u] = float("inf")
        distances[v] = float("inf")

    distances[start] = 0

    # 松弛V-1轮
    for i in range(num_nodes - 1):
        updated = False
        for u, v, w in edges:                       # 遍历所有边
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                updated = True

        if not updated:
            break

    for u, v, w in edges:                           # 遍历所有边
        if distances[u] + w < distances[v]:
            print("存在负权环")
            return None

    return distances


edges = [
    ("A", "B", 1),
    ("A", "C", 4),
    ("B", "C", 2),
    ("B", "D", -3),
    ("C", "D", 1),
]


result = bellman_ford(edges, "A", 4)
print(result)