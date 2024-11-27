bread = input("enter quantity of bread loafs: ").strip()
bread_guantity = float(bread)
bread_price = 24.35
total_bread = bread_guantity * bread_price

butter =input("enter quanity of butter g: ").strip()
butter_price_kg = 320.16
butter_price_g = butter_price_kg / 1000
total_butter = bread_guantity * butter_price_g

total= total_butter + total_bread
total = round(total, -1)
print("*" * 50)
print("RECEIPT")
print(f'Total amount of money for your purchase = {total}')
print('=' * 50)


