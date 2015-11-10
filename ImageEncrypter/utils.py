__author__ = 'james'

import time



def main():
    start = time.time()
    two_kdp(25000, 12412513, 345987439589897)
    end = time.time()
    print end - start


def two_kdp(size, k1, k2):

    # Initialization
    y = 1
    z = 1
    p = k1 * k2

    C = range(size)

    # Generate set
    for i in range(size):
        w = y + (k2 + i)
        x = z + (k1 + i)

        y += w
        z += x + y

        p = (p + y + z) % size

        C[i] = int(p)

    # Replace duplicates
    U = set([])
    K = 0
    for i in range(size):
        if C[i] in U:
            C[i] = -1
            K += 1
        else:
            U.add(C[i])

    # Get missing element set
    I = set(range(size))
    M = list(I.difference(U))

    M.sort(reverse=True)

    miss_counter = 0
    for i in range(size):
        if C[i] == -1:
            C[i] = M[miss_counter]
            miss_counter += 1

    if miss_counter != len(M):
        assert False

    return C

def euclid(a, b):
    pass

if __name__ == '__main__':
    main()