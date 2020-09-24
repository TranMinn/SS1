
#Vowels and Consonants

def v_c(argu):

    vowels = ['u', 'e', 'o', 'a', 'i']
    vowel = 0
    cons = 0
    for i in argu:
        if i in vowels:
            vowel += 1
        else:
            cons += 1

    print("Number of vowels: "+ str(vowel))
    print("Number of consonants: " + str(cons))

if __name__ == '__main__':
    argu = input("Enter a string: ")
    print(v_c(argu))