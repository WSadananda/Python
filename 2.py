#squring
thelist = []
sqrlist=[]
print("enter your number\n")
for i in range(5):
    number=int(input())
    thelist.append(number)
#print squre of the value
print("squre the value")
for i in thelist:
    sqrt=i*i
    sqrlist.append(sqrt)
print(sqrlist)
print(i)