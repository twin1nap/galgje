# vragen om input voor het woordt dat geraden moet worden                                           [X]
# laten zien hoelang het woordt is met streepjes: "_ _ ..."                                         [x]
# loop:                                                                                             [ ]
#   input letter                                                                                    [x]
#   conteroleer of de letter er in zit                                                              [x]
#   conteroleer of de letter al geraden is                                                          [ ]
#   letter goed:                                                                                    [ ]
#       laat die letter in het woordt zien                                                          [ ]
#   letter fout:                                                                                    [ ]
#       laat de man hangen en laat zien dt die letter verkeerd is                                   [ ]
#       kansen - 1                                                                                  [ ]
#   als alle letter goed zijn:                                                                      [ ] 
#       zeggen dat het woordt geraden is                                                            [ ]
#   als het aantal keer proberen op is:                                                             [ ]
#        meling geven dat de speler verloren heeft                                                  [ ]
tries = 3
hangman_word = input("welk wordt moet er geraden worden?\n") 


word_legnth = 0                         #-| 
for characters in hangman_word:         # |- telt de letters
    word_legnth += 1                    #-|

word_descovered = "_ "*word_legnth      #-|
print(word_descovered)                  #-|- prints de "_ "           

guessed_letters = ""                                            #-|
while True:                                                     # |
    input_letter = input("input letter:\n")                     # |
    for a in hangman_word:                                      # |
        if input_letter != a:                                   # |
            letter_in_word = False                              # |- kijkt of het letter in het woord zit.(conteroleer of de letter er in zit)
        else:                                                   # |
            letter_in_word = True                               # |
            guessed_letters = guessed_letters + input_letter    # |
            break                                               # |
    print(letter_in_word)                                       #-|

    word_descovered = ""                     # ]- resets word_descovered
    for characters in hangman_word:                                 #-|
        if characters == input_letter:                              # |
            discovered_character = input_letter+ " "                # |
        else:                                                       # |- laat de plekken van de letters zien als ze zijn gevonden.(#   letter goed: laat die letter in het woordt zien)
            discovered_character = "_ "                             # |
        word_descovered = word_descovered + discovered_character    # |
    print(word_descovered)                                          #-|
    print(guessed_letters)

            

