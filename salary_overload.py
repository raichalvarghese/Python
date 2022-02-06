class Salary:
    def __init__(self,salary_of_day,number_of_days):
        self.salary_of_day = salary_of_day
        self.number_of_days = number_of_days
    def total(self):
        self.total = self.salary_of_day * self.number_of_days
    def __LT__(self,other):
        if(self.total < other.total):
            return "Less"
        else:
            return "Not Less"

    
    
s1 = Salary(1200,25)
s2 = Salary(1500,22)
print(s1<s2)
