def count_sub_sum_k(nums, k):
    """
    returns the count of all the subsequences with sum 
    """
    n = len(nums)
    def solve(ind, total):
        if total == k:
            return 1
        elif total > k:
            return 0
        if ind >= n:
            return 0
        pick = solve(ind+1, total+nums[ind])
        not_pick = solve(ind+1, total)
        return pick + not_pick
    return solve(0, 0)

if __name__ == "__main__":
    nums = [2, 3, 2, 3, 4, 2]
    k = 6
    print(count_sub_sum_k(nums, k))