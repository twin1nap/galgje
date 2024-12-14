# vragen om input voor het woordt dat geraden moet worden                                           [X]
# legen regels zodat je de input niet terug kan vinden                                              [x]
# laten zien hoelang het woordt is met streepjes: "_ _ ..."                                         [x]
# loop:                                                                                             [x]
#   input                                                                                           [x]
#   conteroleer of het een wood is                                                                  [x]
#   als woord:                                                                                      [x]
#       als woord goed is:                                                                          [x]
#           spel gewonnen                                                                           [x]
#       als woord fout is:                                                                          [x]
#           tries - 1                                                                               [x]
#           zeg dat het woord fout is                                                               [x]
#   als niet woord:                                                                                 [x]
#       conteroleer of de letter er in zit                                                          [x]
#       letter goed:                                                                                [x]
#           laat die letter in het woordt zien                                                      [x]
#       letter fout:                                                                                [x]
#           kansen - 1                                                                              [x]
#   als alle letter geraden zijn:                                                                   [x] 
#       zeggen dat het woordt geraden is                                                            [x]
#   als het aantal keer proberen op is:                                                             [x]
#        meling geven dat de speler verloren heeft en zeggen wat het woord is                       [x]

hangman_word = input("welk wordt moet er geraden worden?\n") # vragen om input voor het woordt dat geraden moet worden
print("\n"*1037) 
tries = 10


word_legnth = 0                         #-| 
for characters in hangman_word:         # |- telt de letters
    word_legnth += 1                    #-|

word_descovered = "_ "*word_legnth      #-|
print(word_descovered)                  #-|- prints de "_ "           

descovered_letter = False
guessed_letters = ""                                            #-|
while True:                                                     # |
    letter_count = 0
    input_letter = input("input letter:\n")                     # |
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
        for is_letter_in in hangman_word:                           # |
            if input_letter != is_letter_in:                        # |
                letter_in_word = False                              # |- kijkt of het letter in het woord zit.(conteroleer of de letter er in zit)
            else:                                                   # |
                letter_in_word = True                               # |
                guessed_letters = guessed_letters + input_letter    # |
                break                                               # |
                                                                    #-|
        if letter_in_word == False:
            tries -= 1
    
    if is_word == False:
        word_descovered = ""                                                    #-|
        for characters in hangman_word:                                         # |
            for letter in guessed_letters:                                      # |
                if characters == letter:                                        # |
                    descovered_letter = True                                    # |
                    break                                                       # |
                else:                                                           # |
                    descovered_letter = False                                   # |-laat die letter in het woordt zien
            if characters == input_letter or descovered_letter == True:         # |
                descovered_character = characters+ " "                          # |
            else:                                                               # |
                descovered_character = "_ "                                     # |
            word_descovered = word_descovered + descovered_character            # |
        print(word_descovered)                                                  #-|

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