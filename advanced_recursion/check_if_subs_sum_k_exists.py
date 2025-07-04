def subs_sumk_exist(nums, k):

    n = len(nums)

    result = []
    def solve(ind, total, subset):
        if total == k:
            result.append(subset.copy())
            return True
        elif total > k:
            return False
        if ind >= n:
            return False
        
        subset.append(nums[ind])
        pick = solve(ind+1, total+nums[ind], subset)
        if pick == True:
            return True
        subset.pop()
        can_pick = solve(ind+1, total, subset)
        return can_pick
    
    ans = solve(0, 0, [])
    print(result)
    return ans
    
if __name__ == "__main__":
    print(subs_sumk_exist([2, 3, 4], 7))
    
