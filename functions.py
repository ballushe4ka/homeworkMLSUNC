def prod_non_zero_diag(x):
    res = 1
    mini = min(len(x),len(x[0]))
    for i in range(mini):
        if x[i][i] != 0:
            res *= (int)x[i][i]
    return res

def are_multisets_equal(x, y):
    if len(x) != len(y):
        return False
    return sorted(x) == sorted(y)

def max_after_zero(x):
    mx = None
    for i in range(1,len(x)):
        if x[i-1] == 0:
            if mx is None or x[i] > mx:
                mx = x[i]
    return mx

def convert_image(img, coefs):
    h = len(img)
    w = len(img[0])
    res = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            val = 0
            for k in range(3):
                val += img[i][j][k] * coefs[k]
            res[i][j] = val
    return res


def run_length_encoding(x):
    if len(x) == 0:
        return [], []
    a = []
    cnt = []
    cur = x[0]
    c = 1
    for i in range(1, len(x)):
        if x[i] == cur:
            c+=1
        else:
            a.append(cur)
            cnt.append(c)
            cur = x[i]
            c = 1
    a.append(cur)
    cnt.append(c)
    return a, cnt

def pairwise_distance(x, y):
    n = len(x)
    m = len(y)
    dist = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            d = 0
            for k in range(len(x[i])):
                d += (x[i][k]-y[j][k])**2
            dist[i][j] = d ** 0.5
