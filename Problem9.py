for i in range(400):
    for j in range(400):
        k = 1000-i-j
        if i<j<k:
            if i**2 + j**2 == k**2:
                answer=i*j*k
                print(answer)

        else:
            break

           
                
                
