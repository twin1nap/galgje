hangman_word = input("welk woord moet er geraden worden?\n")
print("\n"*1037)

word_legnth = 0
for characters in hangman_word:
    word_legnth += 1

word_descovered = "_ "*word_legnth
print(word_descovered)   

tries = word_legnth + 3

descovered_letter = False
guessed_letters = ""
while True:
    letter_count = 0
    input_letter = input("input letter:\n")
    for letters in input_letter:
        letter_count += 1
        if letter_count >= 2:
            is_word = True
            break
        else:
            is_word = False
    if is_word == True and input_letter == hangman_word:
        print("je hebt het woord goed geraden")
        break
    elif is_word == True and input_letter != hangman_word:
        tries -=1
        print("dat it niet het woord")
    else:
        for is_letter_in in hangman_word:
            if input_letter != is_letter_in:
                letter_in_word = False
            else:
                letter_in_word = True
                guessed_letters = guessed_letters + input_letter
                break
        if letter_in_word == False:
            tries -= 1
    
    if is_word == False:
        word_descovered = ""
        for characters in hangman_word:
            for letter in guessed_letters:
                if characters == letter:
                    descovered_letter = True
                    break
                else:
                    descovered_letter = False
            if characters == input_letter or descovered_letter == True:
                descovered_character = characters+ " "
            else:
                descovered_character = "_ "
            word_descovered = word_descovered + descovered_character
        print(word_descovered)
    
    if tries <= 0:
        print("je hebt verloren het woord was", hangman_word)
        break

    for character in hangman_word:
        if character not in guessed_letters:
            correct = False
            break
        else:
            correct = True
    
    if correct == True:
        print("je hebt gewonnen")
        break