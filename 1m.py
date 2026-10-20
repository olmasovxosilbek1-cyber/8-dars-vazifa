import csv

with open("employees_homework.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    print("Xodimlar ro'yxati:")
    print("-" * 40)

    for row in reader:
        print(f"Ismi: {row['name']}, Bo'limi: {row['department']}")
