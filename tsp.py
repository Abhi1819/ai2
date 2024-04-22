import numpy as np
import sys


def nearest_neighbor(distances, start=0):
    n = len(distances)
    visited = [False] * n
    path = [start]
    visited[start] = True
    for _ in range(n - 1):
        nearest_city = min((i for i in range(n) if not visited[i]), key=lambda x: distances[path[-1]][x])
        path.append(nearest_city)
        visited[nearest_city] = True
    return path


# Example usage
distances = np.array([[0, 1, 2, 3], [1, 0, 4, 5], [2, 4, 0, 6], [3, 5, 6, 0]])
print(nearest_neighbor(distances))
