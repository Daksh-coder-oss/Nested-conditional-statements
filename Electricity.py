units_consumed=int(input("Please enter the amount units you have used"))


if units_consumed<=50:
    amount=units_consumed*2.60
    tax=25
elif units_consumed<=100:
    amount=(50*2.60)+((units_consumed-50)*3.25)
    tax=35
elif units_consumed<=200:
    amount=(50*2.60)+(50*3.25)+((units_consumed-100)*5.26)
    tax=45
else:
    amount=(50*2.60)+(50*3.25)+(100*5.26)+((units_consumed-200)*5.26)   
    tax=75
Total_bill=amount+tax
print(Total_bill)  