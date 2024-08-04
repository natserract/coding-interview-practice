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

data = [180, 78, 317]

def quadratic_big_o(items: list):
    """
    O(N^2) - Quadratic Time
    -> Ketika jumlah runtime / operasi dari fungsi kita adalah sebesar n^2, dimana n adalah jumlah input dari fungsi tersebut.
        Hal tersebut bisa terjadi karena kita menjalankan fungsi linear didalam fungsi linear (n*n).
        (for loop in for loop)
    """
    def find_the_min_or_max_price(items: list):
        max_price = 0
        min_price = 0
        for i in items:
            for j in items:
                if i > j:
                    max_price = i
                elif i < j:
                    min_price = i

        return min_price, max_price

    return (
        ('find_the_min_or_max_price', find_the_min_or_max_price(items))
    )

def linear_big_o(items: list):
    """
    O(N) - Linear Time
    -> Ketika jumlah runtime / operasi dari fungsi kita berbanding lurus dengan jumlah input yang diberikan.
    """
    def find_the_min_or_max_price(items: list):
        max_price = 0
        min_price = 0
        for i in items:
            if i > max_price:
                max_price = i
            elif i < max_price:
                min_price = i

        return min_price, max_price

    return (
        ('find_the_min_or_max_price', find_the_min_or_max_price(items))
    )

def constant_big_o(items: list):
    """
    O(1) - Constant Time
    -> Banyaknya input yang diberikan kepada sebuah algoritma, tidak akan mempengaruhi waktu proses (runtime) dari algoritma tersebut.
    """
    def find_the_min_or_max_price(items: list):
        # Already know which index that have the largest or smallest price
        # [180, 78, 317] -> Min: index 1, Max: index 2
        return items[1], items[2]

    return (
        ('find_the_min_or_max_price', find_the_min_or_max_price(items))
    )

def run():
    print('O(N^2)', quadratic_big_o(data))
    print('O(N)', linear_big_o(data))
    print('O(1)', constant_big_o(data))
