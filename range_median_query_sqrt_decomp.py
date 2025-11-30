import math, bisect

def coord_compression(A):
    # Global coordinate compression
    """
    So the idea is basically to assign a special no. m to every number x in the array
    where m is a number in the Value Set of Array A (at max n)
    and x is any number in array

    Useful when len(array) is much lesser than the value set to compress the differences in the array nums
    Especially useful for medians and stuff
    """

    vals = sorted(set(A))
    comp = {v: i + 1 for i, v in enumerate(vals)}
    M = len(vals)
    return [comp[x] for x in A], vals

def sqrt_decomp(A):
    n = len(A)

    B = math.isqrt(n) or 1
    blocks = []
    blocks_pref_sum = []
    block_max = [] # optional
    block_min = [] # optional
    for start in range(0, n, B): # O(root(n))
        blk = A[start: start + B]
        blk.sort() # O(root(n)log(n))
        blocks.append(blk)
        ps = [0] # to make it one indexed ie ps[idx] -> sum of idx no. of elems
        for x in blk: # O(root(n))
            ps.append(ps[-1] + x)
        blocks_pref_sum.append(ps)
        block_max.append(blk[-1])
        block_min.append(blk[0])

    # total -> O(root(n) * (root(n) log(n) + root(n))) -> O(nlog(n))

    return B, blocks, blocks_pref_sum, block_max, block_min


def count_le(l, r, x, A):
    """
    This function uses the sqrt decomp and gives us the count of elems
    in the range [l, r] that are <= x

    It takes O(root(n) + root(n) * logn(n) + root(n)) -> O(root(n)log(n)) time
    """
    B, blocks, blocks_pref_sum, block_max, block_min = sqrt_decomp(A)
    ans = 0

    # Left partial Block
    while l <= r and l % B != 0: # checking if l is not at a block start
        if A[l] <= x:
            ans += 1
        l += 1
    
    # Full Block counts
    while l + B - 1 <= r: # Basically if the full block lenght lies inside the range L:R, l + B is the start of new block
        b = l // B # Block no.
        ans += bisect.bisect_right(blocks[b], x) # gives the idx to the right of rightmost value of <= x which is the count
        l += B

    # Right partial block
    while l <= r:
        if A[l] <= x:
            ans += 1
        l += 1

    return ans

def count_median(l, r, A):
    B, blocks, blocks_pref_sum, block_max, block_min = sqrt_decomp(A)
    
    Ac, vals = coord_compression(A)
    M = len(vals)
    length = r - l + 1
    rank = (length + 1) // 2

    lo, hi = 1, M

    while lo < hi:
        mid = (lo + hi) // 2
        mid_val = vals[mid - 1]

        if count_le(l, r, mid_val) >= rank:
            hi = mid
        else:
            lo = mid + 1
    return vals[lo - 1] # actual value



