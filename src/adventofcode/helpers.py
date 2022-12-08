import collections
from itertools import islice


def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def transpose_matrix(matrix):
    return [list(x) for x in zip(*matrix)]


def rotate_matrix(matrix):
    return [list(x) for x in zip(*matrix[::-1])]


def flip_matrix(matrix):
    return [list(reversed(x)) for x in matrix]
