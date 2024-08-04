
colors = ['red', 'blue', 'green']

def find_index(d: list, i: int):
    return d[i]

def iterations(d: list):
    # for loop
    forloop_iter = []
    for v in d:
        forloop_iter.append(v)

    # inline for loop
    forloop_inline_iter = [
        v for v in d
    ]

    # while loop
    i = 0
    whileloop_iter = []
    while i < len(d):
        whileloop_iter.append(d[i])
        i += 1

    return forloop_iter, forloop_inline_iter, whileloop_iter

def range_list(end = 10):
    values = []
    for i in range(end):
        values.append(i)

    return values

def insert_list(d: list, value: str):
    d.insert(len(d), value)
    return d

def concat(d: list, new: list):
    return d + [*new]

def reverse_list(d: list):
    values = d.copy()
    values.reverse()
    return values

def pop_list(d: list, i: int):
    values = d.copy()
    values.pop(i)
    return values

def run():
    print('find_index', find_index(colors, 0))
    print('iterations', iterations(colors))
    print('range', range_list())
    print('insert_list', insert_list(colors, 'yellow'))
    print('concat', concat(colors, ['brown']))
    print('reverse_list', reverse_list(colors))
    print('pop_list', pop_list(colors, 1))
