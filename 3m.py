import csv

count = 0

with open("books_homework.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        year = int(row["year"])

        if year > 2021:
            count += 1
            print(f"Kitob nomi: {row['title']}, Yili: {year}")

print(f"\n2021-yildan keyin nashr etilgan kitoblar soni: {count}")
