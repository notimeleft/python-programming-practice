"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.
"""
def isIsomorphic(s, t):
        string_s = list(s)
        string_t = list(t)
        encountered_s = {}
        encountered_t = {}
        new_string_s = []
        new_string_t = []
        value_s = 0
        value_t = 0
        for i in range(0, len(string_s)):
            k = string_s[i]
            p = string_t[i]
            if k not in encountered_s:
                encountered_s[k]=value_s
                value_s=value_s+1
            new_string_s.append(encountered_s[k])
            if p not in encountered_t:
                encountered_t[p]=value_t
                value_t=value_t+1
            new_string_t.append(encountered_t[p])

        if new_string_s == new_string_t:
            return True
        return False

isIsomorphic("apple","diary")
