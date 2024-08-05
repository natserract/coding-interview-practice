"""
Recursive

Pros: DRY, Readability
Cons: Large Stack (call stack structure)
"""
def factorize(n:int):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if n == 0:
        return 1

    return n * factorize(n-1)

def run():
    print('factorize', factorize(5))
