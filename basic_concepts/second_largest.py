nums = [-2, 3, 5, 9, 8]

# max -> 
max_ = float('-inf')
sec_max = 0

for num in nums:
    if num > max_:
        sec_max = max_
        max_ = num

