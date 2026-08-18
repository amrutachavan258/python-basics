class student:
    name=" "
    roll_no=0
    sub1=0
    sub2=0
    total=0

    def accept_value(self):
        self.name=input("Enter name of student: ")
        self.roll_no=int(input("Enter roll num of student: "))
        self.sub1=int(input("Enter marks for first subject: "))
        self.sub2=int(input("Enter marks for second subject: "))

    def cal_total(self):
        self.total=self.sub1+self.sub2

    def display(self):
        print("Name: ",self.name)
        print("Roll Number: ",self.roll_no)
        print("Total: ",self.total)

s1=student()
s2=student()

print("Enter details for first student: ")
s1.accept_value()
print("Enter details for second student: ")
s2.accept_value()

s1.cal_total()
s2.cal_total()

s1.display()
s2.display()
