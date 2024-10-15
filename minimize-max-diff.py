'''
You are given an array ‘A’ of length ‘N’ consisting only of positive integers and an integer ‘K’. You have to update every element of the array by increasing or decreasing its value by ‘K’ only once. Your task is to minimize the difference between maximum and minimum elements of the array after performing the increment or decrement on every element of the array.

Note: After the operation, every value of the array should remain non-negative.

For example:

Let’s say the array ‘A’ = [1, 2, 3, 4, 5] and ‘K’ = 2, then after increasing each element by ‘K’. The array ‘A’ will become [3, 4, 5, 6, 7]. So the maximum - minimum will be 7 - 3 = 4. 
'''


def minimizeIt(a: List[int], k: int) ->int:
    # Write your code here.
    n = len(a)
    if n == 1:
        return 0

    a.sort()
    mx = a[n-1]
    mn = a[0]
    df = mx - mn

    for i in range(1, n):
        if a[i] - k < 0:
            continue
        mx = max(a[i - 1] + k, a[n - 1] - k)
        mn = min(a[i] - k, a[0] + k)
        df = min(df, mx - mn)

    return df
