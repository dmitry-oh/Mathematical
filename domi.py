#Machine Calculating binomial theorem

# DO NOT forget to describe coefficient of each character ex) 1x+1y
# only 1 digit coefficient accepted

def f(r):
    result = 1
    for item in range(1, r+1, 1):
        result *= item     
    return result

def Slice(st,ag1,ag2):
    k = st.split("+")
    n = f(ag1)/(f(ag1-ag2)*f(ag2))
    k1 = k[0]
    k2 = k[1]

    ao = (int(k1[0])**ag2)*(int(k2[0])**(ag1-ag2))*n

    toprint = str(ao)+k1[-1]+"^"+str(ag2)+k2[-1]+"^"+str(ag1-ag2)
    return toprint

a = input("Syn ? : ")
b = int(input("Power ? : "))

m = 0
A = []
while m<=b:
    A.append(Slice(a,b,m))
    m = m+1

print(A)