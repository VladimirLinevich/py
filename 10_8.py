import numpy as np

def min_max_dist(*vectors):
    min1 = 0
    max1 = 0
    for i in range(len(vectors)):
        if i == 0: min1 = abs(np.linalg.norm(vectors[0] - vectors[1]))
        for j in range(i+1,len(vectors)):
            length = abs(np.linalg.norm(vectors[i] - vectors[j]))
            if length >= max1: max1 = length;
            if length <= min1: min1 = length
    return (min1,max1)