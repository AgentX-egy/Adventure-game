import random
StoryChapters = {0: "Prolog.txt", 1: "Chapter1.txt", 2: "Chapter2.txt"}

with open("Game_Instructions.txt") as txt:
    Ohelp = txt.read()


def cls():
    n = "-" * 15
    print ("\n"+n)*30


def sls():
    n = "-" * 95
    print n


def findline(fromFileName, lineno):
    with open(fromFileName) as fn:
        for line in fn:
            if lineno in line:
                return line.lstrip(lineno)


def StoryTeller(Tolevel):
    with open(StoryChapters[Tolevel]) as txt:
        for line in txt:
            print (str(line).strip()), raw_input()
    cls()
    if Tolevel == 0:
        print (Ohelp)


def RoomDetails(Inroom, Inlevel):
    '''Finds the room description paragraph and then formates it'''
    # Find room description
    with open("rooms_description.txt") as txt:
        description = txt.readlines()
        description.sort()
        del description[0:5]
        ref = 4*Inroom + Inlevel
        description = description[ref]
    # Formate the description
    description = description[2:]
    try:
        repr(description).format('\n', '\t')
    finally:
        return description


def level0(room_num, inventory):
    if room_num == 1:
        if "Red key" in inventory:
            inventory.pop(inventory.index("Red key"))
            print ("Invertory: "+str(inventory))
            return True
    else:
        print (findline("Think_Hints.txt", str(random.randint(0, 1))+"0"))
        return False


def level1(room_num):
    if room_num == 6:
        password = '3985'
        guess = raw_input('> "Do you know the password?"'+"\n>> ")
        if guess == password:
            return True
        else:
            print ('> "Wrong!"')
            return False
    else:
        print (findline("Think_Hints.txt", str(random.randint(0, 1))+"1"))
