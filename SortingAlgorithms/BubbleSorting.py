def ListSize():
   ok = False
   while not ok or n<5 or n>20:
      n = int(input("Enter the size of the list :"))
      ok = True
   return n

def Fill(n):
    T = []
    for i in range(n):
        m = int(input("Enter number "+str(i)+":"))
        while m<0:
            m = int(input("Try again with a positive number :"))
        T.append(m)       
    return T       

def Sort(T,n):
    #reduce the size of the array by 1
    for parc in range(n-1,0,-1):
        for i in range(parc):
            if T[i+1] < T[i]:
                T[i+1],T[i] = T[i],T[i+1]
    return T

n = ListSize()
T = Fill(n)
print(T)
l = Sort(T,n)
print(l)



