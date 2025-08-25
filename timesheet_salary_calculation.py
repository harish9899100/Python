import pandas as pd

def calculate_monthly_salary(timesheet_file, hourly_rate, overtime_rate=1.5):
   # df = pd.read_excel('/home/harish/Downloads/harbinger-timesheet')
    try:

        df = pd.read_excel('/home/harish/Downloads/harbinger-timesheet .xlsx')
    except FileNotFoundError:
        return {"error": f"Error: The file '{timesheet_file}' was not found."}

    required_cols = ['Date', 'Hours_Worked', 'Overtime_Hours', 'Leave_Type']
    if not all(col in df.columns for col in required_cols):
        return {"error": f"Error: Timesheet must contain columns: {required_cols}"}

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
        "Regular_Pay": f"${regular_pay:.2f}",
        "Overtime_Pay": f"${overtime_pay:.2f}",
        "Deduction_for_Unpaid_Leave": f"${deduction_for_unpaid_leave:.2f}",
        "Gross_Salary": f"${gross_salary:.2f}"
    }

    return salary_breakdown

if __name__ == "__main__":
    data = {
        'Date': pd.to_datetime(['2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05']),
        'Hours_Worked': [8, 8, 0, 8, 8],
        'Overtime_Hours': [2, 0, 0, 0, 4],
        'Leave_Type': ['Present', 'Present', 'Unpaid', 'Present', 'Persent']
    }
    df_timesheet = pd.DataFrame(data)
    dummy_file_path = "employee_timesheet.xlsx"
    df_timesheet.to_excel(dummy_file_path, index=True)

    employee_hourly_rate = 25.00
    overtime_multiplier = 1.5

    salary_result = calculate_monthly_salary(dummy_file_path, employee_hourly_rate, overtime_multiplier)

    if "error" in salary_result:
        print(salary_result["error"])
    else:
        print("--- Monthly Salary Report ---")
        for key, value in salary_result.items():
            print(f"{key.replace('_', ' '):<30}: {value}")