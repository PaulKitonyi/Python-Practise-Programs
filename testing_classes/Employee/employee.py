class Employee():
    """class to simulate Employees"""
    def __init__(self, first, last, annual_salary):
        self.first         = first
        self.last          = last
        self.annual_salary = annual_salary

    def give_raise(self, amount=''):
        self.annual_salary += 5000
        amount = amount
        if amount:
            self.annual_salary += amount
        return self.annual_salary



# emp_1 = Employee('pau', 'kitonyi', 1000)
# emp_1.give_raise(1000)
# print(emp_1.annual_salary)




        
        

