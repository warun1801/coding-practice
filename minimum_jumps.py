'''
Bob lives with his wife in a city named Berland. Bob is a good husband, so he goes out with his wife every Friday to ‘Arcade’ mall.

‘Arcade’ is a very famous mall in Berland. It has a very unique transportation method between shops. Since the shops in the mall are laying in a straight line, you can jump on a very advanced trampoline from the shop i, and land in any shop between (i) to (i + Arr[i]), where Arr[i] is a constant given for each shop.

There are N shops in the mall, numbered from 0 to N-1. Bob's wife starts her shopping journey from shop 0 and ends it in shop N-1. As the mall is very crowded on Fridays, unfortunately, Bob gets lost from his wife. So he wants to know, what is the minimum number of trampoline jumps from shop 0 he has to make in order to reach shop N-1 and see his wife again. If it is impossible to reach the last shop, return -1.
'''


def minimumJumps(arr, n):
    if n == 1:
        return 0

    curr = 0
    steps = 0
    max_curr = curr
    
    for i in range(n-1):
        ## Count whats the max till we reach where we are currently
        max_curr = max(max_curr, arr[i] + i)
        # if we reach max possible already, and not at the end quit
        if max_curr == i:
            return -1

        ## Taking the actual step and getting to the max possible place
        if i == curr:
            curr = max_curr
            steps += 1

    return steps


