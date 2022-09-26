class Person:
    name = 'Elnura'
    age = 18

    def display_info(self):
        print ("My name is ", self.name)
        print ("age:", self.age)
    def getname(self):
        return self.name
    def setname(self,name):
        self.name = name 

person1 =Person()
person1.display_info() 
person1.name = "Asan"
person1.display_info() 
person2 = Person()
person2.name = "Bolot"
person2.display_info()
person2.setname("Alex")
person2.display_info()
print (person2.getname())
