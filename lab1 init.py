class Phone:
    def __init__(self, name, marka, tcena):
        self.name = name
        self.marka = marka
        self.tcena = tcena

    def display_info(self):
        print("\ntelephone:", self.name, " \n marka :", self.marka, "\n tcena :", self.tcena)

    def getmarka(self):
        return self.marka

    def settcena(self, tcena):
        self.tcena = tcena

    def gettcena(self):
        return self.tcena


phone1 = Phone("iphone", 14, 89000)
phone1.display_info()
print("marka", phone1.getmarka())
phone1.settcena(97000)
print("changed tcena", phone1.gettcena())
