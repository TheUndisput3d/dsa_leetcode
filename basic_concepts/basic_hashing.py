nums = [ 1, 2, 3, 4, 4, 5, 4]

# return the repeating num with its count
# a dict that stores each elem and its count

name = "aba"

def is_palindrome(name):
    f = 0
    l = len(name) -1 # 3

    while f <= l:
        if name[f] != name[l]:
            return False
        f += 1
        l -= 1
    return True




# "appa" - name
#   f l
if __name__ == "__main__":
    print(is_palindrome("appa"))    