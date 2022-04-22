from tonleiter import tonleiter


def dreiklang(tonleitername, stufe=None, dreiklangtyp=None):
    if stufe is None:
        stufe = 1
    if dreiklanglage is None:
        dreiklanglage = "quintlage"
    dreiklanglage = dreiklanglage.lower()
    stufe -= 1
    tl = tonleiter(dreiklangname)
    if tl is None:
        return None

    if dreiklangtyp in ["quintlage", "grundstellung"]:
        dreiklang = [tl[i] for i in [stufe % 8, (2 + stufe) % 8, (4 + stufe) % 8]]
    elif dreiklangtyp in ["oktavlage", "sextakkord"]:
        dreiklang = [tl[i] for i in [(2 + stufe) % 8, (4 + stufe) % 8], stufe % 8]
    elif dreiklangtyp in ["terzlage", "quartsextakkord"]:
        dreiklang = [tl[i] for i in [(4 + stufe) % 8], stufe % 8, (2 + stufe) % 8]
    else:
        return None

    return dreiklang
