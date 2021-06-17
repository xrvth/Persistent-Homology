import numpy as np
from ripser import ripser
from persim import plot_diagrams
import laspy
import matplotlib.pyplot as plt
import gudhi

def PlotBarcode(PointCloud):
	RipsComplex = gudhi.RipsComplex(points=PointCloud, max_edge_length=0.8)
	SimplexTree = RipsComplex.create_simplex_tree(max_dimension=3)
	Diagram = SimplexTree.persistence(min_persistence=0.0)
	return Diagram

#Santoribiru Park (Kumamoto Prefecture, ~1000 points)
SantoribiruPark = laspy.read("../point-clouds/santoribiru_park.laz")
Santoribiru = np.vstack([SantoribiruPark.X, SantoribiruPark.Y, SantoribiruPark.Z]).transpose()
diagram = ripser(Santoribiru)['dgms']
plot_diagrams(diagram, show=True, title="Persistent Homology of Santoribiru Park Topography") 
#bar = gudhi.plot_persistence_barcode(PlotBarcode(Santoribiru))
#bar.set_title("Persistence Barcode of Santoribiru Park Topography")
#plt.show()
#UserWarning: Attempting to set identical left == right == 0.0 results in singular transformations; automatically expanding.
	#axes.axis([axis_start, infinity, 0, ind])

#Cyclooctane
Cyclooctane = np.loadtxt("../point-clouds/cyclooctane.txt", delimiter=',')
diagram = ripser(Cyclooctane)['dgms']
plot_diagrams(diagram, show=True, title="Persistent Homology of Cyclooctane")
bar = gudhi.plot_persistence_barcode(PlotBarcode(Cyclooctane))
bar.set_title("Persistence Barcode of Cyclooctane")
plt.show()

#Bunny
#Bun = pye57.E57("../point-clouds/bunnyInt19.e57")
#Bunny = np.vstack([Bun["cartesianX"], Bun["cartesianY"]]).transpose()
#diagram = ripser(Bunny)['dgms']
#plot_diagrams(diagram, show=True)
#gudhi.plot_persistence_barcode(PlotBarcode(Bunny))
#plt.show()

#House
House = np.loadtxt("../point-clouds/house.txt", delimiter=',')
diagram = ripser(House)['dgms']
plot_diagrams(diagram, show=True, title="Persistent Homology of 5 points on a plane")
#bar = gudhi.plot_persistence_barcode(PlotBarcode(House))
#bar.set_title("Persistence Barcode of 5 points on a plane")
#plt.show()
#UserWarning: Attempting to set identical left == right == 0.0 results in singular transformations; automatically expanding.
	#axes.axis([axis_start, infinity, 0, ind])

#Torus
Torus = np.loadtxt("../point-clouds/torus.txt", delimiter=',')
diagram = ripser(Torus)['dgms']
plot_diagrams(diagram, show=True, title="Persistent Homology of Torus")
bar = gudhi.plot_persistence_barcode(PlotBarcode(Torus))
bar.set_title("Persistence Barcode of Torus")
plt.show()

#Sphere
Sphere = np.loadtxt("../point-clouds/sphere.txt", delimiter=',')
diagram = ripser(Sphere)['dgms']
plot_diagrams(diagram, show=True, title="Persistent Homology of Sphere")
bar = gudhi.plot_persistence_barcode(PlotBarcode(Sphere))
bar.set_title("Persistence Barcode of Sphere")
plt.show()

#Loop
Loop = np.loadtxt("../point-clouds/loop.txt", delimiter=',')
diagram = ripser(Loop)['dgms']
plot_diagrams(diagram, show=True, title="Persistent Homology of Loop")
bar = gudhi.plot_persistence_barcode(PlotBarcode(Loop))
bar.set_title("Persistence Barcode of Loop")
plt.show()

#Cube
Cube = np.loadtxt("../point-clouds/cube.txt", delimiter=' ')
diagram = ripser(Cube)['dgms']
plot_diagrams(diagram, show=True, title="Persistent Homology of Cube")
bar = gudhi.plot_persistence_barcode(PlotBarcode(Cube))
bar.set_title("Persistence Barcode of Cube")
plt.show()


# Datasets below unfortunately have too many points to process

#Kumamoto Prefecture ~20k points - too many points to compute
#Kumamoto = laspy.read('kumamoto_prefecture_iwato_river_pointcloud.laz')
#dataset = np.vstack([Kumamoto.X, Kumamoto.Y]).transpose()

#Tsuchiyama (Kumamoto Prefecture, 8000 points) - too many points to compute
#tsu = laspy.read('Tsuchiyama.laz')
#dataset = np.vstack([tsu.X, tsu.Y]).transpose()