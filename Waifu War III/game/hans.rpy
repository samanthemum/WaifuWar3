define hans = Character('Hans')
label hans_start:
    python:
        hansDialogPositive = DialogGenerator("writing/hans/hans_positive.txt")
        hansDialogNegative = DialogGenerator("writing/hans/hans_negative.txt")
        hansDialogApathetic = DialogGenerator("writing/hans/hans_apathy.txt")
    play music "Hans.mp3"
    
label hans:
    $ iconlist = mcMood.imageMoodIcon()
    
    image icon1 = "images/"+"[iconlist[0]]"+".png"
    
    image icon2 = "images/"+"[iconlist[1]]"+".png"
        
    $ iconlove = hansAffection.imageLoveLevel()
    
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
    show hans_neutral at right
    if hansAffection.infatuated == True:
        jump hans_love
    hans "What do you want?"
    
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
            jump hans_response
        
        "[text2]":
            jump hans_response
            
        "[text3]":
            jump hans_response
            
        "[text4]":
            jump hans_response
            
        "I gotta go.":
            stop music fadeout 1.0
            hide hans_neutral
            hide imageiconlove
            jump character_screens

label hans_response:
    if mcMood.currentmood == "angry":
        hide hans_neutral
        show hans_positive at right
        $ response = hansDialogPositive.generateDialog()
        hans "[response]"
        $ mcMood.increaseHappycounter()
        $ hansAffection.increaseLoveLevel()
        hide hans_positive
        show hans_neutral at right
    elif mcMood.currentmood == "happy":
        $ response = hansDialogApathetic.generateDialog()
        hans "[response]"
        $ mcMood.increaseSadcounter()
    elif mcMood.currentmood == "sad":
        hide hans_neutral
        show hans_negative at right
        $ response = hansDialogNegative.generateDialog()
        hans "[response]"
        $ mcMood.increaseAngrycounter()
        $ hansAffection.decreaseLoveLevel()
        hide hans_negative
        show hans_neutral at right
        
    
        
    if mcMood.moodSwung == True:
        jump hans_mood_swing
        
    jump hans
        
label hans_mood_swing:
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
        
    jump hans
    
label hans_love:
    hans "Even if I loathe to admit, I think I'm into you."
    hans "Want to hook up?"
    
    menu:
        "Why wouldn't I?":
            hans "I know, but I was still nervous."
            hans "C'mon, let's go."
            
            scene hansend
            with fade
            
            "Hans and MC would stay together for a very, very long time."
            
            return
        
        "You're not the one for me":
            hans "Well, you're nothing special either!"
            hans "Whatever. Just get out of my face."
            
            $ hansAffection.lovelevel = 0
            
            jump hans
    
    return
    
    
    
    return


