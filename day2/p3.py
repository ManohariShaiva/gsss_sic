import p2
if p2.taxable_income >= 0 and  p2.taxable_income  <= 300000:
    print(p2.taxable_income)
elif  p2.taxable_income >= 300001 and  p2.taxable_income <=600000:
    print((5/100)*p2.taxable_income )
elif  p2.taxable_income >= 600001 and  p2.taxable_income  <= 900000:
    print((10/100)*p2.taxable_income )
elif  p2.taxable_income >= 900001 and  p2.taxable_income  <= 1200000:
    print((15/100)*p2.taxable_income )
elif  p2.taxable_income >= 1200001 and  p2.taxable_income  <= 1500000:
    print((20/100)*p2.taxable_income )
else:
    print((30/100)*p2.taxable_income)

choice = str(input('Are you under 87A Rebate : '))
if choice == 'yes' and p2.taxable_income <= 700000:
    print("p2.taxable_income")

health_education_cess = p2.taxable_income + (4/100)*p2.taxable_income
p2.taxable_income += health_education_cess
print(p2.taxable_income)
 
