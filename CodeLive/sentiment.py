# Sentiment

def main():
    file = open("test.txt")
    list_data = file.readlines()
    print(list_data)
    print(len(list_data))
    cont = True
    while(cont):
        print("What would you like to do? \n"
              "1: Get the score of the word \n"
              "2: Get the average score of words in a file \n"
              "3: Find the highest/ lowest scoring words in a file \n"
              "4: Sort the words in a file into positive.txt and negative.txt \n"
              "5: Exit the program"
              )
        choice = int(input("Enter number 1 - 5: "))

        if choice < 1 and choice > 5:
            print("Enter option from 1 - 5 only!")
            continue
        else:
            if choice == 1:
                print(get_score(list_data))
            elif choice == 2:
                print(get_average(list_data))
            elif choice == 3:
                print(highest_lowest(list_data))
            elif choice == 4:
                print(sort_word(list_data))
            else:
                cont = False
                print("Goodbye")



# def readFile(filename):
#     file = open(filename, "r")
#     list_data = file.readlines()
#     print(list_data)

def get_score(list_data):

    list_number = []
    list_sen = []
    list_w = []
    word = input("Which words? ")
    for i in range(len(list_data)):
        num = list_data[i][0]
        sen = list_data[i][2:].strip()
        list_sen.append(sen)
        list_number.append(num)

    for i in range(len(list_data)):
        list_word = list_sen[i].split(' ')
        list_w.append(list_word)

    count = 0
    for i in range(len(list_data)):
        for w in list_word[i]:
            if word == w:
                count += 1

    print(count)


    # for i in range(len(list_word)):
    #     count = 0
    #     for word in list_word[i]:
    #         for j in range(len(list_word[i])):
    #             if word[j] == word[i][j]:
    #                 count += 1
    #     list_count.append(count)

    # print(list_sen)
    # print(list_number)

def get_average(word_dict):
    score_list = []
    average_score = []
    assessment = []
    num_word = len(word_dict)
    for i in range(num_word):
        score = word_dict[i].keys()
        score_list.append(score)

    for i in range(len(score_list)):
        ave = score_list[i] / num_word
        average_score.append(ave)

    for i in range(len(average_score)):
        if average_score[i] > 2.01:
            assessment.append("Positive")
        elif average_score[i] < 1.99:
            assessment.append("Negative")
        else:
            assessment.append("Neutral")

    return average_score

def highest_lowest():
    return ""

def sort_word(my_dict):
    return ""


main()