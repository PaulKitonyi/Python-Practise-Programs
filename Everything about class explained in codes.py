import datetime

class Employee:

    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{},{}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod  #Are alternative constructors
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,e_str):
        first,last,pay = e_str.split('-')
        return cls(first,last,pay)

    @staticmethod #Dont operate on instance or class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.Employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())

    

    
    
mgr_1=Manager
dev1=Developer('paul','kitonyi',2000,'js')
dev2=Developer('Fred','mukoba',44000,'php')
Employee.set_raise_amt(1.5)


print(dev1.prog_lang)
print(dev2.pay)
print(Employee.fullname(dev1))
print(dev1.email)
print(Employee.num_of_emps)
        
