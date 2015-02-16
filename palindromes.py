first = 999
second = 999
palindromes = []

def is_palindrome(x):
    y = []
    x = str(x)
    x = list(x)
    for n in x:
        y.append(n)
    y.reverse()
    x = "".join(x)
    y = "".join(y)
    if x == y:
        return True
    else:
        return False


while first > 99:
    while second > 99:
        if is_palindrome(first * second) == True:
            palindromes.append(first*second)
        second -= 1
    first -= 1
    second = 999
print max(palindromes)
