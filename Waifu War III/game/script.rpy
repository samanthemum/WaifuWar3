# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    import random
    class Affection:
        """A class to keep track of different's affections towards the main character"""
        def __init__(self):
            self.lovelevel = 0
            self.infatuated = False
            
        
        def checkLove(self):
            if self.lovelevel >= 5:
                self.infatuated = True
        
        def decreaseLoveLevel(self):
            if self.lovelevel == 0:
                self.lovelevel = 0
            else:
                self.lovelevel-=1
        
        def increaseLoveLevel(self):
            self.lovelevel+=1
            self.checkLove()
            
        def imageLoveLevel(self):
            if self.lovelevel == 0:
                return "love0"
            elif self.lovelevel == 1:
                return "love1"
            elif self.lovelevel == 2:
                return "love2"
            elif self.lovelevel == 3:
                return "love3"
            elif self.lovelevel == 4:
                return "love4"
            elif self.lovelevel >= 5:
                return "love5"

        
    class Mood:
        """A class to keep track of the main character's mood"""
        def __init__(self):
            self.currentmood = "happy"
            #Set happy to the default mood
            
            self.happycounter = 0
            self.sadcounter = 0
            self.angrycounter = 0
            self.moodSwung = False
            #create counter objects to
        
        def checkMood(self):
            if self.currentmood != "happy" and self.happycounter == 3:
                self.currentmood = "happy"
                self.happycounter = 0
                self.sadcounter = 0
                self.angrycounter = 0
                self.moodSwung = True
                
            elif self.currentmood != "angry" and self.angrycounter == 3:
                self.currentmood = "angry"
                self.happycounter = 0
                self.sadcounter = 0
                self.angrycounter = 0
                self.moodSwung = True
                
            elif self.currentmood != "sad" and self.sadcounter == 3:
                self.currentmood = "sad"
                self.happycounter = 0
                self.sadcounter = 0
                self.angrycounter = 0
                self.moodSwung = True
                
            else:
                self.moodSwung = False
                
        def increaseSadcounter(self):
            self.sadcounter +=1
            self.checkMood()
            
        def increaseHappycounter(self):
            self.happycounter +=1
            self.checkMood()
            
        def increaseAngrycounter(self):
            self.angrycounter +=1
            self.checkMood()
            
        def imageMoodIcon(self):
            if self.currentmood == "angry":
                return "happy"+str(self.happycounter),"sad"+str(self.sadcounter)
            elif self.currentmood == "sad":
                return "happy"+str(self.happycounter),"anger"+str(self.angrycounter)
            elif self.currentmood == "happy":
                return "anger"+str(self.angrycounter),"sad"+str(self.sadcounter)
            else:
                return "ERROR"
                
        def imageMood(self):
            if self.currentmood == "angry":
                return "collar"
            elif self.currentmood == "happy":
                return "sangria"
            elif self.currentmood == "sad":
                return "melon"
            
            
    class DialogGenerator:
        
        def __init__(self, filename):
            self.dialog = []
            inputfile = renpy.file(filename).read().decode("utf-8")
            inputfile = inputfile.split("\n")
            for item in inputfile:
                if len(item) > 1:
                    self.dialog.append(item[:-1])
                
            
        def generateDialog(self):
            index = random.randint(0, len(self.dialog)-1)
            return self.dialog[index]
        

#define the main character
define mc = Character("MC")


label start:
    jump howtoplay
    
    
label posttutorial:
    scene headspace
    with dissolve
    
    play music "Post_Arockalypse.mp3"
    
    "God, do I need a girlfriend."
    "Or boyfriend. I'm not picky."
    "At this rate, I'm going to die alone."
    
    $camAffection = Affection()
    $charAffection = Affection()
    $katAffection = Affection()
    $hansAffection = Affection()
    $romAffection = Affection()
    
    $ mcMood = Mood() 

    scene bg
    
    $ imagetitle = mcMood.imageMood()
    
    $ iconlist = mcMood.imageMoodIcon()
    
    image icon1 = "images/"+"[iconlist[0]]"+".png"
    
    image icon2 = "images/"+"[iconlist[1]]"+".png"

    image mcimage = "images/"+"[imagetitle]"+".png"
    
    show mcimage
    
    show icon1:
        xalign 0
        yalign 0
        
    show icon2:
        xalign .07
        yalign 0
    
    
    

    $ mcAngryDialog = DialogGenerator("writing/mc_angry/mc_angry.txt")
    $ mcHappyDialog = DialogGenerator("writing/mc_happy/mc_happy.txt")
    $ mcSadDialog = DialogGenerator("writing/mc_sad/mc_sad.txt")
    
   

    # These display lines of dialogue.

    

    # This ends the game.

label character_screens:
    
    play music "Post_Arockalypse.mp3"
    
    
    "Who should I talk to?"
    
    menu:
        "Cameron":
            stop music fadeout 1.0
            hide mcimage
            jump cameron_start
        "Charlotte":
            stop music fadeout 1.0
            hide mcimage
            jump charlotte_start
        "Hans":
            stop music fadeout 1.0
            hide mcimage
            jump hans_start
        "Katerina":
            stop music fadeout 1.0
            hide mcimage
            jump katerina_start
        "Romeo":
            stop music fadeout 1.0
            hide mcimage
            jump romeo_start
        "I need a break from this hot, steamy romance.":
            stop music fadeout 1.0
            return
    
label end:

    return
