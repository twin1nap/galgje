# vragen om input voor het woordt dat geraden moet worden                                           [X]
# laten zien hoelang het woordt is met streepjes: "_ _ ..."                                         [x]
# loop:                                                                                             [ ]
#   input letter                                                                                    [x]
#   conteroleer of de letter er in zit                                                              [x]
#   letter goed:                                                                                    [ ]
#       laat die letter in het woordt zien                                                          [ ]
#   letter fout:                                                                                    [ ]
#       laat de man hangen en laat zien dt die letter verkeerd is                                   [ ]
#       kansen - 1                                                                                  [ ]
#   als alle leeter goed zijn:                                                                      [ ] 
#       zeggen dat het woordt geraden is                                                            [ ]
#   als het aantal keer proberen op is:                                                             [ ]
#        meling geven dat de speler verloren heeft                                                  [ ]

hangman_word = input("welk wordt moet er geraden worden?\n")

word_legnth = ""                        #-|
for legnth in hangman_word:             # |-- maybe replace with counting the letters and then print "_ " * word_leght
    word_legnth = word_legnth+"_ "      # |
print(word_legnth)                      #-|

while True:
    input_letter =input("input letter:\n")
    for a in hangman_word:
        if input_letter != a:
            letter_in_word = False
        else:
            letter_in_word = True
            break
    print(letter_in_word)
    word_legnth = "" 
