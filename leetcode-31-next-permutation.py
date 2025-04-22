'''
1, 2, 4, 3, 5, 6, 0 -> 1, 2, 4, 3, 6, 0, 5 
First find the pivot element after which things will begin to shift
Here that element is going from back clearly 5

Second reverse the array after that to signify the lowest possible values
1, 2, 4, 3, 5, 0, 6

Third find the next bigger element for 5 to swap with here -> 6
1, 2, 4, 3, 6, 0, 5
'''

def nextPermutation(nums):
    #the ascent - go till the peak
    idx = -1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            idx = i
            break

    if idx == -1:
        nums.reverse()
        return
    
    ## Reverse everything after that
    nums[idx + 1 : ] = reversed(nums[idx + 1 : ])

    ## Find the next bigger element than the pivot
    swap_ele = -1
    for i in range(idx + 1, len(nums)):
        if nums[idx] < nums[i]:
            swap_ele = i
            break

    nums[idx], nums[swap_ele] = nums[swap_ele], nums[idx]
    return
        
            
    