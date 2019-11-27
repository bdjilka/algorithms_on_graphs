# Uses python3

import sys


class Queue:
    """
    Implementation of queue structure to process vertices processing. The maximum size of queue is bounded to total
    number of vertices (from 1 to 10**5)
    Has two methods: read from the start, add to the end.
    """
    def __init__(self):
        self.read = 0
        self.write = 0
        self.queue = list()

    def dequeue(self):
        if self.read == self.write and self.read > 0:
            return None
        if self.read >= len(self.queue):
            return None
        el = self.queue[self.read]
        self.read += 1
        return el

    def enqueue(self, el):
        self.queue.append(el)
        self.write = self.write + 1


def bipartite(adj):
    """
    This method checks whether given undirected graph is bipartite.
    [A graph is bipartite if its vertices can be colored with two colors (say, type1 and type2) such that the endpoints
    of each edge have different colors]

    This algorithm uses approach based on breadth first search. We mark first vertex as type1 equal to 0. Then find all
    vertices with distance equal one and mark them as type2 (1). Then move to layer with distance 2 and so on. Also,
    for each edge (u, v), where u is currently processing vertex, we make the following check: if vertex v is visited,
    we compare their color types and if they are the same, then edge (u, v) has vertices with equal color and graph is
    not bipartite.

    :param adj: list of adjacency
    :return: 1 if graph bipartite, 0 either.
    """
    queue = Queue()
    # list of colors, -1 means than vertex not marked yet
    color = [-1] * n

    # add first vertex to queue and mark it as 0
    queue.enqueue(0)
    color[0] = 0

    # continue process vertices until queue is not empty
    while queue.read != queue.write:
        u = queue.dequeue()
        # in case of some error probability during dequeue
        if u is None:
            return -1

        for v in adj[u]:
            if color[v] == -1:
                queue.enqueue(v)
                color[v] = int(not color[u])
            else:
                # terminate check if edge has same colored vertices, graph not bipartite
                if color[u] == color[v]:
                    return 0

    # all vertices was processed successfully, graph is bipartite
    return 1


if __name__ == '__main__':
    """
    Input sample:
        4 4             // number of vertices n and of edges m, 1 <= n <= 10**5, 0 <= m <= 10**5
        1 2             // edge between 1 and 2, not directed
        4 1
        2 3
        3 1
    Output sample:
        0               // 0 because graph is not bipartite
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
    print(bipartite(adj))
