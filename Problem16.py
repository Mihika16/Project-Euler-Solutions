first = 2**1000
print(first)


sum= 0
while first:
    sum += first % 10
    first //= 10

print(sum)
