import csv

name = input("Student ismini kiriting: ")
age = int(input("Student yoshini kiriting: "))
score = int(input("Student ballini kiriting: "))

if score >= 70:
    with open("new_students_homework.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, score])

    print("Student CSV faylga qo'shildi!")
else:
    print("Ball 70 dan past. Student faylga qo'shilmadi.")