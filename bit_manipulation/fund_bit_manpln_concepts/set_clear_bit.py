from to_binary import convert_to_binary

# set a respective bit in a number
def set_bit_left_shift(num, i):
    """ 
    set the ith bit  bit in num
    """
    print(f"question_ls: {convert_to_binary(num)}")
    ans = num | 1<<i
    print(f"ans_ls: {convert_to_binary(ans)}")

def reset_bit(num, i):
    """ 
    reset the ith bit  bit in num
    """
    print(f"question_reset: {convert_to_binary(num)}")
    ans = num & ~(1<<i)
    print(f"ans_reset: {convert_to_binary(ans)}")

if __name__ == "__main__":
    set_bit_left_shift(8, 1)
    reset_bit(15, 3)


