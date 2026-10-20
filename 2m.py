import csv

with open("students_homework.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    print("85 yoki undan yuqori ball olgan studentlar:")
    print("-" * 45)

    for row in reader:
        score = int(row["score"])

        if score >= 85:
            print(f"Ismi: {row['name']}, Balli: {score}")
