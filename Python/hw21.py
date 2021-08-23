from itertools import chain


def generator():

    l1 = [x for x in range(1, 10)]
    l2 = [x for x in range(2, 20)]

    y_iter = list(chain(l1, l2))
    y_iter.sort()
    return y_iter


print(generator())


# print([list(x for x in range(1, 4)), list(x for x in range(2, 5))])
