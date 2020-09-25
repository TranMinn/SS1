# Read number
def read(num):
    num_dict = {
        0: 'khong',
        1: 'mot',
        2: 'hai',
        3: 'ba',
        4: 'bon',
        5: 'nam',
        6: 'sau',
        7: 'bay',
        8: 'tam',
        9: 'chin'
    }

    #Read 1-digit number
    if len(str(num)) == 1:
        one = int(num)
        print(num_dict[one])
        
    #Read 2-digit number
    elif len(str(num)) == 2:
        ten = int(num) // 10
        one = int(num) % 10
        if ten == 0:
            print(num_dict[one], 'muoi')
        else:
            print(num_dict[one], 'muoi', num_dict[ten])
            
    #Read 3-digit number
    elif len(str(num)) == 3:
        hundred = int(num) // 100
        ten = (int(num) % 100) // 10
        one = int(num) % 10
        if ten == 0:
            print(num_dict[hundred], 'tram', 'linh', num_dict[one])
        elif one == 0:
            print(num_dict[hundred], 'tram', num_dict[ten], 'muoi')
        else:
            print(num_dict[hundred], 'tram', num_dict[ten], 'muoi', num_dict[one])


if __name__ == '__main__':
    money = input('Enter the money: ')
    
    #Divide money number into parts and use def read() for each
    #Each part has maximum 3 digits
    if len(str(money)) <= 3:
        part1 = int(money)
        print(read(part1))

    elif len(str(money)) <= 6:
        part1 = int(money) // 1000
        part2 = int(money) % 1000
        print(read(part1), 'nghin', read(part2), 'dong chan')

    elif len(str(money)) <= 9:
        part1 = int(money) // 1000000
        part2 = (int(money) % 1000000) // 1000
        part3 = int(money) % 1000
        print(read(part1), 'trieu', read(part2), 'nghin', read(part3), 'dong chan')

    elif len(str(money)) <= 12:
        part1 = int(money) // 1000000000
        part2 = (int(money) % 1000000000) // 1000000
        part3 = (int(money) % 1000000) // 1000
        part4 = int(money) % 1000
        print(read(part1), 'ti', read(part2), 'trieu', read(part3), 'nghin', read(part4),
              'dong chan')
