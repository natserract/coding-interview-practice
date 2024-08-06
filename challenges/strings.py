def reverse_string(text: str):
    """
    Input: 'i like this program very much'
    Output: 'hcum yrev margorp siht ekil i'

    Input: 'how are you'
    Output: 'uoy era woh'

    Time complexity: O(n)
    Space complexity: O(n)
    """
    arr = [t for t in text]
    start = 0
    end = len(arr) - 1

    while(start < end):
        arr[start], arr[end] = arr[end], arr[start] #swap
        start += 1
        end -= 1

    return ''.join(arr)

def run():
    print('reverse_string', reverse_string('how are you'))
