#cube
import numpy as np
xAngle = 0
yAngle = 0
zAngle = 0

verticies=[
    [[-2.000,-2.000000,2.000000]],
    [[-2.000,2.000000,2.000000]],
    [[-2.000,-2.000000,-2.000000]],
    [[-2.000,2.000000,-2.000000]],
    
    [[2.000,-2.000000,2.000000]],
    [[2.000,2.000000,2.000000]],
    [[2.000,-2.000000,-2.000000]],
    [[2.000,2.000000,-2.000000]],


]
faces=[
    [[1,0,2],[7,0,2],[5,0,2]],
    [[1,0,2],[3,0,2],[7,0,2]], 
    [[1,0,6],[4,0,6],[3,0,6]], 
    [[1,0,6],[2,0,6],[4,0,6]], 
    [[3,0,3],[8,0,3],[7,0,3]], 
    [[3,0,3],[4,0,3],[8,0,3]], 
    [[5,0,5],[7,0,5],[8,0,5]], 
    [[5,0,5],[8,0,5],[6,0,5]], 
    [[1,0,4],[5,0,4],[6,0,4]], 
    [[1,0,4],[6,0,4],[2,0,4]], 
    [[2,0,1],[6,0,1],[8,0,1]], 
    [[2,0,1],[8,0,1],[4,0,1]], 

]
