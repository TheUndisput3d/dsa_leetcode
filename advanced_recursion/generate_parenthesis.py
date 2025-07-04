from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def solve(ind: int, total: int, ans: List) -> List[str]:
            if total < 0:
                return 
            
            elif total > n:
                return 

            if ind >= 2*n:
                if not total:
                    res.append("".join(ans))
                return 
            ans.append("(")
            solve(ind+1, total+1,ans)
            ans.pop()
            ans.append(")")
            solve(ind+1, total-1, ans)
            ans.pop()

        solve(0, 0, [])
        print(res)
        return res
    
if __name__ == "__main__":
    sln = Solution()
    n = 3
    ans = sln.generateParenthesis(n)
            

        ### ((()))
        # yeuta solve function banaunu paro
        # teslai kk chainxa hola ta?:
            # n ta mathiko func batai refer garna sakxa so arg ma pathauna jaruri xaina
            # yeuta string(tara str ma append garna mildaina tei vara list pass garera antim ma join garnu paro)
            # jun ma curr ans store garinxa tyota last ma gara list ma append garnu parxa
            # yeuta ans list chaiyo tesma hareko choti valid subst aauda ans append garnu paro
            # yeuta ta base case handle garna ra chinna laai pani ta chaaiyo ni variable (index type ko)
            # tsko value chi >= 2*n huda base case vo
            # backtracking type ko chalaunu parxa jasto lagyo
            # harek choti u can either pick '(' or ')'  