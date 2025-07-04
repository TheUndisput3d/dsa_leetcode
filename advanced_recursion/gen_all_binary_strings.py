# Generate all the binary strings

def generate_bin_strings(n):
    ans = ["0"] * n
    res = []
    def solve(ind, flag, ans):
        if ind >= n:
            res.append("".join(ans))
            return 
        solve(ind+1, True, ans)
        if flag:
            ans[ind] = "1"
            solve(ind+1, False, ans)
            ans[ind] = '0'

    
    solve(0, True, ans)
    print(res)

generate_bin_strings(5)
        