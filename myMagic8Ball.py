#myMagic8Ball
import random
#put answers in a tuple
answers = (
    "Go for it!",
    "No way, Jose!",
    "I'm not sure. Ask me again.",
    "Fear of the unknown is what imprisons us.",
    "It would be madness to do that!",
    "Only you can save mankind!",
    "Makes no difference to me, do or don't - whatever.",
    "Yes, I think on balance that is the right choice."
    )
print("Welcome to MyMagic8Ball.")
#get the user's question
question = input("Ask me for advice then press ENTER to shake me.\n")
print("shaking...\n"*4)
#use the randint() function to select the correct answer
choice = random.randint(0, 7)
#print the answer to the screen
print(answers[choice])
#exit nicely
input("\n\nPress the RETURN key to finish.")
