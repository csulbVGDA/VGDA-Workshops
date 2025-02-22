# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mis = Character("Mitra", image="mitra")
define mel = Character("Melisande", image="melisande")

#Background
image bg road = "images/background.jpg"

#Character Images
image mis casual = "mitra_casual_neutral.png"
image mis sad = "mitra_casual_sad.png"
image mel casual = im.Flip("melisande_shopkeeper_neutral.png", horizontal=True)
image mel laugh = im.Flip("melisande_shopkeeper_happy.png", horizontal=True)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg road:
        zoom 1.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mis casual at right
    show mel casual at left
    with dissolve

    # These display lines of dialogue.

    mis "Hi Mel! How is your day?"

    show mel laugh at left
    mel "Hi Mistra! My day is great!"

    mis "I'm really happy to hear that!"

    mis "Do you wanna get coffee?"


    # Menu Option
    menu:

        "Yeah!":

            jump yes

        "No thanks":

            jump no

    # Yes response
    label yes:

        mel "Yes! I need coffee"

        mis "Great! Let's go!"

        return

    # No response
    label no:

        show mis sad at right
        mis "Oh...okay, see ya later"

    return
