def convert_to_decimal(bin_num):
    decimal_ans = 0

    index = len(bin_num) - 1
    power = 0
    while index >= 0:
        decimal_ans += int(bin_num[index]) * 2**(power)
        power += 1
        index -= 1
    print(decimal_ans)
    return decimal_ans

if __name__ == "__main__":
    convert_to_decimal("1010")