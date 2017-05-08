import random



k = [random.randint(0,100) for r in range(100)]

fst_max = 0
snd_max = 0
count=0
print(k)

for i in range(len(k)):
    if(k[i]>fst_max):
        snd_max = fst_max
        fst_max =k[i]
        print(k[i],fst_max,snd_max)
    elif(k[i]>snd_max):
        count+=1
        snd_max=k[i]

print("final:",fst_max,snd_max, count)
