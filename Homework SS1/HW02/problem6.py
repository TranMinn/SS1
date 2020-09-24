# Most frequent character

def fre_char(string_):
    counter = 0
    counter2 = 0
    most_fre_char = ''

    for i in string_:
        for j in string_:
            # Count the frequency of similar character
            if i == j:
                counter += 1

        #save value for the comparison in the next loop
        #figure out the most frequent character
        if counter > counter2:
            counter2 = counter
            most_fre_char = i

        # Continue counting with other characters
        counter = 0

    print("The most frequent character: " + most_fre_char)


if __name__ == '__main__':
    string_ = input("Enter a string: ")
    print(fre_char(string_))
