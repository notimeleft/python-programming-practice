#Write a function that takes a string as input and returns the string reversed.
def reverseString(s):
    string = list(s)
    last = len(string)-1
    for i in range(0,len(string)/2):
        temp_first = string[i]
        temp_last = string[last]
        print "1.", temp_first, temp_last
        string[i] = temp_last
        string[last] = temp_first
        print "2.", string[i], string[last]
        last = last-1
    print string


reverseString("abelincolnk")
