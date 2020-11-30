
# Word separator
def main():
    yourString = input('Enter your string: ')

    outputString = yourString[0]
    for i in range(1, len(yourString)):
        ch = yourString[i]

        if ch.isupper():
            ch = ch.lower()
            outputString = outputString + ''

        outputString += ch

    print(outputString)

# Main
main()



