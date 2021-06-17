# 3D Visualisation of used point clouds
# using matplotlib


import matplotlib.pyplot as plt
import numpy as np
import laspy
from scipy import interpolate
from mpl_toolkits.mplot3d import axes3d


fig = plt.figure()


#Santoribiru Park (Kumamoto Prefecture, ~1000 points)
SantoribiruPark = laspy.read("../point-clouds/santoribiru_park.laz")

Santoribiru = fig.add_subplot(231, projection='3d')

c = np.arange(len(SantoribiruPark.Y)) / len(SantoribiruPark.Y)
Santoribiru.set_title('Santoribiru Park Point Cloud')
Santoribiru.scatter(SantoribiruPark.X, SantoribiruPark.Y, SantoribiruPark.Z, c = 0.5 * c, cmap = plt.cm.gray, marker = 'o')


#Torus
Torus = np.loadtxt("../point-clouds/torus.txt", delimiter=',')

Tor = fig.add_subplot(232, projection='3d')

x = Torus[:,0]
y = Torus[:,1]
z = Torus[:,3]

c = np.arange(len(x)) / len(x)
Tor.set_title('Torus Point Cloud')
Tor.scatter(x, y, Torus[:,2], c = 0.5 * c, cmap = plt.cm.viridis, marker = 'o')
Tor.scatter(x, y, Torus[:,3], c = 0.5 * c, cmap = plt.cm.viridis, marker = 'o')


#Sphere
Sphere = np.loadtxt("../point-clouds/sphere.txt", delimiter=',')

Sph = fig.add_subplot(233, projection='3d')

x = Sphere[:,0]
y = Sphere[:,1]
z = Sphere[:,2]

c = np.arange(len(x)) / len(x)
Sph.set_title('Sphere Point Cloud')
Sph.scatter(x, y, z, c = 0.5 * c, cmap = plt.cm.plasma, marker = 'o')


#Loop
Loop = np.loadtxt("../point-clouds/loop.txt", delimiter=',')

Loo = fig.add_subplot(234, projection='3d')

x = Loop[:,0]
y = Loop[:,1]
z = Loop[:,2]

c = np.arange(len(x)) / len(x)
Loo.set_title('Loop Point Cloud')
Loo.scatter(x, y, z, c = 0.5 * c, cmap = plt.cm.cool, marker = 'o')


#Cube
Cube = np.loadtxt("../point-clouds/cube.txt", delimiter=' ')

Cub = fig.add_subplot(235, projection='3d')

x = Cube[:,0]
y = Cube[:,1]
z = Cube[:,2]

c = np.arange(len(x)) / len(x)
Cub.set_title('Loop Point Cloud')
Cub.scatter(x, y, z, c = 0.5 * c, cmap = plt.cm.cool, marker = 'o')


plt.show()