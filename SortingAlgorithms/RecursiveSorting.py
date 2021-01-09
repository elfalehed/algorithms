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
    for i in range(len(T)):
        for j in range(i+1,len(T)):
            if T[j] < T[i]:
                num1 = T[i]
                num2 = T[j]
                T[i] = num2
                T[j] = num1
    return T

n = ListSize()
T = Fill(n)
print(T)
l = Sort(T,n)
print(l)



