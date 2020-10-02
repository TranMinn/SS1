
def main():
        question_list = ['1. Which is the most prioritized vehicle?', '2. What do you do when traffic light turn red?']

        answer_list = ['A: ambulance B: bicycle C:motocycle D: police car ', 'A: nothing B: keep going C: stop']

        answer_dict = {
            1: 'A', 2: 'C'
        }

        right_ans = 0
        wrong_ans = 0

        print('Enter answers: ')
        answer_input = []
        for i in range(2):
            print(question_list[i])
            print(answer_list[i])
            print('Answer ', (i+1),': ')
            answer = input()
            answer= answer.upper()
            answer_input.append(answer)

            if answer_dict[i+1] == answer_input[i]:
                right_ans += 1
            else:
                wrong_ans += 1


        print('Right answers: ', right_ans)
        print('Wrong answers: ', wrong_ans)

main()