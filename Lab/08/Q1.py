import numpy as np
myArray = np.array(np.arange(21,50))
myArray = myArray[myArray%2==0]
print(myArray)
