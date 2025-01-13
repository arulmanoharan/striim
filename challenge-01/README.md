# challenge 01
The python file employee_detail.py reads the csv file with 2 dataframes to store each sheet data into each data frame.

Now it takes employees_df["id"] which is id column of employee sheet and compares with employee_id column of device sheet device_df["employee_id"] , here it take not(~) of id = employee_id to get list of all employee ids that are not in device sheet and prints details of those employees.