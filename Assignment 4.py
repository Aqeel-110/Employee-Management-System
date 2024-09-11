class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def get_info(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nDepartment: {self.department}\nSalary: ${self.salary}"

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def is_salary_higher_than(self, threshold):
        return self.salary > threshold


# Creating Employee objects
employee1 = Employee(1, "John Doe", "Engineering", 60000)
employee2 = Employee(2, "Jane Smith", "Marketing", 55000)

# Displaying employee information
print("Employee 1:")
print(employee1.get_info())
print("\nEmployee 2:")
print(employee2.get_info())

# Applying raise to employee1
employee1.increase_salary(10)
print("\nEmployee 1 after raise:")
print(employee1.get_info())

# Checking if employees' salaries are higher than a threshold
threshold = 60000
print(f"\nIs Employee 1's salary higher than ${threshold}? {employee1.is_salary_higher_than(threshold)}")
print(f"Is Employee 2's salary higher than ${threshold}? {employee2.is_salary_higher_than(threshold)}")
