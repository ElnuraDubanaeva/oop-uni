class Device:
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


class Payment():
    def __init__(self, month, installment):
        self.month = month
        self.installment = installment

    def count(self):
        if self.installment == "Yes":
            count = self.tcena / self.month
            print(f"Payment:{count} \n{self.month} month")
        else:
            print("Payment:", self.tcena)


class Phone(Device):
    pass


phone1 = Phone("iphone", 14, 89000, '2014 year')
phone1.display_info()
phone1.setmarka('14 pro')
print("marka", phone1.getmarka())
phone1.settcena(97000)
print("changed tcena:", phone1.gettcena())


class laptop(Device, Payment):
    def __init__(self, name, marka, tcena, year, month, installment):
        Device.__init__(self, name, marka, tcena, year)
        Payment.__init__(self, month, installment)

    pass


laptop1 = laptop('lenovo', '7th Gen', 25000, '2015 year', 8, "no")
laptop2 = laptop('lenovo', '7th Gen', 25000, '2015 year', 8, "Yes")
laptop1.display_info()
laptop1.count()
laptop1.setmarka('8 th Gen')
print('marka:', laptop1.getmarka())
laptop1.settcena(30000)
print("changed tcena:", laptop1.gettcena())

laptop2.display_info()
laptop2.count()
laptop2.setmarka('8 th Gen')
print('marka:', laptop2.getmarka())
laptop2.settcena(30000)
print("changed tcena:", laptop2.gettcena())
