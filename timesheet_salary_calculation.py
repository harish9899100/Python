import pandas as pd

def calculate_monthly_salary(hourly_rate, overtime_rate=1.5):
    df = pd.read_excel('/home/harish/Downloads/harbinger-timesheet .xlsx')

    total_regular_hours = df['Hours_Worked'].sum()

    total_overtime_hours = df['Overtime_Hours'].sum()

    df['Leave_Type'] = df['Leave_Type'].fillna('')

    unpaid_leave_days = len(df[df['Leave_Type'].str.lower() == 'unpaid'])
    deduction_for_unpaid_leave = unpaid_leave_days * 8 * hourly_rate

    regular_pay = total_regular_hours * hourly_rate
    overtime_pay = total_overtime_hours * hourly_rate * overtime_rate
    gross_salary = regular_pay + overtime_pay - deduction_for_unpaid_leave

    salary_breakdown = {
        "Total_Regular_Hours": total_regular_hours,
        "Total_Overtime_Hours": total_overtime_hours,
        "Regular_Pay": f"Rs.{regular_pay}",
        "Overtime_Pay": f"Rs.{overtime_pay}",
        "Deduction_for_Unpaid_Leave": f"Rs.{deduction_for_unpaid_leave}",
        "Gross_Salary": f"Rs.{gross_salary:.2f}"
    }

    return salary_breakdown

## driver logic
employee_hourly_rate = 440
overtime_multiplier = 1.5

salary_result = calculate_monthly_salary(employee_hourly_rate, overtime_multiplier)
print("Monthly Salary Report")
new_salary_result = pd.Series(salary_result)
print(new_salary_result)
