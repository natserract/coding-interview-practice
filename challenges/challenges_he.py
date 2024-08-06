
def plus_minus(arr):
    """
    Time complexity: O(n) - Linear Time
    Space complexity: O(1) - Constant Time
    """
    positive, negative, zero = (0, 0, 0)
    for v in arr:
        # find zero number:
        if v == 0:
            zero += 1
        # find negative number
        elif v < 0:
            negative += 1
        # find positive number
        elif v > 0:
            positive += 1

    length = len(arr)
    print(positive / length)
    print(negative / length)
    print(zero / length)

def mini_max_sum(arr: list[int]):
    """
    Input: 1, 2, 3, 4, 5
    Output: 10 14

    Iterations
    Index 0, Except 1 -> 2 + 3 + 4 + 5 = 14
    Index 1, Except 2 -> 1 + 3 + 4 + 5 = 13
    ..

    Time complexity: O(n^2)
    Space complexity: O(n^2)

    """
    results: list[int] = []
    for i in range(len(arr)):
        left_node, right_node = arr[:i+1], arr[i+1:] # O(n) -> Because in loop, space complexity becomes O(n^2)
        left_node.pop(i) # Remove curr index

        # Sum
        result = sum(left_node + right_node)
        results.append(result)

    print('mini_max_sum', min(results), max(results))

def run():
    plus_minus([-4, 3, -9, 0, 4, 1])
    mini_max_sum([1, 2, 3, 4, 5])
