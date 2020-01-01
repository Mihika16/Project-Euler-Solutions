sum=1
for i in range(1,101):
    sum=sum*i




ansum= 0
while sum:
    ansum += sum % 10
    sum //= 10

print(ansum)
