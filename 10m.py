import csv

scores = []

with open("exam_results_homework.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        score = int(row["score"])
        scores.append(score)

if len(scores) > 0:
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)

    passed = 0
    for score in scores:
        if score >= 70:
            passed += 1

    print("Imtihon natijalari:")
    print(f"Eng yuqori ball: {highest}")
    print(f"Eng past ball: {lowest}")
    print(f"O'rtacha ball: {average:.2f}")
    print(f"70 yoki undan yuqori ball olganlar soni: {passed}")
else:
    print("Imtihon natijalari mavjud emas.")