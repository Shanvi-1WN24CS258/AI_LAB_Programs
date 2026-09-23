rooms={
    "A":"DIRTY",
    "B":"CLEAN"
}

current_room="A"
for step in range(4):
    print("current room:",current_room)
    print("condition:",rooms[current_room])

    if rooms[current_room]=="DIRTY":
        print("ACTION:SUCK")
        rooms[current_room]="CLEAN"

    else:
        print("ACTION:MOVE")
        if current_room=="A":
            current_room="B"
        else:
            current_room="A"

    print()