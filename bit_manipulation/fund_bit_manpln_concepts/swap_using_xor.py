def swap_xor(n1, n2):
    print(f"before_swapping: {n1, n2}")
    n1 = n1 ^ n2
    n2 = n1 ^ n2
    n1 = n1 ^ n2
    print(f"after_swapping: {n1, n2}")

if __name__ == "__main__":
    swap_xor(2, 3)