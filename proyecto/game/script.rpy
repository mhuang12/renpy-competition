# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define TL = Character("Team Leader")
define Friend = Character("Friend")
define Nerd = Character("Nerd")
define LT = Character("Lab Tech")

default life = 0
default greed = 0
default war = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg confroom #WIP
    "Hello…. Is anyone there?"
    "This is mining team –bzzst– We were on a routine check when we came across a –bzzst–."
    "There’s nobody left. I- I don’t know what happened."
    "There was a cave-in."
    "We fell into uncharted territory and encountered the object. One touch and we saw it."
    "Visions. Chaos. Quickly we descended into conflict."
    "Fighting for –bzzst– power. If this message reaches you, please, please send help."
    "We’ve seen what can happen."
    "Please help us."
    show tl at left
    TL "As you can see from this audio transmission, we have no idea what kind of power lies beneath."
    TL "All we know is that whatever it is, it was able to drive an entire team to madness."
    TL "Imagine, the whole world at your fingertips with this kind of power."
    show friend at right
    Friend "Friend: Do you really think that there’s something in these caves that could drive an entire team insane?"
menu:
    "I’m not too sure":
        Friend "Yeah, me neither. Honestly it sounds crazy."
        jump conf
    "Either way, we’re gonna be rich":
        Friend "With all the money Mr. [CEO NAME] has, we better be well-compensated."
        $greed += 1
        jump conf
    "Sure, I mean stranger things have happened right?":
        Friend "I don’t know about that, but I like your optimism"
        $life += 1
        jump conf

label conf:
    TL "Now, the reason you have been chosen is because you are the best of the best on our payroll."
    TL "Private contractors with a history of success in every field you’ve worked in. Specialists that can accomplish any task we have given you."
    TL "Your skills will be necessary if you are to retrieve this object."
    TL "Are there any questions?"
menu:
    "*Silence*":
        TL "Good, then let’s get started."
        jump dig1
    "How much am I getting paid to do this?":
        TL "Not as much as I am, surely."
        $greed += 1
        jump dig1
    "When do we get to go home?":
        TL "When you retrieve the item for our employer, idiot."
        $war += 1
        jump dig1

label dig1:
    hide friend
    hide tl
    scene bg digsite #WIP
    show nerd at left
    Nerd "Hey, have you seen my pen anywhere? It was one of a kind and I really need to find it."
menu:
    "No, but I’ll keep an eye out":
        Nerd "Really? Thanks!"
        jump dig2
    "Do I get something in return?":
        Nerd "Surely you’d do this out of the kindness of your own heart?"
        Nerd "But I guess I could give you something for finding it."
        $greed += 1
        jump dig2
    "Your pen means nothing. I couldn’t care any less than I do right now.":
        Nerd "Wow. That’s harsh."
        $war += 1
        jump dig2

label dig2:
    show TL annoyed at right
    TL "If everyone could focus, that would be great."
menu:
    "Right, sorry":
        TL "Let’s get back to business"
        jump dig3
    "I’m trying to have a conversation here?":
        TL "You’re not getting paid to socialize with your coworkers. Pay attention."
        jump dig3
    "He started talking to me first.":
        TL "I care why?"
        jump dig3

label dig3:
    TL "Anyway, our first expedition is tonight. Make sure you all are prepared at 1800 hours."
    TL "I expect there to be full concentration and cooperation."
    show friend sarcastic
    Friend "I can’t wait to go crazy and go missing like they did!"
    return
