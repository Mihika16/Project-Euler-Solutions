first = 0
for i in range(100,1000):
   for j in range(i, 1000):
      second = i * j
      if str(second) == str(second)[::-1] and second>first:
          first = second

print(first)

