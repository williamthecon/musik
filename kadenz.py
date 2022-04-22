from tonleiter import tonleiter
from dreiklang import dreiklang


def einfache_kadenz(tonleitername, stufen, dreiklanglage=None):
    if dreiklanglage is None:
        dreiklanglage = "quintlage"
    dreiklanglage = dreiklanglage.lower()
    tl = tonleiter(tonleitername)
    if tl is None:
        return None

    kadenz = []

    for s in stufen:
        kadenz.append(dreiklang(tonleitername, s, dreiklanglage))

    return kadenz

# Kadenz
# Startakkord -> nächster Akkord in der Stellung die am nächsten dran ist (wenn kein gleicher Ton -> Gegenbewegung)
#
#
#
#
#
#

def kadenz(tonleitername, stufen, dreiklanglage):
    if dreiklanglage is None:
        dreiklanglage = "quintlage"
    dreiklanglage = dreiklanglage.lower()
    tl = tonleiter(tonleitername)
    if tl is None:
        return None

    kadenz = []

    for s in stufen:
        if kadenz == []:
            kadenz.append(dreiklang(tonleitername, s, dreiklanglage))
        else:
            akkorde = [dreiklang(tonleitername, s, l) for l in ["quintlage", "oktavlage", "terzlage"]]
            for akkord in akkorde:
                gleiche = False
                for a in akkord:
                    if a in kadenz[-1]:
                        gleiche = True

                if not gleiche:
                    pass

    return kadenz
