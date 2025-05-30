from faker import Faker
import random
from datetime import datetime, timedelta
from database import session
from models import Group, Student, Teacher, Subject, Grade

fake = Faker('uk_UA')

# Очистимо таблиці (для повторного запуску)
session.query(Grade).delete()
session.query(Student).delete()
session.query(Subject).delete()
session.query(Teacher).delete()
session.query(Group).delete()
session.commit()

# 1. Групи
groups = [Group(name=f"Група {i+1}") for i in range(3)]
session.add_all(groups)
session.commit()

# 2. Викладачі
teachers = [Teacher(fullname=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

# 3. Предмети
subject_names = ["Математика", "Фізика", "Хімія", "Історія", "Біологія"]
subjects = [
    Subject(name=name, teacher_id=random.choice(teachers).id)
    for name in subject_names
]
session.add_all(subjects)
session.commit()

# 4. Студенти
students = [
    Student(fullname=fake.name(), group_id=random.choice(groups).id)
    for _ in range(30)
]
session.add_all(students)
session.commit()

# 5. Оцінки (по кожному предмету кожному студенту за випадкові дні)
grades = []
for student in students:
    for subject in subjects:
        for _ in range(5):  # по 5 оцінок на предмет
            grade = Grade(
                student_id=student.id,
                subject_id=subject.id,
                grade=random.randint(60, 100),
                date_of=fake.date_between(start_date='-3M', end_date='today')
            )
            grades.append(grade)

session.add_all(grades)
session.commit()

print("✅ Дані успішно додані в базу.")
