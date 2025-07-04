def toggle_bit(num, i):
    """
    toggle the ith bit of num
    """
    print(num ^ (1 << i))
    return num ^ (1 << i)

if __name__ == "__main__":
    toggle_bit(7, 1)
