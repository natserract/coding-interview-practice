def reverse_array(arr: list):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Workflow:
    Input: [1, 2, 3, 4, 5]

    Iterasi:
    ------------------------------------------------------------------------------
    Iterasi 0:
    1 2 3 4 5

    start = 0, end = 4
    swap: arr[4] <swap> arr[0] = [5, 2, 3, 4, 1]
    start = 1, end = 3

    ---
    Iterasi 0:
    input: [1, 2, 3, 4, 5]
    start = 0, end = 4
    swap: arr[4] <swap> arr[0] = [5, 2, 3, 4, 1]
    start = 1, end = 3

    ---
    Iterasi 1:
    input: [5, 2, 3, 4, 1]
    start = 1, end = 3
    swap: arr[1] <swap> arr[3] = [5, 4, 3, 2, 1]
    start = 2, end = 2

    ---
    Stop, start == end
    ------------------------------------------------------------------------------
    """
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start] # swap
        start += 1
        end -= 1

    return arr

def middle(arr: list):
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    return arr[len(arr) // 2]

def run():
    data = [1, 9, 2, 3, 6, 4, 5]
    print('reverse_array', reverse_array(data))
    print('middle', middle(data))
