# ? Player Character
import attributes


class pc(attributes.attributes):
    def __init__(self, Cstrength, Cperception, Cendurance, Ccharisma, Cintelligence, Cagility, Cluck, CPCFirstName, CPCLastName, CPCGender, CPCPhysique, CPCAge, CPCDescription):
        super().__init__(Cstrength, Cperception, Cendurance,
                         Ccharisma, Cintelligence, Cagility, Cluck)

        self.firstName = CPCFirstName
        self.lastName = CPCLastName
        self.gender = CPCGender
        self.physique = CPCPhysique
        self.age = CPCAge
        self.description = CPCDescription

    # ? Getters

    def GetName(self):
        return self.firstName + " " + self.lastName

    def GetFirstName(self):
        return self.firstName

    def GetLastName(self):
        return self.lastName

    def GetGender(self):
        return self.gender

    def GetAge(self):
        return self.age

    def GetDescritpion(self):
        return self.description

    # ? Setters

    def SetFirstName(self, newFirstName):
        self.firstName = newFirstName

    def SetLastName(self, newLastName):
        self.lastName = newLastName

    def SetGender(self, newGender):
        self.gender = newGender

    def SetAge(self, newAge):
        self.age = newAge

    def SetDescritpion(self, newDescription):
        self.description = newDescription
