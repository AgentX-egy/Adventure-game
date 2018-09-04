from Progress_Modules import *

Actions_ls = {"Move": 0, "Drop": 1, "Pickup": 2, "Think!": 3}
room_ls = ([], [], ["Red key"], [], [], [], [], [], [])
invertory = []  # remember to capitalize
Position = [0, 0]  # RELEASE MODE:[0,0]
level_Info = [-1, True]  # RELEASE MODE:[-1, True]
# DEBUG   MODE:[x-level,False] where x>-1


def input_breakdown(given):
    try:
        x, y = str(given).split(" ", 1)
        return str(x).capitalize(), str(y).capitalize()
    except ValueError:
        return str(given).capitalize(), 0


def CallActionModule(callno, point):
    if callno == 0:
        Move(point)
    if callno == 1:
        Drop(point)
    if callno == 2:
        Pickup(point)
    if callno == 3:
        Think()


def Move(Direction):
    WLD = checkWLD(Direction)
    if WLD is -1:
        print ('> "door is locked.."')
    elif Direction == "North":
        try:
            if (Position[1] + 1 > 2) | WLD:
                raise Exception
        except Exception:
            print ('> "Blocked"')
        else:
            Position[1] += 1
    elif Direction == "South":
        try:
            if (Position[1]-1 < 0) | WLD:
                raise Exception
        except Exception:
            print ('> "Blocked"')
        else:
            Position[1] -= 1
    elif Direction == "East":
        try:
            if (Position[0]+1 > 2) | WLD:
                raise Exception
        except Exception:
            print ('> "Blocked"')
        else:
            Position[0] += 1
    elif Direction == "West":
        try:
            if (Position[0]-1 < 0) | WLD:
                raise Exception
        except Exception:
            print ('> "Blocked"')
        else:
            Position[0] -= 1


def checkWLD(Direction):
    '''Checks Walls and Locked Doors'''
    RoomNum = Room_Num("int")
    # Locked Doors
    if level_Info[0] == 0:
        if (RoomNum == 1) & (Direction == "North"):
            return -1
    if level_Info[0] == 1:
        if (RoomNum == 4) & (Direction == "East"):
            return -1
        elif (RoomNum == 7) & (Direction == "East"):
            return -1
    # Walls
    if RoomNum == 0:
        if Direction == "North":
            return True
    if RoomNum == 2:
        if Direction == "North":
            return True
    if RoomNum == 3:
        if Direction == "South":
            return True
        elif Direction == "East":
            return True
    if RoomNum == 4:
        if Direction == "West":
            return True
    if RoomNum == 5:
        if Direction == "South":
            return True

    return False


def Room_Num(mode):
    value = 3*Position[1]+Position[0]
    if mode == "str":
        return str(value)
    if mode == "int":
        return int(value)


def Drop(Item):
    try:
        From = invertory.index(Item)
    except ValueError:
        randline = findline("Drop_randlines.txt", str((random.randint(1, 7))))
        print "> "+(randline)
    else:
        room_ls[Room_Num("int")].append(invertory.pop(From))


def Pickup(Item):
    try:
        Take = room_ls[Room_Num("int")].index(Item)
        if len(invertory) == 3:
            raise Exception
    except ValueError:
        randline = findline("Pickup_randlines.txt",
                            str((random.randint(1, 7))))
        print "> "+(randline)
    except Exception:
        print ("Can't carry more stuff")
    else:
        del room_ls[Room_Num("int")][Take]
        invertory.append(Item)


def Think():
    if invertory != []:
        print ('> "Invertory: '+str(invertory)+'"')
    if level_Info[0] == 0:
        level_Info[1] = level0(Room_Num("int"), invertory)
    if level_Info[0] == 1:
        level_Info[1] = level1(Room_Num("int"))

# raw_input() #UNCOMMENT TO DEBUG
