# Uses python3

import sys


class Queue:
    """
    Implementation of queue structure to process vertices processing. The maximum size of queue is bounded to total
    number of vertices (from 2 to 10**5)
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


def distance(n, adj, s, t):
    """
    Algorithm that finds the shortest distance between given node s and all other nodes in unordered graph.
    As tasks need only shortest path between nodes s and t, we return only one value from the list of found
    distances, if there is no path -1 is returned.

    To solve such problem used breadth first search in graph, that has running time of O(n + m), where n - number of
    vertices, m - number of edges.
    For representation of edges used adjacency list, as the most suitable and efficient for current algorithm.

    :param n: number of vertices
    :param adj: adjacency list
    :param s: source vertex
    :param t: target vertex
    :return: minimum path
    """
    queue = Queue()

    # list of distances, -1 means than vertex in unreachable
    dist = [-1] * n
    dist[s] = 0

    # add root vertex to queue
    queue.enqueue(s)

    # continue process vertices until queue is not empty
    while queue.read != queue.write:
        u = queue.dequeue()

        # in case of some error probability during dequeue
        if u is None:
            return -1

        for v in adj[u]:
            if dist[v] == -1:
                queue.enqueue(v)
                dist[v] = dist[u] + 1

    return dist[t]


if __name__ == '__main__':
    """
    Input sample:
        4 4             // number of vertices n and of edges m, 2 <= n <= 10**5, 0 <= m <= 10**5
        1 2             // edge between 1 and 2, not directed
        4 1
        2 3
        3 1
        2 4             // nodes to find distance s = 2 and t = 4, s != t, 1 <= s, t <= n
    Output sample:
        2               // minimum path between nodes 2 and 4
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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1

    print(distance(n, adj, s, t))
