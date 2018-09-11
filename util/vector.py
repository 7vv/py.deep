def vector_add(v, w): return [_v + _w for _v, _w in zip(v, w)]
def vector_substract(v, w): return [_v - _w for _v, _w in zip(v, w)]    
def vector_sum(vectors): return reduce(vector_add, vectors)
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def scalar_multiply(c, v): return [c * _v for _v in v]    

def test():
    v = [1, 0, 2, 3, 4, 5, 6, 1, 3]
    w = [2, 1, 4, 5, 6, 2, 2, 4, 5]

    print(vector_add(v, w))
    print(vector_substract(v, w))    

test()