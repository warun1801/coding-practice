def reverseArr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArray(arr: list, k: int) -> list:
    '''
    This question is tricky to solve in O(1)
    Needs concept that rotate by k to left is same as
    1. Reverse from 0 to k - 1
    2. Reverse from k to n - 1
    3. Reverse from 0 to n - 1
    In this order

    for eg. 1 2 3 4 5, k = 3
    desired output should be 4 5 1 2 3
    so basically
    1. 3 2 1 4 5
    2. 3 2 1 5 4
    3. 4 5 1 2 3
    '''

    n = len(arr)
    k = k % n

    reverseArr(arr, 0, k - 1)
    reverseArr(arr, k, n - 1)
    reverseArr(arr, 0, n - 1)

    return arr