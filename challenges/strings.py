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

def find_first_non_repeating_char(text: str) -> str:
    """
    Input: aabccdeff
    Output: 'b'

    Input: aabbcc
    Output: ''

    Time complexity: O(n)
    Space complexity: O(n)
    """
    found = ""
    collect = {}
    for t in text:
        if t not in collect:
            collect[t] = 0 # O(n)

        if t in collect:
            collect[t] += 1 # O(n)

    for key, value in collect.items():
        if value == 1:
            found = key
            break;

    return found

def run():
    print('reverse_string', reverse_string('how are you'))
    print('find_first_non_repeating_char', find_first_non_repeating_char('aabbcc'))
