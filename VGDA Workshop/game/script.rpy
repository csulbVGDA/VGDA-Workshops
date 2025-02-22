# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mis = Character("Mitra", image="mitra")
define mel = Character("Melisande", image="melisande")

#Background
image bg road = "images/background.jpg"

#Character Images
image mis casual = "mitra_casual_neutral.png"
image mel casual = "melisande_shopkeeper_neutral.png"


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

    show mis casual at left
    show mel casual at right
    with dissolve

    # These display lines of dialogue.

    mis "You've created a new Ren'Py game."

    mel "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
