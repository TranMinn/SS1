# Alphabetic telephone number translator

def al_tele(telephone):
    # split telephone number into 3 part
    telephone = telephone.split('-')

    #tel_num for storing numeric phone number
    tel_num = ''

    #match characters with equivalent number
    for var in telephone:
        for char in var:
            if char.isdigit():
                tel_num += char
            elif char in 'ABC':
                tel_num += '2'
            elif char in 'DEF':
                tel_num += '3'
            elif char in 'GHI':
                tel_num += '4'
            elif char in 'JKL':
                tel_num += '5'
            elif char in 'MNO':
                tel_num += '6'
            elif char in 'PQRS':
                tel_num += '7'
            elif char in 'TUV':
                tel_num += '8'
            elif char in 'WXYZ':
                tel_num += '9'

    print("Telephone number: " + tel_num)


if __name__ == '__main__':
    telephone = input("Enter your Alphabetic telephone(XXX-XXX-XXXX): ")
    print(al_tele(telephone))
