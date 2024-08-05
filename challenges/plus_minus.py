##############
# Solution 1 #
##############
def plusMinus_1(arr):
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

def run():
    plusMinus_1([-4, 3, -9, 0, 4, 1])
