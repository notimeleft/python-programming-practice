from collections import deque

def reverseVowels(s):
    stack = []
    position = deque([])
    string = list(s)
    vowels = ["a","e","i","o","u", "A","E","I","O","U"]
    for i in range(0,len(string)):
         if string[i] in vowels:
             stack.append(string[i])
             position.append(i)

    for k in range(0,len(stack)):
        pos = position.popleft()
        string[pos] = stack.pop()

    return "".join(string)
print reverseVowels("aA")
