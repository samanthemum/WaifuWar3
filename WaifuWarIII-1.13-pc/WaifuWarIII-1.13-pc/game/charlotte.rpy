define char = Character('Charlotte')
label charlotte_start:
    python:
        charDialogPositive = DialogGenerator("writing/charlotte/charlotte_positive.txt")
        charDialogNegative = DialogGenerator("writing/charlotte/charlotte_negative.txt")
        charDialogApathetic = DialogGenerator("writing/charlotte/charlotte_apathy.txt")
    play music "Charlotte.mp3"
    
label charlotte:
    $ iconlist = mcMood.imageMoodIcon()
    
    image icon1 = "images/"+"[iconlist[0]]"+".png"
    
    image icon2 = "images/"+"[iconlist[1]]"+".png"
        
    $ iconlove = charAffection.imageLoveLevel()
    
    image imageiconlove = "images/"+"[iconlove]"+".png"

    
    show icon1:
        xalign 0
        yalign 0
        
    show icon2:
        xalign .07
        yalign 0
        
    show imageiconlove:
        xalign .9
        yalign 0
    
    show mcimage at left
    show charlotte_neutral at right
    if charAffection.infatuated == True:
        jump charlotte_love
    char "What's up, buttercup?"
    
    python:
        if mcMood.currentmood == "angry":
            text1 = mcAngryDialog.generateDialog()
            text2 = mcAngryDialog.generateDialog()
            while text2 == text1:
                text2 = mcAngryDialog.generateDialog()
            text3 = mcAngryDialog.generateDialog()
            while text2 == text3 or text3 == text1:
                text3 = mcAngryDialog.generateDialog()
            text4 = mcAngryDialog.generateDialog()
            while text2 == text4 or text3 == text4 or text1 == text4:
                text4 = mcAngryDialog.generateDialog()
                
        if mcMood.currentmood == "happy":
            text1 = mcHappyDialog.generateDialog()
            text2 = mcHappyDialog.generateDialog()
            while text2 == text1:
                text2 = mcHappyDialog.generateDialog()
            text3 = mcHappyDialog.generateDialog()
            while text2 == text3 or text3 == text1:
                text3 = mcHappyDialog.generateDialog()
            text4 = mcHappyDialog.generateDialog()
            while text2 == text4 or text3 == text4 or text1 == text4:
                text4 = mcHappyDialog.generateDialog()
                
        if mcMood.currentmood == "sad":
            text1 = mcSadDialog.generateDialog()
            text2 = mcSadDialog.generateDialog()
            while text2 == text1:
                text2 = mcSadDialog.generateDialog()
            text3 = mcSadDialog.generateDialog()
            while text2 == text3 or text3 == text1:
                text3 = mcSadDialog.generateDialog()
            text4 = mcSadDialog.generateDialog()
            while text2 == text4 or text3 == text4 or text1 == text4:
                text4 = mcSadDialog.generateDialog()
    
    menu:
        "[text1]":
            jump char_response
        
        "[text2]":
            jump char_response
            
        "[text3]":
            jump char_response
            
        "[text4]":
            jump char_response
            
        "I gotta go.":
            stop music fadeout 1.0
            hide charlotte_neutral
            hide imageiconlove
            jump character_screens

label char_response:
    if mcMood.currentmood == "angry":
        hide charlotte_neutral
        show charlotte_negative at right
        $ response = charDialogNegative.generateDialog()
        char "[response]"
        $ mcMood.increaseSadcounter()
        $ charAffection.decreaseLoveLevel()
        hide charlotte_negative
        show charlotte_neutral at right
    elif mcMood.currentmood == "happy":
        hide charlotte_neutral
        show charlotte_positive at right
        $ response = charDialogPositive.generateDialog()
        char "[response]"
        $ mcMood.increaseSadcounter()
        $ charAffection.increaseLoveLevel()
        hide charlotte_positive
        show charlotte_neutral at right
    elif mcMood.currentmood == "sad":
        $ response = charDialogApathetic.generateDialog()
        char "[response]"
        $ mcMood.increaseAngrycounter()
        
        
    if mcMood.moodSwung == True:
        jump charlotte_mood_swing
        
    jump charlotte
        
label charlotte_mood_swing:
    hide mc
    show headspace
    with fade
    if mcMood.currentmood == "sad":
        mc "I'm feeling pretty down right now..."
        mc "Oh no, I'm going to change, aren't I?"
        mc "I don't wanna change."
    elif mcMood.currentmood == "happy":
        mc "I haven't felt this good in ages!"
        mc "I feel so light and happy."
        mc "Oh, I'm changing?"
    elif mcMood.currentmood == "angry":
        mc "God, I could scream right now."
        mc "I wanna start a fight."
        mc "Wait... you've got to be kidding me."
        
    $ imagetitle = mcMood.imageMood()
    
    image mcimage = "images/"+"[imagetitle]"+".png"

    $ iconlist = mcMood.imageMoodIcon()
        
    $ iconlove = charAffection.imageLoveLevel()
    
    image icon1 = "images/"+"[iconlist[0]]"+".png"
    
    image icon2 = "images/"+"[iconlist[1]]"+".png"
        
    hide headspace
    with fade
        
    jump charlotte
    
label charlotte_love:
    char "Hey, would you wanna go on a date sometime?"
    
    menu:
        "I'd love to! Let's go!":
            char "Where would you wanna go?"
            
            mc "Anywhere with you is where I wanna be."
            
            scene charlotteend
            with fade
            
            "That date would be the first, but far from the last."
            
            return
            
        "I'm just not that into you.":
            char "Then why would you play my heart like that?"
            char "Nevermind... just please don't play with me like that again."
            
            $ charAffection.lovelevel = 0
            
            jump charlotte
    
    return
    
    
    
    return


