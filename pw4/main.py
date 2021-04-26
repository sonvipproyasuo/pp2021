class information(Student):
son = information("Luong Nguyen Viet Son", "Bi10-156", "28/01/2001")
nam = information("Nguyen Hoang Nam", "BI10-123", "06/01/2001")

son.showinfo()
nam.showinfo()

class Course(Student):
python = Course("Luong Nguyen Viet Son","Advance Programming With Python ", "PYTHON","14.675",)

python.showinfo()
python.passornot()
