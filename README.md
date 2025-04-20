# Irrotational 2D Fluid Mechanics Simulation

This repository gathers our Python codes to solve irrotational 2D fluid mechanics simulations, which we wrote as part of our [Elements of Fluid Mechanics](https://www.programmes.uliege.be/cocoon/20242025/cours/MECA0011-2.html) course at [Uliège](https://www.uliege.be).


It gives tools to simulate irrotational flow with an asymetric obstacle in it.


## User guide
Run the main.py file to plot a variety of graphs.

CL directory contains the files describing the problem : 
- 2-dom.txt describes wether or not a point is part of the domain : 0 = outside the domain, 1 = inside and 2 = boundary node. (File was given to us by our instructor)
- 2-dom_bords.txt asigns a different number to each distinct edge, in order to asign uniform boundary conditions easily
- 2-contourObj.txt provides the (x, y) coordinates of the obstacle. (File was given to us by our instructor)
- 2-num.txt asigns a different number to each node and is used for the computation of the Laplacien. (File was given to us by our instructor)
- kutta.txt is used to select the stopping point for kutta conditions by writing a 3 at the right spot




## Requirements
- [Python](https://www.python.org/downloads/)
- Matplotlib, Numpy and Scipy modules
  
## License


## Contributors 
- Lhoest Guy-Louis
- Leyen Benjamin
- Hendrickx Victor 
