import pandas as pd

class EmployeeSalaryCalculator:
    def __init__(self, file_path, hourly_rate, overtime_rate=1.5):
        self.file_path = file_path
        self.hourly_rate = hourly_rate
        self.overtime_rate = overtime_rate
        self.df = None
        self.salary_breakdown = {}

    def load_timesheet(self):
        """Load timesheet Excel file into DataFrame"""
        try:
            self.df = pd.read_excel(self.file_path)
            self.df['Leave_Type'] = self.df['Leave_Type'].fillna('')
        except FileNotFoundError:
            print("Error: Timesheet file not found.")
            return False
        return True

    def calculate_salary(self):
        """Calculate the employee's monthly salary"""
        if self.df is None:
            raise ValueError("Timesheet not loaded. Call load_timesheet() first.")

        total_regular_hours = self.df['Hours_Worked'].sum()
        total_overtime_hours = self.df['Overtime_Hours'].sum()

        unpaid_leave_days = len(self.df[self.df['Leave_Type'].str.lower() == 'unpaid'])
        deduction_for_unpaid_leave = unpaid_leave_days * 8 * self.hourly_rate

        regular_pay = total_regular_hours * self.hourly_rate
        overtime_pay = total_overtime_hours * self.hourly_rate * self.overtime_rate
        gross_salary = regular_pay + overtime_pay - deduction_for_unpaid_leave

        self.salary_breakdown = {
            "Total_Regular_Hours": total_regular_hours,
            "Total_Overtime_Hours": total_overtime_hours,
            "Regular_Pay": f"Rs.{regular_pay}",
            "Overtime_Pay": f"Rs.{overtime_pay}",
            "Deduction_for_Unpaid_Leave": f"Rs.{deduction_for_unpaid_leave}",
            "Gross_Salary": f"Rs.{gross_salary:.2f}"
        }

        return self.salary_breakdown

    def print_salary_report(self):
        """Prints the salary breakdown in a clean format"""
        if not self.salary_breakdown:
            print("Salary has not been calculated yet.")
            return
        
        print("\n===== Monthly Salary Report =====")
        for key, value in self.salary_breakdown.items():
            print(f"{key}: {value}")
        print("=================================")


# ---------- Driver Code ----------
if __name__ == "__main__":
    file_path = "/home/harish/Downloads/harbinger-timesheet .xlsx"
    hourly_rate = 440
    overtime_multiplier = 1.5

    calculator = EmployeeSalaryCalculator(file_path, hourly_rate, overtime_multiplier)

    if calculator.load_timesheet():
        calculator.calculate_salary()
        calculator.print_salary_report()
