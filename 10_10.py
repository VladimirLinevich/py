import numpy as np

def get_loto(num):
    loto = list()
    for i in range(num):
        loto.append(np.random.randint(1,101, size=(5, 5)))
    loto = np.array(loto)
    loto = loto.astype(np.int8)
    return np.array(loto)