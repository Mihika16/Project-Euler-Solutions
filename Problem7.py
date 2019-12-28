def functionmihika(num):
    if num < 2: return "cool"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#____________________
def actual(n):
    second = 0
    prime = 1

    while second < n:
        prime = prime+ 1
        if functionmihika(prime):
            second = second+ 1
    return prime

print(actual(10001))
