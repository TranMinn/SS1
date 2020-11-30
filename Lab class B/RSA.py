
import math
# Calculate mod
# Calculate modular
def mod(a, b):
    if a < 0:
        while a < 0:
            a += b
        return a % b
    else:
        return a % b

# Extended Euclidean Algorithm: Ax = B mod N
def extendedEuclidean(a, b, n):
    a1 = a
    n1 = n

    if a > n:
        a = a % n

    # GCD and List of q
    q = []
    while a != 0:
        q.append(n // a)
        tempt = a
        a = n % a
        n = tempt

    gcd = n

    print('gcd = '+ str(gcd))

    # Extended Euclidean Algorithm

    # The length of q_lst and p_lst is the same
    p = [0] * (len(q) + 1)
    p_len = len(q)

    p[0] = 0
    p[1] = 1

    print('Step 0: p0 = 0')
    print('Step 1: p1 = 1')

    for i in range(2, p_len + 1):
        p_tempt = p[i - 2] - p[i - 1] * q[i - 2]
        p[i] = mod(p_tempt, n1)

        print('Step ' + str(i) + ': p' + str(i) + ' = ' + str(p[i - 2]) + ' - ' + str(p[i - 1]) + '.(' + str(q[i - 2])
              + ') mod ' + str(n1) + ' = ' + str(p[i]))

    # Calculate x
    r = p[len(p) - 1]
    x0 = (r * b) // gcd

    print('x0 = (r * b)/d mod (n/d) = (' + str(r) + ' * ' + str(b) + ')/' + str(gcd) + ' mod (' + str(n1) + '/'
          + str(gcd) + ')')

    x = mod(x0, n1 // gcd)
    print('x = ' +  str(x))

    return  x

# Modular Exponentiation : A ^ B mod N
def modularExp(a, b, n):
    list_bin = []
    while b > 0:
        list_bin.append(b % 2)
        b = b // 2

    lst2 = []
    for i in range(len(list_bin)):
        if list_bin[i] == 1:
            lst2.append(math.pow(2, i))

    s = 1
    lst3 = []
    for j in lst2:
        m = pow(a, int(j), n)
        s *= m
    result = mod(s, n)

    return result

def main():
    p = 7
    q = 11
    e = 17
    n = p * q
    z = (p -1) * (q - 1)

# Public key K+ = (n, e)
# Private key K- = (n, d)
# Find d: Solve e * d = 1 mod z
# Use extended euclidean algorithm
    d = extendedEuclidean(e, 1, z)
    print('d = '+ str(d))

# Find m by modular Exponentiation

    c1 = 37
    c2 = 39
    c3 = 29

    m1 = modularExp(c1, d, n)
    m2 = modularExp(c2, d, n)
    m3 = modularExp(c3, d, n)

    print('m1 = ' + str(c1) + '^' + str(d) + ' mod ' + str(n) + ' = '+ str(m1))
    print('m2 = ' + str(c2) + '^' + str(d) + ' mod ' + str(n) + ' = ' + str(m2))
    print('m3 = ' + str(c3) + '^' + str(d) + ' mod ' + str(n) + ' = ' + str(m3))
    print("******************************")
    print('Message: ' + chr(m1) + chr(m2) + chr(m3))

#Verify signature
    s1 = modularExp(m1, 5, n)
    m11 = modularExp(s1, c1, n)

    print(s1)
    print(m11)
# Call Main
main()