define kat = Character('Katerina')

label katerina_start:
    python:
        katDialogPositive = DialogGenerator("writing/katerina/katerina_positive.txt")
        katDialogNegative = DialogGenerator("writing/katerina/katerina_negative.txt")
        katDialogApathetic = DialogGenerator("writing/katerina/katerina_apathy.txt")
    play music "Katerina.mp3"
    
label kat:
    $ iconlist = mcMood.imageMoodIcon()
    
    image icon1 = "images/"+"[iconlist[0]]"+".png"
    
    image icon2 = "images/"+"[iconlist[1]]"+".png"
        
    $ iconlove = katAffection.imageLoveLevel()
    
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
    show katerina_neutral at right
    if katAffection.infatuated == True:
        jump kat_love
    kat "Hi. Can I help you with something?"
    
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
            jump kat_response
        
        "[text2]":
            jump kat_response
            
        "[text3]":
            jump kat_response
            
        "[text4]":
            jump kat_response
            
        "I gotta go.":
            stop music fadeout 1.0
            hide katerina_neutral
            hide imageiconlove
            jump character_screens

label kat_response:
    if mcMood.currentmood == "angry":
        hide katerina_neutral
        show katerina_negative at right
        $ response = katDialogNegative.generateDialog()
        kat "[response]"
        $ mcMood.increaseSadcounter()
        $ katAffection.decreaseLoveLevel()
        hide katerina_negative
        show katerina_neutral at right
    elif mcMood.currentmood == "happy":
        hide katerina_neutral
        show katerina_positive at right
        $ response = katDialogPositive.generateDialog()
        kat "[response]"
        $ mcMood.increaseSadcounter()
        $ katAffection.increaseLoveLevel()
        hide katerina_positive
        show katerina_neutral at right
    elif mcMood.currentmood == "sad":
        $ response = katDialogApathetic.generateDialog()
        kat "[response]"
        $ mcMood.increaseAngrycounter()
        
    
        
    if mcMood.moodSwung == True:
        jump kat_mood_swing
        
    jump kat
        
label kat_mood_swing:
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
        
    jump kat
    
label kat_love:
    kat "It's not like I like you or anything, but do you want to go on a date sometime?"
    
    menu:
        "Sure!":
            kat "Really?!?"
            kat "I mean, I knew you'd say that."
            
            scene katerinaend
            with fade

            "The couple's love for eachother would only continue to grow."
            
            return
            
        "I don't think so.":
            kat "Oh... okay."
            
            $ katAffection.lovelevel = 0
            
            jump katerina
    
    return
    
    
    
    return


