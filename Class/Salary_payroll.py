class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

class Salary:
    def __init__(self, emp_id, basic_salary):
        self.emp_id = emp_id
        self.basic_salary = basic_salary

class PayrollSystem:
    def __init__(self):
        self.employees = {}
        self.salaries = {}

    def add_employee(self, employee):
        if employee.emp_id not in self.employees:
            self.employees[employee.emp_id] = employee
            print(f"Employee {employee.name} added.")
        else:
            print(f"Employee with ID {employee.emp_id} already exists.")

    def add_salary(self, salary):
        if salary.emp_id not in self.salaries:
            self.salaries[salary.emp_id] = salary
            print(f"Salary details added for employee with ID {salary.emp_id}.")
        else:
            print(f"Salary details for employee with ID {salary.emp_id} already exist.")

    def calculate_net_salary(self, emp_id):
        if emp_id in self.employees and emp_id in self.salaries:
            basic_salary = self.salaries[emp_id].basic_salary
            # Add your logic to calculate net salary (e.g., deductions, allowances)
            net_salary = basic_salary  # Placeholder calculation
            return net_salary
        else:
            print("Employee or salary details not found.")
            return None

# Example usage:
# Create instances of employees, salaries, and payroll system
emp1 = Employee(1, "John Doe", "Engineering")
emp2 = Employee(2, "Jane Smith", "Marketing")

salary1 = Salary(1, 50000)
salary2 = Salary(2, 55000)

payroll_system = PayrollSystem()

# Add employees and their salaries to the payroll system
payroll_system.add_employee(emp1)
payroll_system.add_employee(emp2)

payroll_system.add_salary(salary1)
payroll_system.add_salary(salary2)

# Calculate net salary for an employee
emp_id_to_calculate = 1
net_salary = payroll_system.calculate_net_salary(emp_id_to_calculate)
if net_salary is not None:
    print(f"Net salary for employee with ID {emp_id_to_calculate}: {net_salary}")
