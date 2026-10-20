import csv

with open("cities_homework.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    print("Aholisi 500 000 dan ko'p bo'lgan shaharlar:")
    count = 0

    for row in reader:
        population = int(row["population"])

        if population > 500000:
            print(f"Shahar: {row['city']}")
            count += 1

    print(f"Jami shaharlar soni: {count}")