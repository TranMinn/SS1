def main():
    # Local variables
    morse_string = ''

    morse_string = input('Enter the string to be ' \
                         'converted to Morse code: ')

    morse_string2 = ''
    morse_dict = {
        ' ': ' ',
        ',': '--..--',
        '.': '.-.-.-',
        '?': '-----',
        '0': '.----',
        '1': '..---',
        '2': '...--',
        '3': '....-',
        '4': '.....',
        '5': '-....',
        '6': '--...',
        '7': '---..',
        '8': '----.',
        '9': '.-',
        'A': '-...',
        'B': '-.-.',
        'C': '-..',
        'D': '.',
        'E': '..-.',
        'F': '--.',
        'G': '....',
        'H': '..',
        'I': '.---',
        'J': '-.-',
        'K': '.-..',
        'L': '--',
        'M': '-.',
        'N': '---',
        'O': '.--.',
        'P': '--.-',
        'Q': '.-.',
        'R': '...',
        'S': '-',
        'T': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.-',
        'Z': '--..'

    }

    for ch in morse_string:
        ch = ch.upper()
        print(morse_dict[ch], ',', sep='', end='')

main()
