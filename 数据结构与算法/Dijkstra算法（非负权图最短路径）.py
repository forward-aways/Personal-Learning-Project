"""
Dijkstra算法（非负权图最短路径）, 时间复杂度 O((V+E)logV)
相比 Bellman-Ford 算法，Dijkstra 算法只能处理非负权边
"""

import heapq

def dijkstra(graph, start):
    """
    Dijkstra算法，用于计算带权图中从起点到其他所有节点的最短路径。
    graph: {节点: [(邻居，权重), ...]}
    返回: {节点: 最短距离}
    """

    # 距离表，初始都是无穷大
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # 优先队列：(距离，节点), 谁距离小谁先出队
    pq = [(0, start)]
    visited = set()

    while pq:
        dist, node = heapq.heappop(pq)  # 取出距离最小的

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:            # 遍历当前节点的邻居
            new_dist = dist + weight                    # 算经过当前节点到邻居节点的距离
            if new_dist < distances[neighbor]:          # 如果经过当前节点的距离更小
                distances[neighbor] = new_dist          # 更新邻居节点的距离
                heapq.heappush(pq, (new_dist, neighbor))  # 将邻居节点加入优先队列


    return distances

