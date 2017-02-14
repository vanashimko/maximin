from math import sqrt
from random import randrange
from collections import defaultdict
from statistics import mean


def distance(a, b):
    if len(a) != len(b):
        raise ValueError('Vectors have different dimensions')
    return sqrt(sum(((x-y)**2 for x, y in zip(a, b))))


def allocate_clusters(vectors, centroids):
    clusters = defaultdict(list)
    for vector_index, vector in enumerate(vectors):
        centroid = min(centroids, key=lambda x: distance(vector, x))
        clusters[centroid].append(vector_index)
    return clusters


def average_centroids_distance(clusters):
    centroids = list(clusters.keys())
    if len(centroids) > 1:
        return mean((distance(x, y) for i, x in enumerate(centroids) for y in centroids[i+1:]))
    else:
        return 0


def get_new_centroid_index(vectors, clusters):
    result = None
    max_in_clusters = []
    for centroid, cluster in clusters.items():
        max_in_clusters.append(max(((i, distance(centroid, vectors[i])) for i in cluster), key=(lambda x: x[1])))
    total_max = max(max_in_clusters, key=(lambda x: x[1]))
    if total_max[1] > (average_centroids_distance(clusters) / 2):
        result = total_max[0]
    return result


def maximin(vectors):
    centroids = []
    clusters = None
    new_centroid_index = randrange(len(vectors))
    while new_centroid_index is not None:
        centroids.append(vectors[new_centroid_index])
        clusters = allocate_clusters(vectors, centroids)
        new_centroid_index = get_new_centroid_index(vectors, clusters)
    return clusters
