import matplotlib.pyplot as plt
import numpy as np
import laspy
from scipy import interpolate
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()


#Santoribiru Park (Kumamoto Prefecture, ~1000 points)
SantoribiruPark = laspy.read("../point-clouds/santoribiru_park.laz")

Santoribiru = fig.add_subplot(131, projection='3d')

c = np.arange(len(SantoribiruPark.Y)) / len(SantoribiruPark.Y)
Santoribiru.set_title('Santoribiru Park Point Cloud')
Santoribiru.scatter(SantoribiruPark.X, SantoribiruPark.Y, SantoribiruPark.Z, c = 0.5 * c, cmap = plt.cm.terrain, marker = 'o')


#Torus
Torus = np.loadtxt("../point-clouds/torus.txt", delimiter=',')

Tor = fig.add_subplot(132, projection='3d')

x = Torus[:,0]
y = Torus[:,1]
z = Torus[:,3]

c = np.arange(len(x)) / len(x)
Tor.set_title('Torus Point Cloud')
Tor.scatter(x, y, Torus[:,2], c = 0.5 * c, cmap = plt.cm.viridis, marker = 'o')
Tor.scatter(x, y, Torus[:,3], c = 0.5 * c, cmap = plt.cm.viridis, marker = 'o')


#Sphere
Sphere = np.loadtxt("../point-clouds/sphere.txt", delimiter=',')

Sph = fig.add_subplot(133, projection='3d')

x = Sphere[:,0]
y = Sphere[:,1]
z = Sphere[:,2]

c = np.arange(len(x)) / len(x)
Sph.set_title('Sphere Point Cloud')
Sph.scatter(x, y, z, c = 0.5 * c, cmap = plt.cm.plasma, marker = 'o')



plt.show()