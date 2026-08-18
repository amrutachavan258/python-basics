class employee:
    name=" "
    eid=0
    desig=" "
    salary=0.0
    DA=0.0
    HRA=0.0
    gross_Salary=0.0

    def accept(self):
        self.name=input("Enter name of Employee: ")
        self.eid=int(input("Enter employee ID: "))
        self.desig=input("Enter designation of Employee: ")
        self.salary=int(input("Enter salary of Employee: "))

    def cal_salary(self):
        self.DA=self.salary*0.10
        self.HRA=self.salary*0.20
        self.gross_salary=self.DA+self.HRA+self.salary

    def display(self):
        print("Name: ",self.name)
        print("ID: ",self.eid)
        print("Designation: ",self.desig)
        print("Gross Salary: ",self.gross_salary)

e1=employee()
e2=employee()

print("Enter details for first employee: ")
e1.accept()
print("Enter details for second employee: ")
e2.accept()

e1.cal_salary()
e2.cal_salary()

e1.display()
e2.display()
