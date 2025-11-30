def painters_partition_min_time(arr, k):
    def viable(x):
        painters = 1
        curr_sum = 0
        for l in arr:
            if x < l:
                return False
            
            if curr_sum + l > x:
                painters += 1
                curr_sum = l
            else:
                curr_sum += l

        
        return painters <= k
    
    lo, hi = max(arr), sum(arr)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if viable(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo