# Uses python3

import sys

sys.setrecursionlimit(200000)


def postvisit(v, post, clock):
    post[clock] = v
    clock += 1
    return post, clock


def explore(v, re_adj, visited, post, clock):
    """
    Explores connected components and marks their post order indexes.
    :param v: current vertex
    :param re_adj: adjacency list of reversed direction
    :param visited: boolean list
    :param post: array, where post index 'i' has vertex post[i]
    :param clock: post order counter
    :return:
    """
    visited[v] = 1
    for u in re_adj[v]:
        if not visited[u]:
            visited, post, clock = explore(u, re_adj, visited, post, clock)
    post, clock = postvisit(v, post, clock)

    return visited, post, clock


def explore_simple(v, adj, visited):
    """
    Explores connected components
    :param v: current vertex
    :param adj: adjacency list
    :param visited: boolean list
    :return: visited vertices list
    """
    visited[v] = 1
    for u in adj[v]:
        if not visited[u]:
            visited = explore_simple(u, adj, visited)
    return visited


def deepFirstSearch(post, re_adj, n):
    """
    Visits all nodes and marks their post visit indexes. Fills list post[].
    :param post: array, where post index 'i' has vertex post[i]
    :param re_adj: adjacency list of reversed direction
    :param n: number of vertices
    :return: post order indexes list
    """
    clock = 0
    visited = [0] * n

    for v in range(n):
        if not visited[v]:
            visited, post, clock = explore(v, re_adj, visited, post, clock)

    return post


def number_of_strongly_connected_components(adj, re_adj, n):
    """
    This method computes the number of strongly connected components (SCC) of a given directed graph with n vertices and
    m edges. Running time equal to O(m + n).
    Firstly, it searches post order indexes in graph with reversed edges, the reversed graph helps us because largest
    remaining post number comes from sink component.
    Then in reversed order of post indexes we complete explore method for each vertex if it is not visited yet. After
    each iteration number of SCCs increases.
    :param adj: list of adjacency
    :param re_adj: list of adjacency of reversed graph
    :param n: number of vertices
    :return: number of SCCs
    """
    result = 0

    post = [-1] * n
    post = deepFirstSearch(post, re_adj, n)

    visited = [0] * n
    for i in range(n - 1, -1, -1):
        v = post[i]
        if not visited[v]:
            explore_simple(v, adj, visited)
            result += 1

    return result


if __name__ == '__main__':
    """
    Input sample:
        4 4             // n=4 number of vertices, m=4 number of edges, 1 <= n, m <= 10**4
        1 2             // edge from vertex 1 to vertex 2
        4 1
        2 3
        3 1
    Output:
        2               // graph contains 2 strongly connected components
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    re_adj = [[] for _ in range(n)]

    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        re_adj[b - 1].append(a - 1)

    print(number_of_strongly_connected_components(adj, re_adj, n))
