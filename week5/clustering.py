# Uses python3
import queue
import sys
import math
from collections import namedtuple

Dist = namedtuple("Dist", ["value", "u", "v"])


def make_set(parent, rank, u):
    parent[u] = u
    rank[u] = 0
    return parent, rank


def find(parent, u):
    while u != parent[u]:
        u = parent[u]
    return u


def union(parent, rank, u, v):
    u_id = find(parent, u)
    v_id = find(parent, v)
    if u_id == v_id:
        return
    if rank[u_id] > rank[v_id]:
        parent[v_id] = u_id
    else:
        parent[u_id] = v_id
        if rank[u_id] == rank[v_id]:
            rank[v_id] += 1
    return parent, rank


def compute_distances(q, x, y):
    n = len(x)
    for i in range(n):
        for j in range(i + 1, n):
            value = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            q.put(Dist(value, i, j))
    return q


def clustering(x, y, k):
    """
    Given n points on a plane and an integer k, compute the largest possible value of d such that the given points can
    be partitioned into k non-empty subsets in such a way that the distance between any two points from different
    subsets is at least d.

    This task is solved using slightly modified Kruskal's algorithm. At the beginning we have n disjoint sets, where
    n is number of points, after each union operation, number of such sets is decreasing by one. So we continue to run
    union iterations until we reach required number of clusters. After that, we look for the smallest distance between
    two point, that belongs to different clusters.

    Kruskal's algorithm idea: repeatedly add the next lightest edge if this doesn't produce a cycle.
    To store edges in non-decreasing order used priority queue, to control cycle check used structure of disjoint sets.

    :param x: list of x coordinates
    :param y: list of y coordinates
    :param k: number of clusters
    :return: minimum distance between two clusters
    """
    n = len(x)
    total = n
    parent = [0] * n
    rank = [0] * n
    q = queue.PriorityQueue()
    q = compute_distances(q, x, y)
    for u in range(n):
        parent, rank = make_set(parent, rank, u)

    while len(q.queue) > 0 and total > k:
        edge = q.get()
        if find(parent, edge.u) != find(parent, edge.v):
            parent, rank = union(parent, rank, edge.u, edge.v)
            total -= 1

    edge = q.get()
    while find(parent, edge.u) == find(parent, edge.v):
        edge = q.get()

    return edge.value


if __name__ == '__main__':
    """
    Input sample:
        12              // number of points
        7 6             // (x, y) coordinates of first point
        4 3
        5 1
        1 7
        2 7
        5 7
        3 3
        7 8
        2 8
        4 4
        6 7
        2 6
        3               // number of clusters
    Output:
        2.828427124746  // minimum distances between any two clusters
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]

    print("{0:.9f}".format(clustering(x, y, k)))
