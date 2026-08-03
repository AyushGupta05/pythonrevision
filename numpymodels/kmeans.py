import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1.0, 1.0],
    [1.5, 2.0],
    [3.0, 4.0],
    [5.0, 7.0],
    [3.5, 5.0],
    [4.5, 5.0],
    [3.5, 4.5]
])

max_iterations = 100
tolerance = 1e-4

k = 2
rng = np.random.default_rng(42)
indices = rng.choice(len(X), size = k, replace = False)

centroids = X[indices].copy()
for _ in range(max_iterations):
    distances = np.sum((X[:, None, :] - centroids[None, :, :]) ** 2,axis=2)
    labels = np.argmin(distances, axis=1)

    new_centroids = np.array([X[labels == cluster].mean(axis=0)for cluster in range(k)])
    movement = np.linalg.norm(new_centroids - centroids)
    if movement < tolerance:
            break

for cluster in range(k):
    points = X[labels == cluster]

    plt.scatter(
        points[:, 0],
        points[:, 1]
    )

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=200
)

plt.show()