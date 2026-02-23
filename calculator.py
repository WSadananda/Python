#value taking from user
def take_value():
    a=float(input(" ".join(map(int_convertor,store))+" "))
    store.append(a)
    print("+ - * / =")
    b=(input(" ".join(map(int_convertor,store))+" "))
    if b in ['+', '-', '*','/']:
        store.append(b)
        take_value()
    if b == '=':
        solution()
#-----------------------------------------------------------
#value cdonvertor float -->int 
def int_convertor(x):
    if isinstance(x,(int,float)):
        if x == int(x):
            return str(int(x))
        else:
            return str(x)
    else:
        return str(x)

#--------------------------------------------------------------------
#calculate the solution
def solution():
    global store,i
    while i < len(store):
        if store[i] == '/':
            store[i-1]=store[i-1]/store[i+1]
            store.remove(store[i])
            store.remove(store[i])
        else:
         i+=1
    i=0
    while i < len(store):
        if store[i] == '*':
            store[i-1]=store[i-1]*store[i+1]
            store.remove(store[i])
            store.remove(store[i])
        else:
         i+=1
    i=0
    while i < len(store):
        if store[i] == '+':
            store[i-1]=store[i-1]+store[i+1]
            store.remove(store[i])
            store.remove(store[i])
        else:
         i+=1
    i=0
    while i < len(store):
        if store[i] == '-':
            store[i-1]=store[i-1]-store[i+1]
            store.remove(store[i])
            store.remove(store[i])
        else:
         i+=1
    print(" ".join(map(int_convertor,store))+" ")


#function calling 
print("CALCULATOR\n + - * /")
store=[]
i=0
take_value()
