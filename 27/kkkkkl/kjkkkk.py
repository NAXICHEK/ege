from turtle import *
from random import random
from math import dist

def visual(clusters, k):
    tracer(0)
    up()
    for cluster in clusters:
        color = random(), random(), random()
        for x, y in cluster:
            goto(x * k, y * k)
            dot(4, color)
    update()
    done()

def dbscan(points, eps):
    clusters = []
    while points != []:
        cluster = [points[0]]
        points = points[1:]
        for star in cluster:
            new = [point for point in points if dist(point, star) <= eps]
            cluster += new
            for point in new: points.remove(point)
        clusters.append(cluster)
    return clusters

def get_centroid(cluster):
    min_sum_dist = 10**40
    final = []
    for centroid in cluster:
        sum_dist = sum(dist(point, centroid) for point in cluster)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            final = centroid
    return final

points = [list(map(float, line.replace(',', '.').split())) for line in open('27_A.txt')]
clusters = dbscan(points, 10)
# visual(clusters, 5)
centroids = [get_centroid(cluster) for cluster in clusters]
px = int(sum(x for x, y in centroids) / len(centroids) * 10000 // 1)
py = int(sum(y for x, y in centroids) / len(centroids) * 10000 // 1)
print(px, py)

points = [list(map(float, line.replace(',', '.').split())) for line in open('27_B.txt')]
clusters = dbscan(points, 10)
# visual(clusters, 5)
centroids = [get_centroid(cluster) for cluster in clusters]
px = int(sum(x for x, y in centroids) / len(centroids) * 10000 // 1)
py = int(sum(y for x, y in centroids) / len(centroids) * 10000 // 1)
print(px, py)
visual(clusters, 10)