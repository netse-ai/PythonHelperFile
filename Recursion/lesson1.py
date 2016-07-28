def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print list_sum([1, 3, 5, 7, 9])

def fact(num):
    if num <= 1:
        return num
    else:
        return num * fact(num - 1)

print fact(5)

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

print toStr(769, 16)

def reverseString(string):
    if len(string) <= 1:
        return string
    else:
        return reverseString(string[1:]) + string[0]

print reverseString("This is a string")


def recursivePalindrome(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    else:
        return recursivePalindrome(string[1:-1])
print recursivePalindrome("Able was I ere I saw elbA")
