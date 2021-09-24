import checks
import faces


def bottomBar():
    print("╭――――――――――――――――――――――――――――――――――――――――――――╮")
    print("│                                            │")
    print("╰――――――――――――――――――――――――――――――――――――――――――――╯")


def image(actor):
    if actor.GetGender() == 1:
        print()
        faces.oldman1()
        bottomBar()
    if actor.GetGender() == 2:
        print()
        print("            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⠚⢉⣩⣭⡭⠛⠓⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀           ")
        print("            ⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀            ")
        print("            ⠀⠀⠀⠀⢀⡴⠃⢀⡴⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀            ")
        print("            ⠀⠀⠀⠀⡾⠁⣠⠋⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀            ")
        print("            ⠀⠀⠀⣸⠁⢰⠃⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀            ")
        print("            ⠀⠀⠀⡇⠀⡾⡀⠀⠀⠀⠀⣀⣹⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀            ")
        print("            ⠀⠀⢸⠀⢻⡟⡻⢶⡆⠀⠀⠀⠀⡼⠟⡳⢿⣦⡑⢄⠀⠀⠀⠀⠀⠀⠀⢸⡇            ")
        print("            ⠀⠀⣸⠀⢸⠃⡇⢀⠇⠀⠀⠀⠀⠀⡼⠀⠀⠈⣿⡗⠂⠀⠀⠀⠀⠀⠀⠀⢸⠁           ")
        print("            ⠀⠀⡏⠀⣼⠀⢳⠊⠀⠀⠀⠀⠀⠀⠱⣀⣀⠔⣸⠁⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀           ")
        print("            ⠀⠀⡇⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀            ")
        print("            ⠀⢸⠃⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⢀⠀⠀⠀⠀⠀⣾⠀⠀            ")
        print("            ⠀⣸⠀⠀⠹⡄⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠸⠀⠀⠀⠀⠀⡇⠀⠀            ")
        print("            ⠀⡏⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⢀⣠⢶⡇⠀⠀⢰⡀⠀⠀⠀⠀⠀⡇⠀⠀            ")
        print("            ⢰⠇⡄⠀⠀⠀⡿⢣⣀⣀⣀⡤⠴⡞⠉⠀⢸⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣧⠀⠀           ")
        print("            ⣸⠀⡇⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢹⠀⠀⢸⠀⠀⢀⣿⠇⠀⠀⠀⠁⠀  ⢸⠀⠀          ")
        print("            ⣿⠀⡇⠀⠀⠀⠀⠀⢀⡤⠤⠶⠶⠾⠤⠄⢸⠀⡀⠸⣿⣀⠀⠀⠀⠀ ⠀⠈⣇⠀         ")
        print("            ⡇⠀⡇⠀⠀⡀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠸⡌⣵⡀⢳⡇⠀⠀⠀⠀   ⠀⠀⢹⡀        ")
        print("╭―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――╮")
        print("│                                                           │")
        print("╰―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――╯")
    if actor.GetGender() == 3:
        print("╭――――――――――――――――――╮")
        print("│                  │")
        print("│                  │")
        print("│                  │")
        print("│                  │")
        print("│      Person      │")
        print("│                  │")
        print("│                  │")
        print("│                  │")
        print("│                  │")
        print("╰――――――――――――――――――╯")


def titleCard(actor):
    image(actor)
    print("Name: "+actor.GetName())


def dialogueCard(actor):
    image(actor)
    print(actor.GetName()+": ", sep="")


def detailCard(actor):
    titleCard(actor)
    print("Gender: "+checks.genderCheck1(actor).capitalize())
    print("Age: "+str(actor.GetAge()))


def playerCard(actor):
    detailCard(actor)
    print("HP: "+str(actor.GetHP())+"/"+str(actor.GetMaxHP()))
    print("AP: "+str(actor.GetAP())+"/"+str(actor.GetMaxAP()))
    print()
    print("S.P.E.C.I.A.L. STATS:")
    print("STR: "+str(actor.GetStrength()))
    print("PER: "+str(actor.GetPerception()))
    print("END: "+str(actor.GetEndurance()))
    print("CHA: "+str(actor.GetCharisma()))
    print("INT: "+str(actor.GetIntelligence()))
    print("AGI: "+str(actor.GetAgility()))
    print("LUC: "+str(actor.GetLuck()))
    print()
