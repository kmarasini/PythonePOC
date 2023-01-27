class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def dispalyCount(self):
        Employee.empCount

    def displayEmployee(self):
        print("Name : ", self.name, " Salary: ", self.salary)
    
emp1 = Employee("Ram", 2000)
emp1.dispalyCount
emp2 = Employee("Hari", 5000)
emp2.dispalyCount
emp1.displayEmployee()
emp2.displayEmployee()
print("Ttotal Emp for empcount: %d" % Employee.empCount)

