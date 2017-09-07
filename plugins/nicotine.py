from cloudbot import hook


@hook.command("nicotine", "nic")
def nicotine(text):
    """nicotine <nic base strength (mg/ml)> <Batch size (ml)> <finished strength (mg/ml)>"""
    query = text.split(" ")

    if len(query) != 3:
        return "Incorrect args: Enter <nic base strength (mg/ml)> <Batch size (ml)> <finished strength (mg/ml)>"

    if query[0].lower.endswith("mg"):
        query[0] = query[0][:-2]
    nicIn = float(query[0])



    if query[1].lower.endswith("ml"):
        query[1] = query[1][:-2]
    batch = float(query[1])

    if query[2].lower.endswith("mg"):
        query[2] = query[2][:-2]
    nicOut = float(query[2])

    if nicIn < nicOut:
        return "Cannot make {0:.2f}mg with {0:.2f}mg base".format(nicOut, nicIn).rstrip('0').rstrip('.')

    nicNeeded = nicOut*batch
    nicVolume = nicNeeded/nicIn

    return "For {0:.2f}ml of {0:.2f}mg liquid you will need {0:.2f}ml of {0:.2f}mg base".format(batch, nicOut, nicVolume, nicIn).rstrip('0').rstrip('.')




