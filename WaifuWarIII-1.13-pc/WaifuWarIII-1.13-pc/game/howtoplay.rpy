label howtoplay:
    show howto
    "This is a quick tutorial to teach you how the basics of the game. Press enter to continue."
    show anger0:
        xalign 0.5
        yalign 0.3
    show happy0:
        xalign 0.3
        yalign 0.3
    show sad0:
        xalign 0.7
        yalign 0.3
    "The above icons track the main character's emotion."
    "If the character feels too happy, or sad, or angry, they'll change shape."
    "Their emotional view changes how they see the world, thus how they interact with other characters."
    "Different characters respond to the tone of the main character in different ways."
    hide anger0
    with fade
    hide happy0
    with fade
    hide sad0
    with fade
    "Next, the matter of the waifus."
    show love0:
        xalign 0.5
        yalign 0.3
    "This icon will be in the upper right corner for each waifu."
    "It tracks how the waifu feels towards you."
    "When it is full, the waifu will ask the MC out on a date."
    hide love0
    with fade
    "Finally, option menus."
    "Menus will appear where you're expected to pick an option."
    "As usual, just click on the option you'd like."
    "Ready to start?"
    menu:
        "Yes!":
            jump story
        "I'd like to rehear the explanation of how to play.":
            jump howtoplay