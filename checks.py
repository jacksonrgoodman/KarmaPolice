def StrengthCheck(character, number):
    strength = character.GetStrength()
    if strength >= number:
        return True
    elif strength < number:
        return False


def PerceptionCheck(character, number):
    perception = character.GetPerception()
    if perception >= number:
        return True
    elif perception < number:
        return False


def EnduranceCheck(character, number):
    endurance = character.GetEndurance()
    if endurance >= number:
        return True
    elif endurance < number:
        return False


def CharismaCheck(character, number):
    charisma = character.GetCharisma()
    if charisma >= number:
        return True
    elif charisma < number:
        return False


def IntelligenceCheck(character, number):
    intelligence = character.GetIntelligence()
    if intelligence >= number:
        return True
    elif intelligence < number:
        return False


def AgilityCheck(character, number):
    agility = character.GetAgility()
    if agility >= number:
        return True
    elif agility < number:
        return False


def LuckCheck(character, number):
    luck = character.GetLuck()
    if luck >= number:
        return True
    elif luck < number:
        return False
# ? gender tools


def genderCheck1(character):
    gender = character.GetGender()
    if gender == 1:
        return "male"
    elif gender == 2:
        return "female"
    else:
        return "non-binary"


def genderCheck2(character):
    gender = character.GetGender()
    if gender == 1:
        return "masculine"
    elif gender == 2:
        return "feminine"
    else:
        return "ambiguous"


def genderCheck2(character):
    gender = character.GetGender()
    if gender == 1:
        return "he"
    elif gender == 2:
        return "she"
    else:
        return "they"


def genderCheck3(character):
    gender = character.GetGender()
    if gender == 1:
        return "him"
    elif gender == 2:
        return "her"
    else:
        return "them"


def genderCheck4(character):
    gender = character.GetGender()
    if gender == 1:
        return "his"
    elif gender == 2:
        return "her"
    else:
        return "their"


def genderCheck5(character):
    gender = character.GetGender()
    if gender == 1:
        return "his"
    elif gender == 2:
        return "hers"
    else:
        return "theirs"


def genderCheck6(character):
    gender = character.GetGender()
    if gender == 1:
        return "himself"
    elif gender == 2:
        return "herself"
    else:
        return "themself"
