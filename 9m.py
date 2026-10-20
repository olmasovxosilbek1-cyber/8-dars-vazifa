
import csv

with open("expenses_homework.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    with open("large_expenses.csv", "w", encoding="utf-8", newline="") as new_file:
        writer = csv.DictWriter(
            new_file,
            fieldnames=["category", "amount"]
        )

        writer.writeheader()

        for row in reader:
            amount = float(row["amount"])

            if amount > 200:
                writer.writerow({
                    "category": row["category"],
                    "amount": amount
                })

                print(f"Kategoriya: {row['category']}, Summa: {amount}")

print("Katta xarajatlar large_expenses.csv fayliga yozildi.")
