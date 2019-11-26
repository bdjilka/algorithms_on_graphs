# Uses python3

import sys


def explore(v, visited, adj):
    visited[v] = 1
    for w in adj[v]:
        if visited[w] == 0:
            visited = explore(w, visited, adj)
    return visited


def number_of_components(adj):
    """
    Finds number of connected components of given unordered graph. On each iteration for unvisited vertex explored all
    reachable from it vertices, after that number of components incremented. Iteration continues until unvisited
    vertices exists.
    :param adj: adjacency list
    :return: number of connected components
    """
    count = 0
    visited = [0 for _ in range(len(adj))]
    for v in range(len(adj)):
        if visited[v] == 0:
            visited = explore(v, visited, adj)
            count += 1
    return count


if __name__ == '__main__':
    """
    Input sample:
        4 2         // number of vertices and number of edges
        1 2         // edge between 1 and 2
        3 2         // edge between 3 and 2
    Output:
        2           // 2 connected components
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
