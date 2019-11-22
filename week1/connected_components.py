# Uses python3

import sys


def explore(v, visited, adj):
    visited[v] = 1
    for w in adj[v]:
        if visited[w] == 0:
            visited = explore(w, visited, adj)
    return visited


def number_of_components(adj):
    count = 0
    visited = [0 for _ in range(len(adj))]
    for v in range(len(adj)):
        if visited[v] == 0:
            visited = explore(v, visited, adj)
            count += 1
    return count


if __name__ == '__main__':
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
