class Person:
    std="sixth"

    def __init__(self,name,school):
        self.name=name
        self.std = school
    def showdeatils(self):
        return f"My name is {self.name} and I`m Studying in {self.std}"
boy1=Person("Mukesh","makerere university")
print(boy1.showdeatils())
