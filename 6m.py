import csv

min_item = ""
min_stock = None

with open("inventory_homework.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        stock = int(row["stock"])

        if min_stock is None or stock < min_stock:
            min_stock = stock
            min_item = row["item"]

if min_stock is not None:
    print("Omborda eng kam qolgan mahsulot:")
    print(f"Mahsulot nomi: {min_item}")
    print(f"Qolgan soni: {min_stock}")
else:
    print("Omborda mahsulotlar mavjud emas.")