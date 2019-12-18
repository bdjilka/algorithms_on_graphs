# Uses python3

import sys
from collections import namedtuple
import heapq

Node = namedtuple("Node", ["index", "dist"])


# realization based on priority queue, somehow not working properly
# def parent_of_node(i):
#     """
#     Index of parent node of some node with index i
#     """
#     return (i - 1) // 2
#
#
# def left_child(i):
#     """
#     Index of left child of node with index i
#     """
#     return 2 * i + 1
#
#
# def right_child(i):
#     """
#     Index of right child of node with index i
#     """
#     return 2 * i + 2
#
#
# def compare(el1, el2):
#     if el1.dist == el2.dist:
#         return el1.index < el2.index
#     else:
#         return el1.dist < el2.dist
#
#
# def sift_up(arr, i):
#     """
#     Method, that moving element closer to the root.
#     :param arr: global list of integers
#     :param i: index of element
#     :return: modified list arr
#     """
#     while i > 0 and compare(arr[i], arr[parent_of_node(i)]):
#         arr[parent_of_node(i)], arr[i] = arr[i], arr[parent_of_node(i)]
#         i = parent_of_node(i)
#     return arr
#
#
# def sift_down(arr, n, i):
#     """
#     Method, that finds right position for element with index i in array arr.
#     Assume that arr[i] is parent for two elements: right_children and left_children. We find least element between this
#     three and swaps if needed least element with parent. Then we repeat this operation, where parent element is that
#     with which ex-parent was swapped.
#     :param arr: global list of integers
#     :param n: size of list
#     :param i: index, parent element
#     :return: modified list arr
#     """
#     min_index = i
#
#     left = left_child(i)
#
#     if left < n and compare(arr[left], arr[min_index]):
#         min_index = left
#
#     right = right_child(i)
#
#     if right < n and compare(arr[right], arr[min_index]):
#         min_index = right
#
#     if i != min_index:
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#         arr = sift_down(arr, n, min_index)
#
#     return arr
#
#
# def extract(h, n):
#     res = h[0]
#
#     h[0] = h[-1]
#     del h[-1]
#
#     n = n - 1
#
#     h = sift_down(h, n, 0)
#     return res, h, n
#
#
# def change_priority(h, v, path):
#     i = 0
#     while h[i].index != v:
#         i += 1
#
#     old_path = h[i][0]
#     h[i] = Node(path, v)
#
#     if path < old_path:
#         h = sift_up(h, i)
#     else:
#         h = sift_down(h, len(h), i)
#
#     return h


def get_min(visited, dist, n):
    """
    Finds next unvisited vertex with minimum distance.
    :param visited: boolean array, representing whether vertex is visited
    :param dist: array of distances
    :param n: number of vertices
    :return: index of vertex
    """
    min_v = n
    min_dist = float('inf')

    for v in range(n):
        if not visited[v] and dist[v] < min_dist:
            min_v = v
            min_dist = dist[v]

    return min_v


def distance(adj, cost, s, t):
    """
    Given an directed graph with positive edge weights and with n vertices and m edges as well as two vertices s and v,
    compute the weight of a shortest path between s and t (that is, the minimum total weight of a path from s to t).

    Shortest path computed using Dijkstra algorithm.

    :param adj: list of adjacency
    :param cost: list of adjacency weights
    :param s: source vertex
    :param t: target vertex
    :return: length of shortest path, -1 if path does not exist
    """
    n = len(adj)
    dist = [float('inf') for _ in range(n)]
    dist[s] = 0
    visited = [False for _ in range(n)]

    # h = queue.PriorityQueue()
    # for i in range(n):
    #     h.put(Node(i, dist[i]))
    #
    # while not h.empty():
    #     u = h.get()
    #     index = u.index
    #     for i in range(len(adj[index])):
    #         v = adj[index][i]
    #         if dist[v] > dist[index] + cost[index][i]:
    #             dist[v] = dist[index] + cost[index][i]
    #             prev[v] = index
    #             if not h.empty():
    #                 h.put(Node(i, dist[v]))

    for _ in range(n - 1):
        v = get_min(visited, dist, n)
        if v == n:
            break
        visited[v] = True
        for i in range(len(adj[v])):
            u = adj[v][i]
            if not visited[u] and dist[u] > dist[v] + cost[v][i]:
                dist[u] = dist[v] + cost[v][i]

    if dist[t] == float('inf'):
        return -1

    return dist[t]


if __name__ == '__main__':
    """
    Input sample:
        4 4         // n - vertices, m - edges, 1 <= n <= 10**4, 0 <= m <= 10**5, weights non-negative integers <= 10**3
        1 2 1       // edge from vertex 1 to vertex 2 with weight 1
        4 1 2 
        2 3 2 
        1 3 5 
        1 3         // between vertices 1 and 3 needed to find shortest path
    Output:
        3           // total weight of shortest path
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    s, t = data[0] - 1, data[1] - 1

    print(distance(adj, cost, s, t))
