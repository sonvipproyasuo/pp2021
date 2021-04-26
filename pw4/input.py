class information(Student):
    def __init__(self, name, id, dob):
        super().__init__(name)
        self.id = id
        self.dob = dob
        self.studentlist = []

    def showinfo(self):
        print("Name:" + self.name)
        print("Id:" + self.id)
        print("Dob:" + self.dob)

    def inputStudent(self, name, id, dob):
        student = input(name, id, dob)
        self.studentlist.append(student)
