dailyCostOfCare = float(input("Enter the daily cost of care: "))
numberOfDaysStayed = int(input("Enter the number of days you stayed: "))
VAT = 1.2

totalBill = (dailyCostOfCare * numberOfDaysStayed) * VAT

print("The total bill for your stay is:", totalBill) 