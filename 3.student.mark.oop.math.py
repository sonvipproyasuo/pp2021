import numpy
from array import *
class Student:
 def countstudent(self):
     count = int(input("Number of students in this class"))
     for i in range(0,count):
         print("Number of students:" + count)
         return count

 def __init__(self,name):
     self.name =name

 def showinfo(self):
     print("This is" +self.name)

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
            print("this student fails " + self.coursename + "with the final score is ", end="")
            print(round(self.coursescore, 1))
        else:
            print("this student passes " + self.coursename + "with the final score is ", end="")
            print(round(self.coursescore, 1))

from Student import Student
class GPA(Student):
    def __init__(self, name):
        super().__init__(name)

    def calculategpa(self):
        a = array('i', [])
        n = int(input("Enter the number of score list of "  +self.name))
        for i in range (n):
            x = int(input("Enter the next score"))
            a.append(x)

        gpa = str(numpy.mean(a))
        print(self.name + "'s GPA is " + gpa)




