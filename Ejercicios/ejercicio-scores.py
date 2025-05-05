student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

# for nombre, nota in student_scores.items():
#     if nota >= 91:
#         student_grades[nombre] = "Outstanding"
#     elif 81 <= nota <= 90:
#         student_grades[nombre] = "Exceeds Expectations"
#     elif 71 <= nota <= 80:
#         student_grades[nombre] = "Acceptable"
#     elif 70 > nota:
#         student_grades[nombre] = "Fail"
#     else:
#         student_grades[nombre] = nota  # deja la nota sin cambiar

# print(student_grades)

student_grades = {}

for nombre in student_scores:  # Solo recorre las claves
    nota = student_scores[nombre]  # Accede al valor con la clave
    if nota >= 91:
        student_grades[nombre] = "Outstanding"
    elif 81 <= nota <= 90:
        student_grades[nombre] = "Exceeds Expectations"
    else:
        student_grades[nombre] = nota

print(student_grades)
