
#Sentence Capitalizer

def capitalize_sentence(sentence):

    #Split sentence in to words list by '. '
    words = sentence.split('. ')

    #Capitalize each word in list words
    cap_sen_str = [word.capitalize() for word in words]

    #Join sentence
    cap_sen2 = '. '.join(cap_sen_str)

    print(cap_sen2)

if __name__ == '__main__':
    sentence = input("Enter a sentence: ")
    print(capitalize_sentence(sentence))