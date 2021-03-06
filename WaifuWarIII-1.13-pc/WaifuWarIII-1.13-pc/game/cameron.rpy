define cam = Character('Cameron')
label cameron_start:
    python:
        camDialogPositive = DialogGenerator("writing/cameron/cameron_positive.txt")
        camDialogNegative = DialogGenerator("writing/cameron/cameron_negative.txt")
        camDialogApathetic = DialogGenerator("writing/cameron/cameron_apathy.txt")
    play music "Cameron.mp3"
    
label cameron:
    
    
    $ iconlist = mcMood.imageMoodIcon()
    
    image icon1 = "images/"+"[iconlist[0]]"+".png"
    
    image icon2 = "images/"+"[iconlist[1]]"+".png"
        
    $ iconlove = camAffection.imageLoveLevel()
    
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
    show cameron_neutral at right
    if camAffection.infatuated == True:
        jump cameron_love
    cam "What can I do for you, mon ami?"
    
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
            jump cam_response
        
        "[text2]":
            jump cam_response
            
        "[text3]":
            jump cam_response
            
        "[text4]":
            jump cam_response
            
        "I gotta go.":
            stop music fadeout 1.0
            hide cameron_neutral
            hide imageiconlove
            jump character_screens

label cam_response:
    if mcMood.currentmood == "angry":
        hide cameron_neutral
        show cameron_negative at right
        $ response = camDialogNegative.generateDialog()
        cam "[response]"
        $ mcMood.increaseSadcounter()
        $ camAffection.decreaseLoveLevel()
        hide cameron_negative
        show cameron_neutral at right
    elif mcMood.currentmood == "happy":
        $ response = camDialogApathetic.generateDialog()
        $ mcMood.increaseAngrycounter()
        cam "[response]"
    elif mcMood.currentmood == "sad":
        hide cameron_netural
        show cameron_positive at right
        $ response = camDialogPositive.generateDialog()
        cam "[response]"
        $ mcMood.increaseHappycounter()
        $ camAffection.increaseLoveLevel()
        hide cameron_positive
        show cameron_neutral
        
        
    if mcMood.moodSwung == True:
        jump cameron_mood_swing
        
    jump cameron
        
label cameron_mood_swing:
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
        
    jump cameron
    
label cameron_love:
    cam "I think I've grown rather fond of you."
    cam "I would be honored if you'd join me on a date?"
    
    menu:
        "I'd love to!":
            cam "I'm honored!"
            
            scene cameronend
            with fade
            
            "And with that, their courtship flourished."
            
            return
        
        "I'd rather not...":
            
            cam "That's ok... I understand."
            
            $ camAffection.lovelevel = 0
            
            jump cameron
    
    
    
    return


