def subset_sum(ind, total, quest):
    """
    appends each possible sum to a global ans variable
    """
    if ind == len(quest):
        ans.append(total)
        return 
    
    subset_sum(ind+1, total+quest[ind], quest) # choose
    subset_sum(ind+1, total, quest) # dont choose or dont pick

def subset_sum_2(ind, total, quest): # doesnt use global ans variable

    """
    returns the list with all the possible sum.
    doesn't append ans to a global ans variable
    """
    if ind == len(quest):
        return [total]
    
    pick = subset_sum_2(ind+1, total+quest[ind], quest) # choose
    not_pick = subset_sum_2(ind+1, total, quest) # dont choose or dont pick
    pick.extend(not_pick)
    return pick

if __name__ == "__main__":
    ans = []
    subset_sum(0, 0, [1, 2])
    print(ans)
    print(subset_sum_2(0, 0, [1, 2]))
