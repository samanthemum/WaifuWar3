define rom = Character('Romeo')

label romeo_start:
    python:
        romDialogPositive = DialogGenerator("writing/romeo/romeo_positive.txt")
        romDialogNegative = DialogGenerator("writing/romeo/romeo_negative.txt")
        romDialogApathetic = DialogGenerator("writing/romeo/romeo_apathy.txt")
    play music "Romeo.mp3"
    
label romeo:
    $ iconlist = mcMood.imageMoodIcon()
    
    image icon1 = "images/"+"[iconlist[0]]"+".png"
    
    image icon2 = "images/"+"[iconlist[1]]"+".png"
        
    $ iconlove = romAffection.imageLoveLevel()
    
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
    show romeo_neutral at right
    if romAffection.infatuated == True:
        jump rom_love
    rom "Hey. It's been a while. What's up?"
    
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
            jump romeo_response
        
        "[text2]":
            jump romeo_response
            
        "[text3]":
            jump romeo_response
            
        "[text4]":
            jump romeo_response
            
        "I gotta go.":
            stop music fadeout 1.0
            hide romeo_neutral
            hide imageiconlove
            jump character_screens

label romeo_response:
    if mcMood.currentmood == "angry":
        $ response = romDialogApathetic.generateDialog()
        rom "[response]"
        $ mcMood.increaseSadcounter()
    elif mcMood.currentmood == "happy":
        hide romeo_neutral
        show romeo_negative at right
        $ response = romDialogNegative.generateDialog()
        rom "[response]"
        $ mcMood.increaseAngrycounter()
        hide romeo_negative
        show romeo_neutral at right
    elif mcMood.currentmood == "sad":
        hide romeo_neutral
        show romeo_positive at right
        $ response = romDialogPositive.generateDialog()
        rom "[response]"
        $ mcMood.increaseHappycounter()
        $ romAffection.increaseLoveLevel()
        hide romeo_positive
        show romeo_neutral at right
        
    
        
    if mcMood.moodSwung == True:
        jump rom_mood_swing
        
    jump romeo
        
label rom_mood_swing:
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
    
    $ iconlist = mcMood.imageMoodIcon()
    
    image icon1 = "images/"+"[iconlist[0]]"+".png"
    
    image icon2 = "images/"+"[iconlist[1]]"+".png"
    
    image mcimage = "images/"+"[imagetitle]"+".png"
        
    hide headspace
    with fade
        
    jump romeo
    
label rom_love:
    rom "I feel really happy when I'm with you."
    
    rom "Do you want to go on an actual date?"
    
    menu:
        "Of course!":
            rom "I'm already excited."
            rom "I can't wait."
            
            
            scene romeoend
            with fade
            
            "The two shared many dates together, their hearts only growing fonder."
            
            return
            
        "Not really.":
            rom "That's okay, I wouldn't date me either."
            
            $ romAffection.lovelevel = 0
            
            jump romeo
    
    return
    
    
    
    return


