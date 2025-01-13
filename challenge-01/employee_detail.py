import pandas as pd

employees_df = pd.read_excel(r"C:\Users\Admin\striim\challenge-01\table_data.xlsx", sheet_name="Employees")
devices_df = pd.read_excel(r"C:\Users\Admin\striim\challenge-01\table_data.xlsx", sheet_name="Devices")
# print(employees_df)
# print(devices_df)

# ~employees_df["id"].isin(devices_df["employee_id"]) '~' is a not symbol used to get only those employees not in devices sheet
employeesID_without_devices = employees_df[~employees_df["id"].isin(devices_df["employee_id"])] 

result = employeesID_without_devices[["id", "first_name", "last_name", "department", "location"]]
print(result)

