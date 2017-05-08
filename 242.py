def isAnagram(s, t):
    string_s = list(s)
    string_t = list(t)

    string_s.sort()
    string_t.sort()
    if string_s == string_t:
        return True
    return False


print isAnagram("able","ablle")
