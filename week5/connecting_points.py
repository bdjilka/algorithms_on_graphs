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


def minimum_distance(x, y):
    """
    The goal is to build roads between some pairs of the given cities such that there is a path between any two cities
    and the total length of the roads is minimized.
    Given n points on a plane, connect them with segments of minimum total length such that there is a path between
    any two points. Recall that the length of a segment with endpoints (x1, y1) and (x2, y2) is equal to
    sqrt((x1^2 − x2^2)^2 + (y1^2 − y2^2)^2).

    To compute minimum spanning tree used Kruskal's algorithm: repeatedly add the next lightest edge if this doesn't
    produce a cycle.
    To store edges in non-decreasing order used priority queue, to control cycle check used structure of disjoint sets.

    :param x: list of x positions
    :param y: list of y positions
    :return: minimal total distance
    """
    result = 0.

    n = len(x)
    parent = [0] * n
    rank = [0] * n

    q = queue.PriorityQueue()
    q = compute_distances(q, x, y)
    x_set = list()

    for u in range(n):
        parent, rank = make_set(parent, rank, u)

    while len(q.queue) > 0:
        edge = q.get()
        if find(parent, edge.u) != find(parent, edge.v):
            x_set.append(edge)
            result += edge.value
            parent, rank = union(parent, rank, edge.u, edge.v)

    return result


if __name__ == '__main__':
    """
    Input sample:
        4               // number of cities
        0 0             // x and y position of city
        0 1
        1 0
        1 1
    Output:
        3.000000000     // minimum distance, that connects all dots
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    print("{0:.9f}".format(minimum_distance(x, y)))
