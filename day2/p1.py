emp_name = input('enter the Name of the Employee : ')
emp_Id = int(input('enter the Id of the Employee : '))
basic_Monthly_Salary = float(input('enter the Basic Monthly Salary of the Employee : '))
special_Allowance = int(input('enter the Special Allowance :  '))
bonus_Percentage = int(input('enter the Bonus Percentage of the Employee : '))
gross_Monthly_Salary = basic_Monthly_Salary + special_Allowance
annual_Gross_Salary = (gross_Monthly_Salary * 12) +  (bonus_Percentage/100)*basic_Monthly_Salary

print(gross_Monthly_Salary)
print(annual_Gross_Salary)