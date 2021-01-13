def likely_reference(skit):
    if skit == "Dead Parrot":
        print("stiff")
    elif skit == "Hungarian Phrasebook":
        print("eels")
    elif skit == "Lumberjack":
        if len(skit) < 3:
            print("sleeps all day")
        else:
            print("i'm okay")
    else:
        print("ni" * len(skit))
