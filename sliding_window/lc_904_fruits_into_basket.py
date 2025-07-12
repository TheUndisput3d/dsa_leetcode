from typing import List

## Brute Force Solution
# T.C: O(n^2)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 1

        for i in range(len(fruits)):
            type_set = set()
            for j in range(i, len(fruits)):
                type_set.add(fruits[j])
                if len(type_set) > 2:
                    break
                max_fruits = max(max_fruits, j-i+1)
        return max_fruits
                
                

## Better Solution
# T.C: O(2n)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Time Complexity: 2n => O(n)
            - The right pointer (j) moves across the list once: n steps
            - The left pointer (i) also moves across the list at most once: n steps
            - Total = 2n operations

        Space Complexity: O(1)
            - A hashmap is used to store at most 2 fruit types at any time

        """

        n = len(fruits)

        # Initialize the window pointers
        i, j = 0, 0

        # Hash map to store fruit type counts in current window
        map_ = {}

        # Variable to store the maximum number of fruits collected
        maxFruits = 0

        # Iterate using the right pointer
        while j < n:
            curr = fruits[j]
            map_[curr] = map_.get(curr, 0) + 1

            # Shrink the window from the left if more than 2 types of fruits
            while len(map_) > 2:
                map_[fruits[i]] -= 1
                if map_[fruits[i]] == 0:
                    del map_[fruits[i]]
                i += 1  # Move the left pointer

            # Update the maximum length of valid window
            currLen = j - i + 1
            maxFruits = max(maxFruits, currLen)

            # Move the right pointer
            j += 1

    
## Best Solution (Most Optimal)
## T.C: O(n)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Time Complexity: 2n => O(n)
            - The right pointer (j) moves across the list once: n steps
            - The left pointer (i) also moves across the list at most once: n steps
            - Total = 2n operations

        Space Complexity: O(1)
            - A hashmap is used to store at most 2 fruit types at any time
        """

        n = len(fruits)

        # Initialize pointers for the sliding window
        i, j = 0, 0

        # Hashmap to track counts of fruit types in current window
        map_ = {}

        # Track the maximum number of fruits collected
        maxFruits = 0

        # Traverse the fruit array using the right pointer `j`
        while j < n:
            curr = fruits[j]
            map_[curr] = map_.get(curr, 0) + 1

            # If more than 2 fruit types in the window, shrink from the left
            if len(map_) > 2:
                map_[fruits[i]] -= 1
                if map_[fruits[i]] == 0:
                    del map_[fruits[i]]
                i += 1  # Shrink window

            # Update maxFruits if current window is valid (≤ 2 types)
            if len(map_) <= 2:
                currLen = j - i + 1
                maxFruits = max(maxFruits, currLen)

            j += 1  # Expand window

        return maxFruits

            





