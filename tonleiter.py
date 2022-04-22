muster_dur = [2, 2, 1, 2, 2, 2, 1]
muster_moll = [2, 1, 2, 2, 1, 2, 2]
muster_moll_harmonisch = [2, 1, 2, 2, 1, 3, 1]
muster_moll_melodisch = [2, 1, 2, 2, 2, 2, 1]
toene = ["c", "", "d", "", "e", "f", "", "g", "", "a", "", "h"]

def tonleiter(name):
    name = name.lower()
    grundton = name.split(" ")[0]
    art = name.replace(grundton + " ", "")
    if art == "dur":
        muster =  muster_dur
    elif art == "moll":
        muster =  muster_moll
    elif art == "moll harmonisch":
        muster =  muster_moll_harmonisch
    elif art == "moll melodisch":
        muster = muster_moll_melodisch
    else:
        return None

    grundton = grundton.lower()
    tonleiter = [grundton]
    if "i" in grundton:
        vor = grundton.count("s")
        grundton = grundton.replace("is", "")
    elif "es" in grundton and not grundton.startswith("e"):
        vor = -grundton.count("s")
        grundton = grundton.replace("es", "")
    elif "es" in grundton:
        vor = -grundton.count("s")
        grundton = "e"
    elif grundton == "b":
        vor = -1
        grundton = "h"
    else:
        vor = 0

    ton = grundton

    for i in muster:
        s = toene.index(ton)
        nton = toene[(s + 1) % 12] if toene[(s + 1) % 12] != "" else toene[(s + 2) % 12]
        ton = nton

        if toene[(s + 1) % 12] == "":
            if i == 1:
                vor -= 1
        else:
            if i == 2:
                vor += 1

        if vor > 0:
            nton += "".join(["is" for i in range(vor)])
        elif vor < 0:
            if nton in "ea":
                nton += "s" + "".join(["es" for i in range((-vor) - 1)])
            elif nton == "h" and vor == -1:
                nton = "b"
            else:
                nton += "".join(["es" for i in range((-vor))])

        tonleiter.append(nton)

    return tonleiter

def vorzeichen(tonleitername):
    tl = tonleiter(tonleiter)
    vz = []
    for i in tl:
        if i not in toene:
            vz.append(i)

    return vz
