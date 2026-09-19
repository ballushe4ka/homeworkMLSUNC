import numpy as np


def prod_non_zero_diag(x):
    d = np.diagonal(x)
    return np.prod(d[d != 0])


def are_multisets_equal(x, y):
    return np.array_equal(np.sort(x), np.sort(y))

def max_after_zero(x):
    mask0 = (x[:-1] == 0)
    return np.max(x[1:][mask0])

def convert_image(img, coefs):
    return np.dot(img, coefs)

def run_length_encoding(x):
    if x.size == 0:
        return np.array([]), np.array([])
    swpos = np.where(x[:-1] != x[1:])[0]
    idxs = np.concatenate(([-1], swpos, [len(x) - 1]))
    a = x[idxs[1:]]
    cnt = np.diff(idxs)
    return a, cnt

def pairwise_distance(x, y):
    d = x[:, np.newaxis, :] - y[np.newaxis, :, :]
    return np.sqrt(np.sum(d ** 2, axis=2))
