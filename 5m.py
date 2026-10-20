
import csv

total = 0
count = 0

with open("orders_homework.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        amount = float(row["amount"])

        total += amount
        count += 1

        print(f"Buyurtma: {row['order_id']}")
        print(f"Mijoz: {row['customer']}")
        print(f"Summa: {amount}")
        print("-" * 30)

if count > 0:
    average = total / count

    print(f"Buyurtmalar summasi yig'indisi: {total}")
    print(f"O'rtacha buyurtma qiymati: {average:.2f}")
else:
    print("Buyurtmalar mavjud emas.")

