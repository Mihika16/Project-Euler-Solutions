
def Primefunction(num):
    if num<2: return "False"#From the next 3 lines, I got help from a website but I understood it fully
    for i in range(2, int(num**0.5) + 1):#this
        if num % i == 0:# and this
            return False

    return True



sum=0
for i in range(2, 2000000):
    if Primefunction(i):
        sum=sum+i

print(sum)




        
    
