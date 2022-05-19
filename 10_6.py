import numpy as np


def get_chess(a):
    chess = np.zeros((a,a),dtype=int)
    chess[::2,1::2] = 1
    chess[1::2,::2] = 1
    np.random.permutation
    
    return chess
    
    
print (get_chess(5))
print (2**32)