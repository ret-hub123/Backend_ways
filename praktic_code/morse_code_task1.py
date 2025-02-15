from preloaded import MORSE_CODE

def decode_morse(morse_code):
    s = morse_code
    res = []
    s = s.strip()
    word = s.split('   ')
    letters = [letter.split(" ") for letter in word]
    for i in range(len(letters)):

        for j in range(len(letters[i])):
            res.append(MORSE_CODE[letters[i][j]])
        res.append(' ')

    res = ''.join(res[:-1])
    
    return (res)

"""довольно интересное задание, но сильная проблема возникла с библиотекой, 
но в моём решении я разбил слова и буквы на под элементы в массиве, 
в итоге получился кортеж, который я прогнал по MORSE_CODE и склеил с помощью join
"""