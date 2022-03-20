

from traceback import print_tb


class Employee:
    increment = 1.5
    no_of_employee = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary =  salary
        Employee.no_of_employee = Employee.no_of_employee +1
    def increase(self):
        self.salary = self.salary * Employee.increment
        
        
    
    @classmethod
    def change_increment(cls,persentage):
        cls.increment = persentage

    @classmethod
    def for_str(cls,str):
        name,salary = str.split("-")
        return cls(name,salary)
    
    @staticmethod
    def isOpen(day):
        if day== "sunday":
            return False
        else:
            return True
        
    pass

# class Progammer(Employee):
#     def __init__(self, n, s, langwage,exp):
#         super().__init__(n,s)
#         self.langwage = langwage
#         self.exp = exp
        
#         def increase(self):
#             self.salary = int(self.salary) + int(self.salary) *int(self.increment)
        
  
        
        
        
        
        
        
        
# print("number of employee is :- ",Employee.no_of_employee)
gourav = Employee("gourav patel",20000)
# print("number of employee is :- ",Employee.no_of_employee)
rahul = Employee("rahul patel",50000)
# print("number of employee is :- ",Employee.no_of_employee)
# mehul = Employee("mehul patel",50000)
# print("number of employee is :- ",Employee.no_of_employee)

# print("name :- ",gourav.name,"\nsalary :- ",gourav.salary)
# print(rahul.name,rahul.salary)
# rahul.increase()
# print(rahul.salary)
# # print(gourav.__dict__)

# print(Employee.increment)
# Employee.change_increment(2.5)
# print(Employee.increment)


# sandeep = Employee.for_str("Sandeep patel-75000")
# print(sandeep.__dict__)


# print(Employee.isOpen("monday"))


# ankit = Progammer("Ankit kawar",25000,"Python","3 year")
# print(ankit.__dict__)
# ankit.increase()
# print(ankit.salary)

# print(Progammer.isOpen('sunday'))

