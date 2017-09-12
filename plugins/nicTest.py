def nicotine(text):
    """nicotine <nic base strength (mg/ml)> <Batch size (ml)> <finished strength (mg/ml)>"""
    query = text.split(" ")

    if len(query) != 3:
        print("Incorrect args: Enter <nic base strength (mg/ml)> <Batch size (ml)> <finished strength (mg/ml)>")
        return

    if query[0].lower().endswith("mg"):
        query[0] = query[0][:-2]
    try:
        nicIn = float(query[0])
    except Exception:
        print("Incorrect args: Enter <nic base strength (mg/ml)> <Batch size (ml)> <finished strength (mg/ml)>")
        return



    if query[1].lower().endswith("ml"):
        query[1] = query[1][:-2]
    try:
        batch = float(query[1])
    except Exception:
        print("Incorrect args: Enter <nic base strength (mg/ml)> <Batch size (ml)> <finished strength (mg/ml)>")
        return

    if query[2].lower().endswith("mg"):
        query[2] = query[2][:-2]
    try:
        nicOut = float(query[2])
    except Exception:
        print("Incorrect args: Enter <nic base strength (mg/ml)> <Batch size (ml)> <finished strength (mg/ml)>")
        return

    if nicIn < nicOut:
        print("Cannot make {:g}mg with {:g}mg base".format(nicOut, nicIn).rstrip('0').rstrip('.'))
        return

    nicNeeded = nicOut*batch
    nicVolume = nicNeeded/nicIn

    print("For {:g}ml of {:g}mg liquid you will need {:g}ml of {:g}mg base".format(batch, nicOut, nicVolume, nicIn).rstrip('0').rstrip('.'))
    return



nicotine("18 60 3")
nicotine("18mg 60ml 3mg")
nicotine("72 100 3")
nicotine("why would you")
nicotine("18sdf")
nicotine("")
nicotine(" ")
nicotine("! ! !")
nicotine("1 100 10")
nicotine("10.1 50.f 60")
