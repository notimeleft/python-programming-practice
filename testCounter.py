import collections
a = "abcd"
b = "abcde"

x = collections.Counter(a)
y = collections.Counter(b)
print y-x

a_dict = {}
b_dict = {}
for i in range(0,len(a)):
    if(a[i] in a_dict):
        a_dict[a[i]]+=1
    else:
        a_dict[a[i]]=1
for i in range(0,len(b)):
    if(b[i] in b_dict):
        b_dict[b[i]]+=1
    else:
        b_dict[b[i]]=1

print b_dict.difference(a_dict)
