import csv

total = 0

with open("products_homework.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])

        value = price * quantity
        total += value

        print(f"Mahsulot: {row['name']}")
        print(f"Narxi: {price}")
        print(f"Soni: {quantity}")
        print(f"Mahsulot qiymati: {value}")
        print("-" * 30)

print(f"Barcha mahsulotlarning umumiy qiymati: {total}")
