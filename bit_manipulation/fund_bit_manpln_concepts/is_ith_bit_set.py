def is_bit_set(num, i):
    """
    returns True if the i-th bit of num is set
    """
    return num & (1 << i) != 0


if __name__ == "__main__":
    print(is_bit_set(8, 3))