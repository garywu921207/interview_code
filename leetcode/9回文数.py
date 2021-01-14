
def isPalindrome(x):
    tmp = []

    for index, item in enumerate(str(x)):
        if index == 0 and item == '-':
            return False
        tmp.append(item)

    if tmp == tmp[::-1]:
        return True
    else:
        return False


print(isPalindrome(-123))
