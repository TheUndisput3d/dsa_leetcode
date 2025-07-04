# Extract the value of the ith bit

def extract_val(num, i):
    """
    returns the value of the i-th bit in num
    """
    return 1 if num & (1 << i) != 0 else 0

if __name__ == "__main__":
    for i in range(4):
        print(extract_val(10, i))