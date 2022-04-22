from tonleiter import tonleiter, vorzeichen
from dreiklang import dreiklang
from kadenz import kadenz, einfache_kadenz

def help():
    print("hilfe/h/help  |  Gibt diese Nachricht aus")
    print("tonleiter/tl <name>  |  Gibt die Tonleiter aus")
    print("vorzeichen/vz <tonleitername>  |  Gibt die Vorzeichen der Tonleiter aus")
    print("dreiklang/dk <tonleitername> [<stufe>] [<dreiklangtyp>]  |  Gibt den Dreiklang der Tonleiter auf der ersten oder angegebenen Stufe in der Quintlage/Grundstellung oder im angegebenen Typ aus")

def main():
    inp = input(">").lower()
    if inp in ["help", "h", "hilfe"]:
        help()
    elif inp.split(" ")[0] in ["tonleiter", "tl"]:
        x = tonleiter(inp.replace(inp.split(" ")[0] + " ", ""))
        if x is not None:
            print(", ".join(x))
        else:
            print("Diese Tonleiter gibt es nicht.")
    elif inp.split(" ")[0] in ["vorzeichen", "vz"]:
        x = vorzeichen(inp.replace(inp.split(" ")[0] + " ", ""))
        if x not in [None, []]:
            print(", ".join(x))
        elif x == []:
            print("Diese Tonleiter hat keine Vorzeichen.")
        else:
            print("Diese Tonleiter gibt es nicht.")
    else:
        print("Das ist kein verfügbarer Befehl. Tippe 'hilfe' für Hilfe.")

    main()

main()
