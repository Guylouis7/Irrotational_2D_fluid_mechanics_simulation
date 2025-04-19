Instructions for Using the Initialization Files
Tips for Importing Files into Python

Use the numpy.loadtxt function, specifying the data type and file path.
Example:

import numpy as np
my_array = np.loadtxt(path + '\\1-num.txt', dtype=int)

    Note: The spatial discretization step is specified below.

Conventions

Each configuration includes 2 or 3 matrix files:

    dom – Domain Matrix
    Identifies node types:

        0: Nodes not to be computed (surrounded by a fringe of zeros)

        1: Internal computational nodes

        2: Dirichlet boundary condition nodes

    num – Node Numbering Matrix

        Provides a unique number for each computational node

        Numbering starts at 1 and is used to structure the system of equations

        For further explanation, refer to the introductory session or consult with student tutors

    cl – Dirichlet Condition Values (only for the straight channel test case)

    2-contourObj.txt – Obstacle Contour Indices (only for the complex channel with an obstacle)

Additional Information

    Straight Channel: Spatial step = 0.5 m

    Channel with Obstacle: Spatial step = 0.01 cm
