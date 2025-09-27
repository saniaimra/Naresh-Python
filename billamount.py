# write a program take input as price quantity discount and give bill amount

price_of_item = int(input("Enter price:"))

no_of_units = int(input("Enter quantity:"))

discount = int(input("Enter discount:"))

bill_amount = price_of_item * no_of_units

final_bill = bill_amount - (discount/100)*bill_amount

print("final_bill:",final_bill)

