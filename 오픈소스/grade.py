# 2021002006 신희주 
#오픈소스프로젝트 6주차

class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = english_score + c_score + python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()
        self.rank = None

    def calculate_grade(self):
        average = self.average_score
        if average >= 90:
            return 'A'
        elif 80 <= average < 90:
            return 'B'
        elif 70 <= average < 80:
            return 'C'
        elif 60 <= average < 70:
            return 'D'
        else:
            return 'F'

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def sort_students_by_total_score(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)

    def count_students_above_80(self):
        return sum(1 for student in self.students if student.total_score >= 240)  # 80 * 3

# 사용 예시
if __name__ == "__main__":
    grade_manager = GradeManager()

    for _ in range(5):
        student_id = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        english_score = int(input("영어 점수를 입력하세요: "))
        c_score = int(input("C-언어 점수를 입력하세요: "))
        python_score = int(input("파이썬 점수를 입력하세요: "))

        student = Student(student_id, name, english_score, c_score, python_score)
        grade_manager.add_student(student)

    grade_manager.sort_students_by_total_score()

    for i, student in enumerate(grade_manager.students):
        student.rank = i + 1
        print(f"{student.rank}등 - 학번: {student.student_id}, 이름: {student.name}, 총점: {student.total_score}, 평균: {student.average_score}, 학점: {student.grade}")

    above_80_count = grade_manager.count_students_above_80()
    print(f"80점 이상 학생 수: {above_80_count}")
