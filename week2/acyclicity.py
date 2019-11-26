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
        self.clock = 1
        self.post = [0 for _ in range(n)]
        self.visited = [0 for _ in range(n)]

    def previsit(self):
        self.clock += 1

    def postvisit(self, v):
        self.post[v] = self.clock
        self.clock += 1

    def explore(self, v):
        self.visited[v] = 1
        self.previsit()
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

    def acyclic(self):
        """
        Checks whether graph has edge in that post visit index of source vertex is less than its end vertex post index.
        If such edge exists than graph is not acyclic.
        :return: 1 if there is cycle, 0 in other case.
        """
        self.deepFirstSearch()

        for v in range(self.size):
            for u in self.adj[v]:
                if self.post[v] < self.post[u]:
                    return 1

        return 0


if __name__ == '__main__':
    """
    Input sample:
        4 4     // number of vertices n and number of edges m, 1 <= n, m <= 1000
        1 2     // edge from vertex 1 to vertex 2
        4 1
        2 3
        3 1 
    Output:
        1       // cycle exists: 3 -> 1 -> 2 -> 3
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    graph = Graph(adj, n)
    print(graph.acyclic())
