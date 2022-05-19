import numpy as np

def any_normal(*vectors):
    for i in range(len(vectors)):
        for j in range(i+1,len(vectors)):
            if np.dot(vectors[i],vectors[j]) == 0:
                return True
    return False