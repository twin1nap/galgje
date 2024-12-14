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



# vragen om input voor het woordt dat geraden moet worden
hangman_word = input("welk wordt moet er geraden worden?\n")
# print 1037 lege regels zodat de speler het ingevoerde woord niet terug kan vinden
print("\n"*1037)
# zet het aantal keer proberen voordat de speler verloren heeft op 10
tries = 10

# zet de lengte van het woordt op 0
word_legnth = 0
# loopt door elke letter in het woord
for characters in hangman_word:
    # telt 1 op de lengte van het woord
    word_legnth += 1

# maakt woord_descovered de streepjes die aan het begin worden laten zien
word_descovered = "_ "*word_legnth
# laat de streepjes zien
print(word_descovered)         

# zet descovered_letter op false zodat de letter standaard nog niet gevonden is voordat de ronde begint.
descovered_letter = False
# zet de lijst met de gevonden letters leeg zodat voor dat het spel begint er nog geen gevonde letters zijn.
guessed_letters = ""
# start de game loop
while True:
    # zet het aantal letters dat die beurt wordt ingevoerd op 0
    letter_count = 0
    # vraagt om een input van de speler
    input_letter = input("input letter:\n")
    # loopt door elke letter in het woord
    for letters in input_letter:
        # telt 1 bij de aantal letters op
        letter_count += 1
        # kijkt of er meer dan 1 letter is ingevoerd
        if letter_count >= 2:
            # onthoud dat de input een woord is
            is_word = True
            # stopt het tellen van de letters die zijn ingevoerd
            break
        # als de input geen woord is
        else:
            # onthoud dat de input geen woord is
            is_word = False
    # als de input een woord is en de input die is ingevoerd het woord is dat geraden moet worden
    if is_word == True and input_letter == hangman_word:
        # zegt dat je hebt gewonnen
        print("je hebt het woord goed geraden")
        #stopt het spel
        break
    # als de input een woord is maar de input niet het woors is dat geraden moet worden.
    elif is_word == True and input_letter != hangman_word:
        # haalt 1 van het aantal keer proberen af
        tries -=1
        # zegt dat de input niet het woord is
        print("dat it niet het woord")
    # als de input niet een woord is
    else:
        # gaat langs elke letter in het woord dat geraden mmoet worden
        for is_letter_in in hangman_word:
            # als de input niet de letter is waar die op dat moment mee aan het vergelijken is.
            if input_letter != is_letter_in:
                # onthoud dat de ingevoerde letter niet in het woord zit
                letter_in_word = False
            # als de inout letter wel de letter is waarmee wordt vergeleken
            else:
                # onthoud dat de ingevoerde letter in het woord zit.
                letter_in_word = True
                # zet de ingevoerde letter in de lijst met alle goed geraden letters
                guessed_letters = guessed_letters + input_letter
                # stopt met het kijken of de ingevoerde letter in het woord zit wanr die uitkomst is er al.
                break
        # als naar het kijken of de letter in het woord zit de uitkomst is dat het letter er niet in zit.
        if letter_in_word == False:
            # haal 1 af van het aantal keer proberen.
            tries -= 1
    
    # kijt of de input geen woord was zodat de loop in de if alleen maar word gedaan als er een letter is ingevoerd
    if is_word == False:
        # maakt word_descovered leeg zodat er een nieuwe gemaakt kan worden die de goed geraden letters laat zien.
        word_descovered = ""
        # gaat langs elke letter in het woord dat geraden moet worde.
        for characters in hangman_word:
            # gaat langs elke letter die al geraden is
            for letter in guessed_letters:
                # als de letter uit het woord dat geraden moet worden waarmee op dit moment wordt vergeleken de zelfde leters is als de letter waarmee wordt vergeleken uit de lijst met al geraden letters
                if characters == letter:
                    # zet dat die letter al gevonden is op true
                    descovered_letter = True
                    # stop met het kijken of die letter uit het hangman woord al gevonden is
                    break
                # als de letter uit het hangman woord nog niet gevonden is
                else:
                    #zet dat de letter al gevonden is op false
                    descovered_letter = False
            # als de letter uit het hangman woord hetzelde is als de ingevoerde letter of de letter is al gevonden
            if characters == input_letter or descovered_letter == True:
                # laat die letter zien in plaats van een streepje en zet dan een spatie neer
                descovered_character = characters+ " "
            # als de letter uit het hangman woord niet de zelfde is als het ingevoerde woord of de letter nog niet gevonden is
            else:
                # zet een streepje neer inplaats van de letter
                descovered_character = "_ "
            # plak alle letters en streepjes achter elkaar
            word_descovered = word_descovered + descovered_character
        # laat zien wat er tot nu toe is geraden
        print(word_descovered)
    
    # als het aantal keer nog proberen 0 of lager is
    if tries <= 0:
        # zeg dat de speler verloren heeft
        print("je hebt verloren het woord was", hangman_word)
        # stop het spel zodat de speler niet nog een keer kan proberen
        break

    # gaat elke letter langs in het woord dat geraden moet worden
    for character in hangman_word:
        # als de huidige leter die wordt vergeleken niet in de lijst met al goed geraden letters zit
        if character not in guessed_letters:
            # zet dat alle letters geraden zijn op false
            correct = False
            # stop met kijken of alle letters al geraden is want de uitkomst daarop is al nee
            break
        # als elke letter al geraden is
        else:
            # zet dat alle letters geraden zijn op true
            correct = True
    
    # als alle letters geraden zijn
    if correct == True:
        # zeg tegen de speler dat hij/zij gewonnen heeft
        print("je hebt gewonnen")
        # stop het spel zodat de speler niet meer letters kan raden want hij/zij heeft al gewonnen
        break