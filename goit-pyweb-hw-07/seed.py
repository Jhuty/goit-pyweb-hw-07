from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Subject, Teacher, Grade
from sqlalchemy import create_engine
import random

# Создаем объект Faker
fake = Faker()

# Подключение к базе данных
DATABASE_URL = 'postgresql://postgres:0502660290@localhost/postgres'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Очистка базы данных
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Генерация данных
groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word(), teacher_id=random.choice(teachers).id) for _ in range(5)]
session.add_all(subjects)
session.commit()

students = [Student(name=fake.name(), group_id=random.choice(groups).id) for _ in range(30)]
session.add_all(students)
session.commit()

# grades = [Grade(student=fake.random_element(students), value=fake.random_int(min=1, max=5)) for _ in range(15)]
# session.add.all(grades)
# session.commit()


for student in students:
    for _ in range(random.randint(15, 20)):
        grade = Grade(
            student_id=student.id,
            subject_id=random.choice(subjects).id,
            grade=random.randint(60, 100),
            date=fake.date_this_year()
        )
        session.add(grade)
session.commit()

print("Database seeded successfully!")
