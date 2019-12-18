# Uses python3

import sys


def negative_cycle(adj, cost, n):
    """
    This algorithm helps to find out if there a cycle with negative weight in directed graph with possibly negative edge
    weights and with n vertices and m edges.
    This task is solved by running relaxation of edges loops exactly (n - 1) times and on the n-th iteration check if
    there was any change. If change was, than negative cycle exists.
    :param adj: list of adjacency
    :param cost: list of weight costs
    :param n: number of vertices
    :return: 0 if there is no cycle, 1 if yes.
    """
    dist = [10 ** 8 for _ in range(n)]
    prev = [None for _ in range(n)]
    dist[0] = 0

    for _ in range(n-1):
        for u in range(n):
            for i in range(len(adj[u])):
                v = adj[u][i]
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    prev[v] = u

    had_change = 0
    for u in range(n):
        for i in range(len(adj[u])):
            v = adj[u][i]
            if dist[v] > dist[u] + cost[u][i]:
                had_change = 1
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u

    return had_change


if __name__ == '__main__':
    """
    Input sample: 
        4 4             // number or vertices and number of edges
        1 2 -5          // edge from 1 to 2 with weight -5
        4 1 2
        2 3 2
        3 1 1
    Output:
        1               // negative cycle exist 1 -> 2 -> 3
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

    # n = 4
    # adj = [[1], [2], [0], [0]]
    # cost = [[-5], [2], [1], [2]]

    print(negative_cycle(adj, cost, n))
