def convert_to_binary(num):
    ans = ""
    if not num: return 0
    while num > 0:
        ans += str(num%2)
        num = num // 2
    return ans[::-1]

if __name__ == "__main__":
    print(convert_to_binary(13))
