def dict_iterations(data: dict):
    # with key pairs
    for key, value in data.items():
        print('Value', key, value)

def run():
    data = {'name': 'James Harden', 'points': 38, 'age': 30}
    print('dict_iterations', dict_iterations(data))
