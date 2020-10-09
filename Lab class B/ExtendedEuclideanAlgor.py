# Congruence Ax = B mod N
# Extended Euclidean Algorithm

# Calculate GCD(a,b)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Calculate modular
def mod(a, b):
    if a < 0:
        while a < 0:
            a += b
        return a % b
    else:
        return a % b


def main():
    print('Find X in equation by Euclidean Algorithm: Ax = B mod N')
    a = int(input('Enter A: '))
    b = int(input('Enter B: '))
    n = int(input('Enter N: '))

    a1 = a
    n1 = n

    if a > n:
        a = a % n

    # GCD and List of quotions
    q = []
    while a != 0:
        q.append(n // a)
        tempt = a
        a = n % a
        n = tempt

    gcd = n

    print('GCD(' + str(a) + ', ' + str(n) + ')' + '= ' + str(gcd))

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


main()
