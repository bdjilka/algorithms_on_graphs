# Uses python3

import sys


def reach(adj, visited, x, y):
    """

    :param adj: adjacency list, indexes start from 0
    :param visited: boolean list of nodes length, show was node checked or not
    :param x: current node index, that is being checked
    :param y: target node index to which path is required
    :return: 1 if path exists, 0 if not

    This is a realization of path search between two nodes. On each iteration we check if there is a node with index 'y'
    in adjacency list corresponding to node 'x'. If adj[x] contains y than we found path and can return 1. If not,
    than we initialize the same search for all adj[x] nodes. We continue search until there are exist unvisited
    reachable nodes.
    """
    visited[x] = 1

    if len(adj[x]) > 0:
        try:
            i = adj[x].index(y)
            if i > -1:
                return 1
        except ValueError:
            pass

        for v in adj[x]:
            if visited[v] == 0:
                res = reach(adj, visited, v, y)
                if res == 1:
                    return 1

        return 0

    return 0


if __name__ == '__main__':
    """
    Input sample:
        4 2         // number of vertices and number of edges
        1 2         // edge between node 1 and 2
        3 2         // edge between node 3 and 2 
        1 4         // check if there is a path between nodes 1 and 4
    Output:
        0           // 0 because path doesn't exist, 1 will be in case path exists 
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    visited = [0 for _ in range(n)]
    print(reach(adj, visited, x, y))
