thelist=[]
print('enter yr number: ')
for i in range(5):
    n=int(input())
    thelist.append(n)
print(thelist)
largest=0
for i in range(len(thelist)-1):
    for j in range(1,len(thelist)):
        if thelist[i]>thelist[j]:
            if largest<thelist[i]:
              largest=thelist[i]
        else:
            if largest<thelist[j]:
              largest=thelist[j]
print(largest)
    