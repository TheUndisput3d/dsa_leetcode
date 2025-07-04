def is_pow_of_2(num):
    """
    returns True if num is a power of 2
    """
    print(num & (num - 1) == 0)
    return num & (num - 1) == 0

if __name__ == "__main__":
    for i in range(2, 101):
        print(f"{i}-{is_pow_of_2(i)}")