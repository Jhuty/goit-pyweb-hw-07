from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Subject, Teacher, Group

engine = create_engine('postgresql://postgres:0502660290@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()


"""Знайти 5 студентів із найбільшим середнім балом з усіх предметів"""
def select_1():
    results = session.query(
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    
    print("Топ 5 студентов с наивысшим средним баллом:")
    for name, average_grade in results:
        print(f"Студент: {name}, Средний балл: {average_grade:.2f}")

"""Знайти студента із найвищим середнім балом з певного предмета"""
def select_2(subject_name):
    results = session.query(
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    
    print(f"Студент с наивысшим средним баллом по предмету '{subject_name}':")
    if results:
        name, average_grade = results
        print(f"Студент: {name}, Средний балл: {average_grade:.2f}")
    else:
        print("Нет данных для данного предмета.")

"""Знайти середній бал у групах з певного предмета"""
def select_3(subject_name):
    results = session.query(
        Group.name.label('group_name'),
        func.avg(Grade.grade).label('average_grade')
    ).select_from(Student).join(Group).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Group.name).all()
    
    print(f"Средний балл по группам для предмета '{subject_name}':")
    for group_name, average_grade in results:
        print(f"Группа: {group_name}, Средний балл: {average_grade:.2f}")

"""Знайти середній бал на потоці (по всій таблиці оцінок)"""
def select_4():
    result = session.query(func.avg(Grade.grade)).scalar()
    
    print("Средний балл на потоке:")
    if result is not None:
        print(f"Средний балл: {result:.2f}")
    else:
        print("Нет данных.")


"""Знайти які курси читає певний викладач"""
def select_5(teacher_name):
    results = session.query(
        Subject.name
    ).select_from(Teacher).join(Subject).filter(Teacher.name == teacher_name).distinct().all()
    
    print(f"Курсы, которые читает преподаватель '{teacher_name}':")
    for subject_name, in results:
        print(f"Курс: {subject_name}")


"""Знайти список студентів у певній групі"""
def select_6(group_name):
    results = session.query(
        Student.name
    ).join(Group).filter(Group.name == group_name).all()
    
    print(f"Студенты в группе '{group_name}':")
    for name, in results:
        print(f"Студент: {name}")


"""Знайти оцінки студентів у окремій групі з певного предмета"""
def select_7(group_name, subject_name):
    results = session.query(
        Student.name,
        Grade.grade
    ).select_from(Student).join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()
    
    print(f"Оценки студентов в группе '{group_name}' по предмету '{subject_name}':")
    for student_name, grade in results:
        print(f"Студент: {student_name}, Оценка: {grade}")



"""Знайти середній бал, який ставить певний викладач зі своїх предметів"""
def select_8(teacher_name):
    result = session.query(
        func.avg(Grade.grade)
    ).select_from(Teacher).join(Subject).join(Grade).filter(Teacher.name == teacher_name).scalar()
    
    print(f"Средний балл, который ставит преподаватель '{teacher_name}':")
    if result is not None:
        print(f"Средний балл: {result:.2f}")
    else:
        print("Нет данных для данного преподавателя.")


"""Знайти список курсів, які відвідує певний студент"""
def select_9(student_name):
    results = session.query(
        Subject.name
    ).select_from(Student).join(Grade).join(Subject).filter(Student.name == student_name).distinct().all()
    
    print(f"Курсы, которые посещает студент '{student_name}':")
    for subject_name, in results:
        print(f"Курс: {subject_name}")


"""Список курсів, які певному студенту читає певний викладач"""
def select_10(student_name, teacher_name):
    results = session.query(
        Subject.name
    ).select_from(Student).join(Grade).join(Subject).join(Teacher).filter(Student.name == student_name, Teacher.name == teacher_name).distinct().all()
    
    print(f"Курсы, которые студенту '{student_name}' читает преподаватель '{teacher_name}':")
    for subject_name, in results:
        print(f"Курс: {subject_name}")

if __name__ == "__main__":
    select_1()  # Топ 5 студентов с наивысшим средним баллом
    print()
    select_2('forward')  # Студент с наивысшим средним баллом по предмету 'forward'
    print()
    select_3('forward')  # Средний балл по группам для предмета 'forward'
    print()
    select_4()  # Средний балл на потоке
    print()
    select_5('Sara Miller')  # Какие курсы читает преподаватель 'Sara Miller'
    print()
    select_6('interest')  # Список студентов в группе 'interest'
    print()
    select_7('interest', 'forward')  # Оценки студентов в группе 'interest' по предмету 'forward'
    print()
    select_8('Sara Miller')  # Средний балл, который ставит преподаватель 'Sara Miller'
    print()
    select_9('Philip Morris')  # Список курсов, которые посещает студент 'Philip Morris'
    print()
    select_10('Philip Morris', 'Sara Miller')  # Список курсов, которые студенту 'Philip Morris' читает преподаватель 'Sara Miller'