
import pandas as pd
import os

class EmployeeAnalyzer:

    def __init__(self, filename):
        self.filename = filename

    def create_dataset(self):
        if not os.path.exists(self.filename):
            data = {
                "Name": ["Amit", "Priya", "Rahul", "Sneha",
                         "Neha", "Rohan"],
                "Department": ["IT", "HR", "IT", "Finance",
                               "HR", "Finance"],
                "Salary": [50000, 35000, 65000, 45000,
                           40000, 70000]
            }

            df = pd.DataFrame(data)
            df.to_csv(self.filename, index=False)
            print("Employee dataset created successfully!")

    def load_data(self):
        return pd.read_csv(self.filename)

    def analyze_data(self):
        df = self.load_data()

        print("\n--- Employee Dataset ---")
        print(df.to_string(index=False))

        # Calculate average salary
        average = df["Salary"].mean()
        print("\nAverage Salary: Rs.", round(average, 2))

        # Count employees in each department
        print("\nDepartment-wise Employee Count:")
        print(df["Department"].value_counts().to_string())

    def filter_salary(self):
        df = self.load_data()

        try:
            threshold = float(input("\nEnter salary threshold: "))

            result = df[df["Salary"] > threshold]

            print("\nEmployees Above Salary Threshold:")
            if result.empty:
                print("No employees found.")
            else:
                print(result.to_string(index=False))

            # Export filtered results
            result.to_csv("high_salary_employees.csv",
                          index=False)

            print("\nResults saved to high_salary_employees.csv")

        except ValueError:
            print("Please enter a valid salary number!")


# Main program
analyzer = EmployeeAnalyzer("employees.csv")
analyzer.create_dataset()

while True:
    print("\n=== Employee Data Analysis ===")
    print("1. Display Employee Data")
    print("2. Analyze Salary and Departments")
    print("3. Filter Employees by Salary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(analyzer.load_data().to_string(index=False))

    elif choice == "2":
        analyzer.analyze_data()

    elif choice == "3":
        analyzer.filter_salary()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")