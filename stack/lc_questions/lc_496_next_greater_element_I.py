from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ## O(n*m) Approach (Brute Force Approach)

        # nums1Idx = {val: i for i, val in enumerate(nums1)}
        # ans = [-1] * len(nums1)

        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1:
        #         continue
        #     for j in range(i+1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             idx = nums1Idx[nums2[i]]
        #             ans[idx] = nums2[j]
        #             break
        # return ans
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
        ## O(n+m) Optimal-Approach

        nums1Idx = {val:i for i, val in enumerate(nums1)}
        ans = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                elem = stack.pop()
                idx = nums1Idx[elem]
                ans[idx] = curr
            if curr in nums1Idx:
                stack.append(curr)

        return ans
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
       ## Another version of Optimal Solution
       
        # nums1Idx = {val:i for i, val in enumerate(nums1)}
        # stack = []

        # for i in range(len(nums2)):
        #     curr = nums2[i]
        #     while stack and curr > stack[-1]:
        #         elem = stack.pop()
        #         idx = nums1Idx[elem]
        #         nums1[idx] = curr
        #     if curr in nums1Idx:
        #         stack.append(curr)
        
        # while stack:
        #     val = stack.pop()
        #     idx = nums1Idx[val]
        #     nums1[idx] = -1
        # return nums1




        


