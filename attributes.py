import math


# ? Attributes
# * Base SPECIAL System Attributes

class attributes:
    def __init__(self, Cstrength, Cperception, Cendurance, Ccharisma, Cintelligence, Cagility, Cluck):
        self.strength = Cstrength
        self.perception = Cperception
        self.endurance = Cendurance
        self.charisma = Ccharisma
        self.intelligence = Cintelligence
        self.agility = Cagility
        self.luck = Cluck
        self.hp = 25 + (2 * self.endurance) + self.strength
        self.maxhp = 25 + (2 * self.endurance) + self.strength
        self.ap = math.floor(self.agility/2) + 5
        self.maxap = math.floor(self.agility/2) + 5
        self.carryWeight = 25 + (self.strength*25)
        self.damageResistance = 0
        self.damageThreshhold = 0
        self.armorClass = self.agility
        self.meleeDamage = ({True: self.strength - 5,
                            False: 1}[self.strength > 5])
        self.sequence = 2 * self.perception
        self.healingRate = math.ceil(self.endurance/3)
        self.poisonResistance = 5 * self.endurance
        self.radiationResistance = 2 * self.endurance
        self.criticalChance = self.luck
        self.barter = 4 * self.charisma
        self.energyWeapons = 2 * self.agility
        self.explosives = 2 * self.perception
        self.guns = 2 * self.agility
        self.lockpick = 10 + self.perception + self.agility
        self.medicine = 2 * (self.perception + self.intelligence)
        self.meleeWeapons = 20 + (2 * (self.strength + self.agility))
        self.repair = 3 * self.intelligence
        self.science = 4 * self.intelligence
        self.sneak = 5 + (3 * self.agility)
        self.speech = 5 * self.charisma
        self.survival = 2 * (self.endurance + self.intelligence)
        self.unarmed = 25 + (2*(self.strength+self.agility))

    # ? Getters

    def GetStrength(self):
        return self.strength

    def GetPerception(self):
        return self.perception

    def GetEndurance(self):
        return self.endurance

    def GetCharisma(self):
        return self.charisma

    def GetIntelligence(self):
        return self.intelligence

    def GetAgility(self):
        return self.agility

    def GetLuck(self):
        return self.luck

    def GetHP(self):
        return self.hp

    def GetMaxHP(self):
        return self.maxhp

    def GetAP(self):
        return self.ap

    def GetMaxAP(self):
        return self.maxap

    def GetCarryWeight(self):
        return self.carryWeight

    def GetDamageResistance(self):
        return self.damageResistance

    def GetDamageThreshhold(self):
        return self.damageThreshhold

    def GetArmorClass(self):
        return self.armorClass

    def GetMeleeDamage(self):
        return self.meleeDamage

    def GetSequence(self):
        return self.sequence

    def GetHealingRate(self):
        return self.healingRate

    def GetPoisonResistance(self):
        return self.poisonResistance

    def GetRadiationResistance(self):
        return self.radiationResistance

    def GetCriticalChance(self):
        return self.criticalChance

    def GetBarter(self):
        return self.barter

    def GetEnergyWeapons(self):
        return self.energyWeapons

    def GetExplosives(self):
        return self.explosives

    def GetGuns(self):
        return self.guns

    def GetLockpick(self):
        return self.lockpick

    def GetMedicine(self):
        return self.medicine

    def GetMeleeWeapons(self):
        return self.meleeWeapons

    def GetRepair(self):
        return self.repair

    def GetScience(self):
        return self.science

    def GetSneak(self):
        return self.sneak

    def GetSpeech(self):
        return self.speech

    def GetSurival(self):
        return self.survival

    def GetUnarmed(self):
        return self.unarmed
    # ? Setters

    def SetStrength(self, newStrength):
        self.strength = newStrength

    def SetPerception(self, newPerception):
        self.perception = newPerception

    def SetEndurance(self, newEndurance):
        self.endurance = newEndurance

    def SetCharisma(self, newCharisma):
        self.charisma = newCharisma

    def SetIntelligence(self, newIntelligence):
        self.intelligence = newIntelligence

    def SetAgility(self, newAgility):
        self.agility = newAgility

    def SetLuck(self, newLuck):
        self.luck = newLuck

    def SetHP(self, newHP):
        self.hp = newHP

    def SetAP(self, newAP):
        self.ap = newAP

    def SetCarryWeight(self, newCarryWeight):
        self.carryWeight = newCarryWeight

    def SetDamageResistance(self, newDamageResistance):
        self.damageResistance = newDamageResistance

    def SetDamageThreshhold(self, newDamageThreshhold):
        self.damageThreshhold = newDamageThreshhold

    def SetArmorClass(self, newArmorClass):
        self.armorClass = newArmorClass

    def SetMeleeDamage(self, newMeleeDamage):
        self.meleeDamage = newMeleeDamage

    def SetSequence(self, newSequence):
        self.sequence = newSequence

    def SetHealingRate(self, newHealingRate):
        self.healingRate = newHealingRate

    def SetPoisonResistance(self, newPoisonResistance):
        self.poisonResistance = newPoisonResistance

    def SetRadiationResistance(self, newRadiationResistance):
        self.radiationResistance = newRadiationResistance

    def SetCriticalChance(self, newCriticalChance):
        self.criticalChance = newCriticalChance

    def SetBarter(self, newBarter):
        self.barter = newBarter

    def SetEnergyWeapons(self, newEnergyWeapons):
        self.energyWeapons = newEnergyWeapons

    def SetExplosives(self, newExplosives):
        self.explosives = newExplosives

    def SetGuns(self, newGuns):
        self.guns = newGuns

    def SetLockpick(self, newLockpick):
        self.lockpick = newLockpick

    def SetMedicine(self, newMedicine):
        self.medicine = newMedicine

    def SetMeleeWeapons(self, newMeleeWeapons):
        self.meleeWeapons = newMeleeWeapons

    def SetRepair(self, newRepair):
        self.repair = newRepair

    def SetScience(self, newScience):
        self.science = newScience

    def SetSneak(self, newSneak):
        self.sneak = newSneak

    def SetSpeech(self, newSpeech):
        self.speech = newSpeech

    def SetSurvival(self, newSurvival):
        self.survival = newSurvival

    def SetUnarmed(self, newUnarmed):
        self.survival = newUnarmed
