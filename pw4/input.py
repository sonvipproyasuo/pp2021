class information(Student):
    def __init__(self, name, id, dob):
        super().__init__(name)
        self.id = id
        self.dob = dob
        self.studentlist = []

    def inputStudent(self, name, id, dob):
        student = input(name, id, dob)
        self.studentlist.append(student)

class Course(Student):
    def __init__ (self,name, coursename, courseid, coursescore):
        super().__init__(name)
        self.coursename = coursename
        self.courseid = courseid
        self.coursescore = float(coursescore)
        self.passcore = 10
        self.courselist = []
        
    def inputCourse(self, coursename, courseid, coursescore):
        course = input(coursename,courseid, coursescore)
        self.courselist.append(course)
