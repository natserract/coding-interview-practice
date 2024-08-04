"""

f(n) =
    - n: size of the input
    - So, n -> operations

Big-O Notation adalah sebuah cara atau metode untuk melakukan
analisa terhadap sebuah algoritma pemrograman terhadap waktu eksekusi.

Kompleksitas suatu algoritma dibagi menjadi 2, yaitu Time Complexity dan Space Complexity.

- Time Complexity: seberapa lama waktu yang diperlukan untuk menjalankan suatu algoritma.
- Space Complexity: seberapa besar memori yang kita gunakan untuk menjalankan suatu algoritma.

Notasi O 	 Istilah Lain    Jumlah Operasi 	Algoritma
O(n2):	     Quadratic 	     n2 	            Komparasi seluruh harga. Pengulangan dalam pengulangan
O(n): 	     Linear 	     2n 	            Mencari harga terendah dan tertinggi. 1 kali pengulangan
O(1): 	     Constant 	     2 	                Asumsi sudah diurut berdasarkan harga, tinggal mencari elemen pertama dan elemen terakhir

Example cases:
- Mencari harga terendah dan harga tertinggi
    data = [180, 78, 317]

    1. O(N^2): Quadratic Time Complexity
    for i in data:
        for j in data:
            # Operations

    n 	             3 	 5 	 10 	100
    Jumlah Operasi 	 9 	25 	 100 	10000

    Semakin banyak datanya semakin signifikan jumlah operasi yang dijalankan.

"""

data = [78, 180, 317, 512]

def quadratic_big_o(items: list):
    """
    O(n²) - Quadratic Time
    -> Ketika jumlah runtime / operasi dari fungsi kita adalah sebesar n^2, dimana n adalah jumlah input dari fungsi tersebut.
        Hal tersebut bisa terjadi karena kita menjalankan fungsi linear didalam fungsi linear (n*n).
        (for loop in for loop)
    """
    def find_max_price(items: list):
        max_price = 0
        for i in items: # O(n)
            for j in items: # O(n)
                if i > j:
                    max_price = i # O(1)

        # Total: O(n) * O(n) = O(n2)
        return max_price

    return (
        ('find_max_price', find_max_price(items))
    )

def linear_big_o(items: list):
    """
    O(n) - Linear Time
    -> Ketika jumlah runtime / operasi dari fungsi kita berbanding lurus dengan jumlah input yang diberikan.
    """
    def find_max_price(items: list):
        max_price = 0
        for i in items:
            if i > max_price:
                max_price = i

        return max_price

    def find_max_price_recurse(items: list, call = 0):
        max_price = 0

        n = call + 1
        if n == len(items):
            max_price = items[call]
        if items[call] > max_price:
            max_price = find_max_price_recurse(items, call + 1)

        return max_price

    return (
        ('find_max_price', find_max_price(items)),
        ('find_max_price_recurse', find_max_price_recurse(items))
    )

def constant_big_o(items: list):
    """
    O(1) - Constant Time
    -> Banyaknya input yang diberikan kepada sebuah algoritma, tidak akan mempengaruhi waktu proses (runtime) dari algoritma tersebut.
    """
    def find_max_price(items: list):
        # Suppose we already know which index that have the largest or smallest price
        # [78, 180, 317, 512] -> Max: index 2
        return items[3] # is constant, meaning it doesn't depend on the input size. Always one step operations

    return (
        ('find_max_price', find_max_price(items))
    )

def logaritmic_big_o(items: list):
    """
    O(log n) - Logarithmic Time
    -> ketika kita memberikan input sebesar n terhadap sebuah fungsi, jumlah tahapan yang dilakukan oleh fungsi tersebut berkurang berdasarkan suatu faktor.
    """
    def find_max_price(items: list) -> int:
        return _find_max_price(items, 0, len(items) - 1)

    def _find_max_price(items: list, left: int, right: int) -> int:
        if left == right:
            return items[left]

        mid = (left + right) // 2

        left_max = _find_max_price(items, left, mid)
        right_max = _find_max_price(items, mid + 1, right)

        return max(left_max, right_max)

    return (
        ('find_max_price', find_max_price(items))
    )


def run():
    print('On²', quadratic_big_o(data))
    print('O(n)', linear_big_o(data))
    print('O(1)', constant_big_o(data))
    print('O(log n)', logaritmic_big_o(data))
