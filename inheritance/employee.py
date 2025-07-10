class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, salary,hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        super().__init__(emp_id, name, salary)
    def salary(self):
        return self.hourly_rate * self.hours_worked
       
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, salary, monthly_salary):
        super().__init__(emp_id, name, salary)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        Total_salary = super().salary() + self.monthly_salary
        return Total_salary
       