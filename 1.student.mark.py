
def studentcounting():
    count = int(input("The numbers of students:"))
    return count

def studentinformation():
    print("enter student info")
    name = input("name:")
    id = input("ID:")
    dob = input("dob:")
    s = {"name": name, "ID": id,"dob": dob }
    return s

def liststudent(student):
    for s in student:
        print(f" = id{s['id']}, name is {s['name']}, dob is{s['dob']}")

count = studentcounting()
for i in range(0,count):
    s = studentinformation()

def coursecounting():
    count = int(input("The numbers of courses:"))
    return count

def courseinformation():
    print("enter course info")
    coursename = input("coursename:")
    courseid = input("courseid:")
    a = {"coursename": coursename, "courseid": courseid}
    return a

def listcourse(course):
    for a in course:
        print(f" = courseid{s['course id']}, coursename is {s['course name']}")

count = coursecounting()
for i in range(0,count):
    a = courseinformation()




