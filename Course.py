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