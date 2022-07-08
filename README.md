# Persistent-Homology

### _**General info**_
Python project about persistent homology applications.

[Link to presentation.](https://www.canva.com/design/DAEiC76bTFQ/sbs5Sdsk2lrd-ezDuLLSWg/view?utm_content=DAEiC76bTFQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

<img src="https://raw.githubusercontent.com/xrvth/Persistent-Homology/main/pictures/example.png" width="700"/>

Visualisation of Point Clouds

<img src="https://raw.githubusercontent.com/xrvth/Persistent-Homology/main/pictures/visualisation.png" width="700"/>
	
	
### _**Technologies**_
Project is created with:
* Python 3.8.6
* [Ripser library](https://github.com/Ripser/ripser)
* Persim library
* [Laspy library](https://pypi.org/project/laspy/)
* GUDHI library
* Matplotlib library (for visualisations)
* NumPy library (for generator)

### _**Sources used**_
* Point Cloud Data of Kumamoto Prefecture, Tsuchiyama and Santorigiru Park from [OpenTopography](https://opentopography.org/)
* Bunny Point Cloud Data from [libe57](http://www.libe57.org/data.html)
* Point Cloud Datas from [Data Science for Mathematicians](https://github.com/ds4m/topological-data-analysis/tree/master/persistent-homology/point_clouds)

### _**How to use**_
For this project you have to install some additional Python libraries.
```
$ pip install ripser
$ pip install laspy
$ pip install gudhi
```
To run, you only need to (python v3 needed):
```
$ python3 project.py
```
To run `project_visualisation.py` you need to install matplotlib.
```
$ pip install matplotlib
$ python3 project_visualisation.py
```

