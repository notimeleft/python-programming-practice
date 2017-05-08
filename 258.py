#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
def addDigits(num):
    string_n = str(num)
    if(len(string_n)==1):
        return int(num)
    else:
        next_num = 0
        for i in range(0,len(string_n)):
            next_num+=int(string_n[i])
        return addDigits(next_num)

print addDigits(1437)
