
def main():
        #open files
        file_ques = open("questions.txt")
        file_ans = open("answers.txt")
        file_key = open("key.txt")

        #read each line of files, form lists
        ques_lst = file_ques.readlines()
        ans_lst = file_ans.readlines()
        key_lst = file_key.readlines()

        #Create a list of keys (extract /n)
        ans = []
        for i in key_lst:
            i = i[:-1]
            ans.append(i)

        right_ans = 0
        wrong_ans = 0

        print('Enter answers: ')
        answer_input = []
        for i in range(2):
            print(ques_lst[i])
            print(ans_lst[i])
            print('Answer ', (i+1),': ')
            answer = input()
            answer= answer.upper()
            answer_input.append(answer)

            #Compare selected ans with true keys
            if ans[i] == answer_input[i]:
                right_ans += 1
            else:
                wrong_ans += 1


        print('Right answers: ', right_ans)
        print('Wrong answers: ', wrong_ans)

main()