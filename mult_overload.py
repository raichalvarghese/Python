class Employee:
    def __init__(self,name,salary_of_day):
        self.salary_of_day = salary_of_day
        self.name = name

        
class Number(Employee):
    def __init__(self,name,salary_of_day,no_of_days):
        self.no_of_days = no_of_days
        Employee.__init__(self,name,salary_of_day)
        
    def __mul__(self):
        return print(self.salary_of_day*self.no_of_days)
        
a = Number("A",20,10)




   
    
