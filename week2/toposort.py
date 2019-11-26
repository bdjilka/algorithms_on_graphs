# Uses python3

import sys


class Graph:
    """
    Class representing directed graph defined with the help of adjacency list.
    """
    def __init__(self, adj, n):
        """
        Initialization.
        :param adj: list of adjacency
        :param n: number of vertices
        """
        self.adj = adj
        self.size = n
        self.clock = 0
        self.post = [0 for _ in range(n)]
        self.visited = [0 for _ in range(n)]

    def postvisit(self, v):
        self.post[v] = self.clock
        self.clock += 1

    def explore(self, v):
        self.visited[v] = 1
        for u in self.adj[v]:
            if not self.visited[u]:
                self.explore(u)
        self.postvisit(v)

    def deepFirstSearch(self):
        """
        Visits all nodes and marks their post visit indexes. Fills list post[].
        """
        for v in range(self.size):
            if not self.visited[v]:
                self.explore(v)

    def topoSort(self):
        """
        Method that computes a topological ordering of a given directed acyclic graph.
        :return: order list
        """
        self.deepFirstSearch()
        order = [0 for _ in range(self.size)]
        for i in range(self.size):
            order[self.size - self.post[i] - 1] = i
        return order


if __name__ == '__main__':
    """
    Input sample:
        4 3         // number of vertices n and number of edges m, 1 <= n, m <= 10**5
        1 2         // edge from 1 to 2
        4 1         // edge from 4 to 1
        3 1         // edge from 3 to 1
    Output:
        4 3 1 2     // topological ordering
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    # adj = [[], [], [0], []]
    # n = 4

    graph = Graph(adj, n)
    order = graph.topoSort()
    for x in order:
        print(x + 1, end=' ')
