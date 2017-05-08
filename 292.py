def canWinNim(n):
    a = n%1==4
    b = n%2==4
    c = n%3==4

    if (not a and not b and not c):
        return False
    return True

print canWinNim(4)
