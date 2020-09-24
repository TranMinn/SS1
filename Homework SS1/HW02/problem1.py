
# Print a person name first, middle and last initials
def print_initial(full_name):
    # Get a string of full_name & split words into a string
    full_name = full_name.split()

    # print the initials of each element in list
    for i in full_name:
        print (i[0] + ".", end = '')


if __name__ == '__main__':
    print("Enter you full name: ")
    full_name = input()
    print(print_initial(full_name))
