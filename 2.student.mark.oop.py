
class Student:
 def countstudent(self):
     count = int(input("Number of students in this class:"))
     print("Number of students:" + count)
     return count

 def __init__(self, name):
     self.name = name

 def showInfo(self):
     print("This is" + self.name)

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

from Student import Student
class Course(Student):
    def __init__ (self,name, coursename, courseid, coursescore):
        super().__init__(name)
        self.coursename = coursename
        self.courseid = courseid
        self.coursescore = int(coursescore)
        self.passcore = 10

    def showinfo(self):
       print( self.name +"'s course is " + self.coursename + ", whose id is " + self.courseid)

    def passornot(self):
        if self.coursescore < self.passcore:
            print("this student fails " + self.coursename + "with the final score is " +str(self.coursescore) )
        else:
            print("this student passes " + self.coursename + "with the final score is " +str(self.coursescore))
son = Course("Luong Nguyen Viet Son","Advance Programming With Python ", "PYTHON","15")
son.showinfo()
son.passornot()
