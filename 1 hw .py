class Phone:
    name = "Iphone"
    marka = 13
    tcena = 85000

    def getname(self):
        return self.name

    def getmarka(self):
        return self.marka

    def gettcena(self):
        return self.tcena

    def settcena(self, tcena):
        self.tcena = tcena

    def setmarka(self, marka):
        self.marka = marka

    def setname(self, name):
        self.name = name


phone1 = Phone()
print(phone1.getname())
print(phone1.getmarka())
print(phone1.gettcena())
phone2 = Phone()
phone2.settcena(96000)
print(phone2.gettcena())
phone2.setmarka(14)
print(phone2.getmarka())
phone2.setname("Iphone x")
print(phone2.getname())
