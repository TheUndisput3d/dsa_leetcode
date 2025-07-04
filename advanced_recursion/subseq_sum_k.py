# Generate all the subsequences with sum K

# Brute Force Approach to generate the subsequences with Sum K
def subseq_sum_k_brute(nums, k):
    """
    Brute-Force Approach to generate the subsequences with Sum K.
    Returns list containing the subsequences whose Sum is equal to K.
    """
    n = len(nums)
    result = []

    def solve(ind, subset):
        if ind >= n:
            if sum(subset) == k:
                result.append(subset.copy())
            return
        
        subset.append(nums[ind])
        solve(ind+1, subset)
        subset.pop()
        solve(ind+1, subset)
    
    solve(0, [])

    return result

# Optimal Approach to generate the subsequences with Sum K
def subseq_sum_k_optimal(nums, k):
    """
    Optimal Approach to generate the subsequences with Sum K.
    Returns list containing the subsequences whose Sum is equal to K.
    """
    n = len(nums)
    result = []

    def solve(ind, total, subset):
        if total == k:
            result.append(subset.copy())
            return
        elif total > k:
            return 
        if ind >= n:
            if total == k:          
                result.append(subset.copy())
            return
        
        subset.append(nums[ind])
        solve(ind+1, total+nums[ind], subset)
        subset.pop()
        solve(ind+1, total, subset)
    
    solve(0, 0, [])

    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 5
    ans = subseq_sum_k_optimal(nums, k)
    print(ans)