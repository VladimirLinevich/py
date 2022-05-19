import numpy as np

def shuffle_seed(array):
    seed_arr = np.random.randint(2**32-1,size = 1)
    np.random.seed(seed_arr)
    shuffle_arr = np.random.permutation(array)
    return (shuffle_arr,seed_arr)