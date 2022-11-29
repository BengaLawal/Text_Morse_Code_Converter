from morse_code_dict import MORSE_CODE_DICT


def text_to_morse_code(sentence):
    """Text to Morse Code Converter"""
    breakup_sentence = sentence.split()  # split up words into list
    breakup_words = []
    for word in breakup_sentence:
        for letter in word:
            breakup_words.append(letter)  # add each letter in sentence to empty list
    morse = [MORSE_CODE_DICT[i.upper()] for i in breakup_words]  # list of letter translated to morse

    morse_code = ''
    for word in breakup_sentence:
        morse_code += " ".join(morse[:len(word)])  # add the joined letters for each word to morse_code string
        del morse[:len(word)]  # delete splice of word from list
        morse_code += "   "  # add 3 spaces after every word
    return morse_code


def morse_code_to_text(morse_code):
    """Morse Code To Text Converter"""
    split_morse = morse_code.split('   ')  # split up the different words divided by 3 spaces
    sentence = []
    for word in split_morse:
        split_morse = word.split()  # split the morse_word into separate morse_letters
        # search for the key in a dict using the values
        letter = [list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse)] for morse in split_morse]
        joined_letter = ''.join(letter)  # join letters to form word
        sentence.append(joined_letter)  # append the words to sentence list
    return ' '.join(sentence).capitalize()  # return joined sentence


active = True
while active:
    choose = input('Do you want to Encode or Decode?\n').lower()
    if choose == 'encode':
        string = input('Enter string/s\n')
        print(text_to_morse_code(string))
    elif choose == 'decode':
        string = input('Enter morse code\n')
        print(morse_code_to_text(string))
    elif choose == 'exit':
        active = False
    else:
        print('wrong option')
