def get_max_min(arr):
  max_ = float('-inf')
  min_ = float('inf')

  for num in arr:
    if num > max_:
      max_ = num
    if num < min_:
      min_ = num
    
  print(f"min: {min_}")
  print(f"max: {max_}")