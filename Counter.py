#Machine- Counting all cases of totally 'b' in nonnegative integer   , too many errors

b = input("Sum? ") #result

a = int(b)

count = 1

k = 0
t = True

E = [0,0,0,0]

A = []

def create():
    global E
    E[0] = a-3
    E[1] = 1
    E[2] = 1
    E[3] = 1

def factorial(r):
    result = 1
    for item in range(1, r+1, 1):
        result *= item     
    return result

def add():
    global A
    global E
    global k
    global count
    global a
    global t
    #return when there is no E[index+1] or E[index]==0
    if k < len(E)-1:
        if E[k] == 0:
            k = k+1
        else:
            E[k] = E[k]-1
            E[k+1] = E[k+1]+1
            for i in A:
                if i == sorted(E):
                    return
            A.append(sorted(E))
            if len(E) == set(E):
                count = count+factorial(len(E))
            else:
                count = count+(factorial(len(E))/factorial(len(E)-len(set(E))))

    else: 
        t = False
        print(count)


create()
while t:
    add()
print(A)