
#Bouble sort

def main():
    #Initiate array
    array = list()
    array_len = int(input('Enter the length of array: '))

    #Enter elements of array
    print('Enter array elements:')
    for i in range(array_len):
        print('Element '+ str((i+1)) + ': ')
        e = int(input())
        array.append(e)


    #Bubble sort array
    for i in range(array_len):
        for j in range(array_len - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print(array)
#Call the main function
main()