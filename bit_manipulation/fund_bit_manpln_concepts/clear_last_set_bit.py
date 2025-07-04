from to_binary import convert_to_binary

def reset_last_set_bit(num):
    """
    resets the last set bit of num
    """
    print(f"before_conv: {convert_to_binary(num)}")
    ans = num & (num - 1)
    print(f"after_conv: {convert_to_binary(ans)}")
    return ans

if __name__ == "__main__":
    reset_last_set_bit(4)
