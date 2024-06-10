class PersonalClass:

    name = ""
    idno = ""
    vehicletype = ""
    credit = ""
    carextras = ""

    def __init__(self, name, idno, vehicletype, carextras, credit):
        self.name = name
        self.idno = idno
        self.vehicletype = vehicletype
        self.credit = credit
        self.carextras = carextras

    # helper
    def hasCreditScore(self):

        if self.credit == "Yes":
            return "Qualified"
        else:
            return "Not Qualified"

    #setters

    # def setName(self, name):
    #     self.name = name
    #
    # def setID(self, idno):
    #     self.idno = idno
    #
    # def setVehicleType(self, vehicletype):
    #     self.vehicletype = vehicletype
    #
    # def setCredit(self, credit):
    #     self.credit = credit
    #
    # def setExtr(self, carextras):
    #     self.carextras = carextras

    #getters
    def getName(self):
        return self.name

    def getID(self):
        return self.idno

    def getVehicleType(self):
        return self.vehicletype

    def getExtr(self):
        return self.carextras

    #ToString
    def __str__(self):
        return self.name + "#" + self.idno + "#" + self.vehicletype + "#"+self.carextras
