
colors = ['red', 'blue', 'green']

def find_index(items: list, i: int):
    return items[i]

def iterations(items: list):
    # for loop
    forloop_iter = []
    for v in items:
        forloop_iter.append(v)

    # inline for loop
    forloop_inline_iter = [
        v for v in items
    ]

    # inline condition for loop
    forloop_inline_iter_cond = [
        v.upper() if v =='red' else v for v in items
    ]

    # while loop
    i = 0
    whileloop_iter = []
    while i < len(items):
        whileloop_iter.append(items[i])
        i += 1

    return forloop_iter, forloop_inline_iter, forloop_inline_iter_cond, whileloop_iter

def range_list(end = 10):
    values = []
    for i in range(end):
        values.append(i)

    return values

def insert_list(items: list, value: str):
    items.insert(len(items), value)
    return items

def concat(items: list, new: list):
    return items + [*new]

def reverse_list(items: list):
    values = items.copy()
    values.reverse()
    return values

def pop_list(items: list, i: int):
    values = items.copy()
    values.pop(i)
    return values

def range_full(items: list, start: int, end: int):
    return items[start:end]

def run():
    print('find_index', find_index(colors, 0))
    print('iterations', iterations(colors))
    print('range', range_list())
    print('insert_list', insert_list(colors, 'yellow'))
    print('concat', concat(colors, ['brown']))
    print('reverse_list', reverse_list(colors))
    print('pop_list', pop_list(colors, 1))
    print('range_full', range_full(colors, 0, 2))
