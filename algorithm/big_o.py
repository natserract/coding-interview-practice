"""
Big-O Notation adalah sebuah cara atau metode untuk melakukan
analisa terhadap sebuah algoritma pemrograman terhadap waktu eksekusi.

f(n) =
    - n: size of the input
    - So, n -> operations

Constant: O(1)
Linear time: O(n)
Logarithmic time: O(n log n)
Quadratic time: O(n^2)
Exponential time: O(2^n)
Factorial time: O(n!)

Kompleksitas suatu algoritma dibagi menjadi 2, yaitu Time Complexity dan Space Complexity.

- Time Complexity: seberapa lama waktu yang diperlukan untuk menjalankan suatu algoritma.
- Space Complexity: seberapa besar memori yang kita gunakan untuk menjalankan suatu algoritma.

Steps:
1. Brute force: yg penting bekerja dl
2. Finds worst case
3. Find best case
4. Optimize
5. Test
"""
from typing import Callable


def constant_big_o():
    """
    O(1) - Constant
    -> Banyaknya input yang diberikan kepada sebuah algoritma, tidak akan mempengaruhi waktu proses (runtime) dari algoritma tersebut.

    Time Complexity: O(1)
    Penjelasan:
        a + b => Kenapa O(1), karena operasi ini tidak berjalan berdasarkan seberapa besar nilai inputnya.
                Melainkan hanya berlaku satu/single operasi alias waktunya constant.
                Meskipun, nilainya sampai 1000 sekalipun.

                Yang dilihat adalah proses runtime (jumlah operasi) nya, artinya jika memang a + b itu
                menghabiskan waktu `0.01ms`. Even itu di for loop, `a + b` proses runtimenya tetap `0.01ms`
                yakni constant / fixed / sama.

                PS:
                Simplenya, O(1) berjalan berdasarkan performa dari hardware / server bukan dari nilai input.
                Contoh proses runtime yang berjalan berdasarkan nilai input,

                    Example 1:
                    def length(items: list):
                        total = 0
                        for i in items:
                            total += 1
                        return total

                    -> length([1, 2, 4]) # 3

                    Example 2:
                    def map(items: list, fn: Callable):
                        return [fn(v) for v in items]

                    -> map([1, 2, 3], lambda x: x + 1) # 2, 3, 4

    >> O(1): "One operation at a time"

    Contoh Time Complexity - O(1) lainnya:
        - return True
        - Array.push()
        - Array.indexOf


    Space complexity: O(1)
        def sum(a: int, b: int):
            return a + b

        Fungsi tersebut tidak membuat alokasi memori baru / variabel tambahan yang bertambah besar seiring bertambahnya input.
        Jadi hanya constant, tidak bergantung pada input.

        Example space complexity: O(n)
        def fill(n: int):
            results = []
            for i in range(n):
                results.append(i)

        ->  fill(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        Space memory dari `results` akan bertambah seiring makin besarnya `n`

    Contoh Space complexity - O(1) lainnya:
        - def length(items: list):
            '''
            Time complexity: O(n)
            Space complexity: O(1)
            '''
            total = 0
            for i in items:
                total += 1
            return total

        - def is_include(items: list, target: int):
            '''
            Time complexity: O(n)
            Space complexity: O(1)
            '''
            contained = False
            for val in items:
                if target == val:
                    contained = True
                    break;
            return contained
    """
    def sum(a: int, b: int):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return a + b

    return (
        ('sum', sum(1, 2)),
    )

def linear_big_o():
    """
    O(n) - Linear
    -> Waktu eksekusi operasi bertambah seiring bertambahnya jumlah input
    """
    def for_each(fn: Callable, items: list):
        """
        Time complexity: O(n)
        Space complexity: O(1) / depends on `fn`
        """
        for i in range(len(items)):
            fn(items[i])

        return items

    return (
        ('for_each', for_each(print, [1, 5, 3]))
    )
def run():
    print('O(1)', constant_big_o())
    print('O(n)', linear_big_o())
