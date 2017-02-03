from math import sqrt
from random import sample


def sqr(a):
    return a*a


def distance(a, b):
    if len(a) != len(b):
        raise ValueError('Vectors have different dimensions')
    return sqrt(sum(map(sqr, (x-y for x, y in zip(a, b)))))


def maximin(vectors, clusters_count):
	pass
