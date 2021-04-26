class information(Student):
    def showinfo(self):
        print("Name:" + self.name)
        print("Id:" + self.id)
        print("Dob:" + self.dob)
        
class Course(Student):
    def showinfo(self):
       print( self.name +"'s course is " + self.coursename + ", whose id is " + self.courseid)

    def passornot(self):
        if self.coursescore < self.passcore:
            print("this student fails " + self.coursename + "with the final score is ", end="")
            print(round(self.coursescore, 1))
        else:
            print("this student passes " + self.coursename + "with the final score is ", end="")
            print(round(self.coursescore, 1))
