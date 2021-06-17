# Generator of sphere and loop point clouds
# using numpy


import numpy as np


#Sphere - ds4m (https://github.com/ds4m/topological-data-analysis)
points = 500
dimensions = 3
# Sample vectors from a normal distribution, ie from a Gaussian distribution, in Euclidean space.
vectors = np.random.randn(dimensions, points)
# Normalize each vector to have length one. These are our uniformly distributed points on the sphere.
vectors /= np.linalg.norm(vectors, axis=0)

np.savetxt('../point-clouds/sphere.txt', np.transpose(vectors), delimiter=', ')


# Loop
N = 100 # Number of points to sample
R = 4   # Big radius of torus
r = 1   # Little radius of torus
X = np.zeros((N, 3))
t = np.linspace(0, 2*np.pi, N)
X[:, 0] = (R + r*np.cos(2*t))*np.cos(t)
X[:, 1] = (R + r*np.cos(2*t))*np.sin(t)
X[:, 2] = r*np.sin(2*t)

np.savetxt('../point-clouds/loop.txt', np.vstack([X[:, 0], X[:, 1], X[:, 2]]).transpose(), delimiter=', ')

