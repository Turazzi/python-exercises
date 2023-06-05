#cash discount on purchase

purchase = float(input())
discount = float(input())

discount_perc = discount / 100
pay = purchase - discount_perc * purchase

print(f"{pay:.2f}")