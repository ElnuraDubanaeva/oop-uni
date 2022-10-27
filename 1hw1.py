class Phone:
    def __init__(self, name, marka, tcena, year):
        self.name = name
        self.marka = marka
        self.tcena = tcena
        self.year = year

    def display_info(self):
        print("\ndevice:", self.name, "\nmarka:", self.marka, "\ntcena:", self.tcena, '\nyear:', self.year)

    def setmarka(self, marka):
        self.marka = marka

    def getmarka(self):
        return self.marka

    def settcena(self, tcena):
        self.tcena = tcena

    def gettcena(self):
        return self.tcena


phone1 = Phone("iphone", 14, 89000, '2014 year')
phone1.display_info()
phone1.setmarka('14 pro')
print("marka", phone1.getmarka())
phone1.settcena(97000)
print("changed tcena:", phone1.gettcena())
