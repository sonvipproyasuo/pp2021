from Student import Student
class information(Student):
    def __init__(self, name, id, dob):
        super().__init__(name)
        self.id = id
        self.dob = dob

    def showinfo(self):
        print("Name:" + self.name)
        print("Id:" + self.id)
        print("Dob:" + self.dob)


son = information("Luong Nguyen Viet Son", "Bi10-156", "28/01/2001")
nam = information("Nguyen Hoang Nam", "BI10-123", "06/01/2001")

son.showinfo()
nam.showinfo()