print("You enter a dark room with 2 doors. \n Do you go through door #1 or door #2 ")
door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear")
    
    bear = input("> ")

    if bear == '1':
        print("The bear eats your face off. Good job!")
    elif bear == '2':
        print("The bear eats your leg off. Good job!")
    else:
        print("Well doing {} is probably better".format(bear))
        print("Bear runs away")

elif door == '2':
    print("You stare into the endless abyss of Cthulhu's retina")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == '1' or insanity == '2':
        print("Your body survives by a mind of jello")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck")
        print("Good job!")
else: 
    print("You stumble around and fall on a knife and die. Good job!")
