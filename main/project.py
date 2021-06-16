import numpy as np
from ripser import ripser
from persim import plot_diagrams
import laspy

#Kumamoto Prefecture ~20k points - too many points to compute
#Kumamoto = laspy.read('kumamoto_prefecture_iwato_river_pointcloud.laz')
#dataset = np.vstack([Kumamoto.X, Kumamoto.Y]).transpose()

#Tsuchiyama (Kumamoto Prefecture, 8000 points) - too many points to compute
#tsu = laspy.read('Tsuchiyama.laz')
#dataset = np.vstack([tsu.X, tsu.Y]).transpose()

#Santoribiru Park (Kumamoto Prefecture, ~1000 points)
SantoribiruPark = laspy.read("../point-clouds/santoribiru_park.laz")
Santoribiru = np.vstack([SantoribiruPark.X, SantoribiruPark.Y]).transpose()
diagram = ripser(Santoribiru)['dgms']
plot_diagrams(diagram, show=True)

#Cyclooctane
Cyclooctane = np.loadtxt("../point-clouds/cyclooctane.txt", delimiter=',')
diagram = ripser(Cyclooctane)['dgms']
plot_diagrams(diagram, show=True)

#Bunny
#Bun = pye57.E57("../point-clouds/bunnyInt19.e57")
#Bunny = np.vstack([Bun["cartesianX"], Bun["cartesianY"]]).transpose()
#diagram = ripser(Bunny)['dgms']
#plot_diagrams(diagram, show=True)

#House
House = np.loadtxt("../point-clouds/house.txt", delimiter=',')
diagram = ripser(House)['dgms']
plot_diagrams(diagram, show=True)

#Torus
Torus = np.loadtxt("../point-clouds/torus.txt", delimiter=',')
diagram = ripser(Torus)['dgms']
plot_diagrams(diagram, show=True)

#Sphere
Sphere = np.loadtxt("../point-clouds/sphere.txt", delimiter=',')
diagram = ripser(Sphere)['dgms']
plot_diagrams(diagram, show=True)

#PiYG colormap