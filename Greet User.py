import random
from better_profanity import profanity


class color:
    RED = '\033[91m'
    END = '\033[0m'


greeting = ['Hello', 'Welcome', 'Hi', 'Hola', 'Greetings', 'Dia duit']
wish = ["Hope you're having a great week", "Hope you're having a great day", "Hope you're well",
        "Hope you're good", "Hope all's well with you"]
value1 = random.choice(greeting)
value2 = random.choice(wish)


def greet_user(name):
    while profanity.contains_profanity(name):
        name = input("Don't be cheeky! What's " + color.RED + "REALLY" + color.END + " your name?")
    while not str.isalpha(name):
        name = input("You didn't enter your name! What's your name, stranger?")
    else:
        place = input(value1 + " %s! Where are you from?" % name)
        while profanity.contains_profanity(place):
            place = input("Well that's not true! Where are you from?")
        while not str.isalpha(place):
            place = input("Did you forget to type something? Where are you from, %s?" % name)
        hobbies = input(
            "%s, I bet it's lovely there! And what are your hobbies?" % place
        )
        while profanity.contains_profanity(hobbies):
            hobbies = input("Excuse me! What hobbies do you have - that you can mention in polite society?")
        while not str.isalpha(hobbies):
            hobbies = input(
                "I'm sure you have more hobbies than that! What do you like to do?"
            )
        animal = input(
            "%s, how interesting! And what's your favourite animal?" % hobbies
        )
        while not str.isalpha(animal):
            animal = input("You forgot to type! What's your favourite animal?")
        while profanity.contains_profanity(animal):
            animal = input("...I don't think those are animals! What's your favourite animal?")
        if animal == "Python" or animal == "python" or animal == "pythons" or animal == "Pythons":
            print("Hahahah, you know it! :-) " + value2 + ", %s!" % name)
        else:
            print("%s, Not Pythons? :-( Oh well. Have a great day anyways!" % animal)


name = input("Hi there, what's your name?\n")
greet_user(name)
