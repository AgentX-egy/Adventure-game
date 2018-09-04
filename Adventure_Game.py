from Action_Modules import *

Playing = True


def Progress():
    if level_Info[1]:
        level_Info[1] = False
        level_Info[0] += 1
        StoryTeller(level_Info[0])
    if level_Info[0] == 4:  # endgame!
        Playing = False


def Dialoge():
    RoomNum = Room_Num("int")
    In_Room = room_ls[RoomNum]
    Dialoge = findline("Action_randlines.txt", str(
        level_Info[0])+str(random.randint(0, 5)))
    description = RoomDetails(RoomNum, level_Info[0])
    description = description
    if In_Room == []:
        description += "The room is empty."
    else:
        description += "in the room you see: "+str(In_Room)
    print ("He is in "+str(Position))
    print (description)
    sls()
    return (Dialoge)


def Action(input):
    keyword, point = input_breakdown(input)
    if Actions_ls.has_key(keyword):
        Callno = Actions_ls[keyword]
        CallActionModule(Callno, point)
    else:
        print (Ohelp)


while Playing:
    sls()
    Progress()
    input = raw_input("> "+str(Dialoge())+">> ")
    Action(input)
