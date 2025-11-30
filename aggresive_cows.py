def agg_cows(n, c, arr):
    arr.sort()

    lo = 0
    hi = arr[-1] - arr[0]

    def viable(x):
        cnt = 1
        curr = arr[0]

        for i in range(1, n):
            if arr[i] - curr >= x:
                curr = arr[i]
                cnt += 1

        return cnt == c

    while lo < hi:
        mid = (lo + hi + 1) // 2

        if viable(mid):
            lo = mid
        else:
            hi = mid - 1

    return mid

if __name__ == '__main__':
    for _ in range(int(input())):
        n, c = map(int, input().strip().split())
        arr = []
        for i in range(n):
            arr.append(int(input()))
    print(agg_cows(n, c, arr))
        

