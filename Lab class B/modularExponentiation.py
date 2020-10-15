
import math

# Calculate modular
def mod(a, b):
    if a < 0:
        while a < 0:
            a += b
        return a % b
    else:
        return a % b

# Main
def main():
    print('Find X in equation by Euclidean Algorithm: A^B mod N')
    a = int(input('Enter A: '))
    b = int(input('Enter B: '))
    n = int(input('Enter N: '))

# Convert decimal to binary
    list_bin = []
    while b > 0:
        list_bin.append(b % 2)
        b = b // 2
    print(list_bin)

# Elements creating b
    lst2 = []
    for i in range(len(list_bin)):
        if list_bin[i] == 1:
            lst2.append(math.pow(2, i))
    print(lst2)

# Final result
    s = 1
    lst3 = []
    for j in lst2:
         m = pow(a,int(j),n)
         s *= m
    result = mod(s, n)
    print(result)

# Call Main
main()