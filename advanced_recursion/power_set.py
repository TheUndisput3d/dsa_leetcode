# Generate all the  the possible subsets/subsequences


# T.C -> O(2^n)
# S.C -> O(n) (memory taken by system_stack)
def generate_power_set(nums):
    """
    returns list containing all the possible subsequences/ subsets of nums.
    each subsequence is a list.
    """
    n = len(nums)
    result = []

    def solve(ind, subset):
        if ind >= n:
            result.append(subset.copy())
            return
        
        subset.append(nums[ind])
        solve(ind+1, subset)
        subset.pop()
        solve(ind+1, subset)
    
    solve(0, [])

    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    power_set = generate_power_set(nums)
    print(power_set)



