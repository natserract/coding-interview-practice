import re

def read_number_of_spaces(text: str):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    spaces = 0
    for s in text:
        if s == " ":
            spaces += 1

    return spaces

def remove_unecessary_spaces(text: str, pattern = "[.]"):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    text = re.sub(rf'{pattern}', '', text)
    text = ' '.join(text.split())
    return text

def swap(arr, i, j):
    '''same as
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    '''
    arr[i], arr[j] = arr[j], arr[i]

def sort_binary_string(text: str):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Workflow:
    Input: 1 0 0 1 1 0

    - Check angka 1 dan 0 di setiap iterasi
    - Case diatas, terdapat 3 jumlah angka 1, dan 3 jumlah angka 0
    - Angka 1 -> muncul pada index: 0, 3, 4
    - Angka 0 -> muncul pada index 1, 2, 5
    - Jadi, pada setiap iterasi:

        ------------------------------------------------------------------------------
        Iterasi 1:
        1(idx: 0)     0(idx: 1)     0(idx: 2)   1(idx: 3)     1(idx: 4)     0(idx: 5)

        Process iterasi 1:
        => index: 0
        => head = 0, tail = 0
        =>
        => [1, 0, 0, 1, 1, 0]
        => arr[i] == '1': True, arr[i] == '0': False
        => Swap: arr[0] <swap> arr[0] = no effect
        =>
        => [1, 0, 0, 1, 1, 0]
        => arr[i] == '1': True, arr[i] == '0': False
        => head = 1, tail = 0
        => head > tail = True
        => head = 1, tail = 1

        ----
        Iterasi 2:
        1(idx: 0)     0(idx: 1)     0(idx: 2)   1(idx: 3)     1(idx: 4)     0(idx: 5)

        Process iterasi 2:
        => index: 1
        => head = 1, tail = 1
        =>
        => [1, 0, 0, 1, 1, 0]
        => arr[i] == '1': False, arr[i] == '0': True
        => Swap: arr[1] <swap> arr[1] = no effect
        =>
        => [1, 0, 0, 1, 1, 0]
        => arr[i] == '1': False, arr[i] == '0': True
        => head = 1, tail = 2
        => head > tail = False
        => head = 1, tail = 2

        ----
        Iterasi 3:
        1(idx: 0)     0(idx: 1)     0(idx: 2)   1(idx: 3)     1(idx: 4)     0(idx: 5)

        Process iterasi 3:
        => index: 2
        => head = 1, tail = 2
        =>
        => [1, 0, 0, 1, 1, 0]
        => arr[i] == '1': False, arr[i] == '0': True
        => Swap: arr[2] <swap> arr[2] = no effect
        =>
        => [1, 0, 0, 1, 1, 0]
        => arr[i] == '1': False, arr[i] == '0': True
        => head = 1, tail = 3
        => head > tail = False
        => head = 1, tail = 3

        ----
        Iterasi 4:
        1(idx: 0)     1(idx: 1)     0(idx: 2)   0(idx: 3)     1(idx: 4)     0(idx: 5)

        Process iterasi 4:
        => index: 3
        => head = 1, tail = 3
        =>
        => [1, 0, 0, 1, 1, 0]
        => arr[i] == '1': True, arr[i] == '0': False
        => Swap: arr[3] <swap> arr[1] = [1, 1, 0, 0, 1, 0]
        =>
        => [1, 1, 0, 0, 1, 0]
        => arr[i] == '1': False, arr[i] == '0': True
        => head = 2, tail = 4
        => head > tail = False
        => head = 2, tail = 4

        ----
        Iterasi 5:
        1(idx: 0)     1(idx: 1)     1(idx: 2)   0(idx: 3)     0(idx: 4)     0(idx: 5)

        Process iterasi 5:
        => index: 4
        => head = 2, tail = 4
        =>
        => [1, 1, 0, 0, 1, 0]
        => hearr[i] == '1': True, arr[i] == '0': False
        => Swap: arr[2] <swap> arr[4] = [1, 1, 1, 0, 0, 0]
        =>
        => [1, 1, 1, 0, 0, 0]
        => arr[i] == '1': False, arr[i] == '0': True
        => head = 3, tail = 4
        => head > tail = False
        => head = 3, tail = 4

        ----
        Iterasi 6:
        1(idx: 0)     1(idx: 1)     1(idx: 2)   0(idx: 3)     0(idx: 4)     0(idx: 5)

        Process iterasi 6:
        => index: 5
        => head = 3, tail = 4
        =>
        => [1, 1, 1, 0, 0, 0]
        => arr[i] == '1': False, arr[i] == '0': True
        => Swap: arr[index] <swap> arr[3] = [1, 1, 1, 0, 0, 0]
        =>
        => [1, 1, 1, 0, 0, 0]
        => arr[i] == '1': False, arr[i] == '0': True
        => head = 3, tail = 6
        => head > tail = False
        => head = 3, tail = 6

        ------------------------------------------------------------------------------

    - PS:
       1. head, tail ini sbg pointer utk menentukan posisi setiap step nya.
          Nntinya digunakan untuk swapping berdasarkan posisi step tersebut

       2. Statement: head > tail, untuk memastikan posisi tail tidak overlap dari head nya. Minimal, sama atau lebih.
          Contoh case: 111010, 3 angka yang sama di depan.

    - If the all inputs integer, use `bubble_sort` instead
    """
    head, tail = 0, 0

    arr = [t for t in text]
    n = len(arr)
    for i in range(n):
        if arr[i] == '1':
            swap(arr, i, head)
            head += 1

        if head > tail:
            tail = head

        if arr[i] == '0':
            swap(arr, i, tail)
            tail += 1

    return ''.join(arr)

def vowels(text: str):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    count = 0
    structure = 'aeuio'

    vowels_dict = {
        'a': True, 'A': True,
        'e': True, 'E': True,
        'i': True, 'I': True,
        'o': True, 'O': True,
        'u': True, 'U': True
    }
    for w in text:
        if w in vowels_dict:
            count += 1

    return count

def fizz_buzz(n: int) -> list:
    """
    Input: 5
    Output: [1, 2, "Fizz", 4, "Buzz"]

    Input: 15
    Output: [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

    Time complexity: O(n)
    Space complexity: O(n)
    """
    results = []
    for i in range(1, n+1):
        # Fizz
        if i % 3 == 0:
            results.append("Fizz")

        # Buzz
        elif i % 5 == 0:
            results.append("Buzz")

        else:
            results.append(i)

    return results

def run():
    print('sort_binary_string', sort_binary_string("100110")) #111000
    print('read_number_of_spaces', read_number_of_spaces('    Jack in    America'))
    print('remove_unecessary_spaces', remove_unecessary_spaces('    Jack in    America.  '))
    print('vowels', vowels('google'))
    print('fizz_buzz', fizz_buzz(15))
