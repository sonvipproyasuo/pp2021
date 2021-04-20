class Student:
 def countstudent(self):
     count = int(input("Number of students in this class:"))
     print("Number of students:" + count)
     return count

 def __init__(self, name):
     self.name = name

 def showInfo(self):
     print("This is" + self.name)





