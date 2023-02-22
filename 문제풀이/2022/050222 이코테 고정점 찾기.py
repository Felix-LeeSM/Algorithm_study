def sect(nums=[-15, -6, 1, 3, 7]):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo+hi)//2
        if mid < nums[mid]:
            hi = mid
        elif mid > nums[mid]:
            lo = mid+1
        else:
            break
    return lo if nums[lo] == lo else -1


print(sect())
