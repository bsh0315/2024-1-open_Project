class StudentGrades:
    def __init__(self):
        self.students = []

    def calculate_grade(self, avg):
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_rank(self, hakbun):
        sorted_students = sorted(self.students, key=lambda student: student['avg'], reverse=True)
        for i, student in enumerate(sorted_students):
            if student['hakbun'] == hakbun:
                return i + 1
        return None

    def insert_student(self, name, hakbun, eng, C_language, python):
        student = {
            "name": name,
            "hakbun": hakbun,
            "eng": eng,
            "C_language": C_language,
            "python": python,
            "total": eng + C_language + python,
            "avg": (eng + C_language + python) / 3
        }
        self.students.append(student)

    def delete_student(self, hakbun):
        self.students = [student for student in self.students if student["hakbun"] != hakbun]

    def find_student_by_hakbun(self, hakbun):
        for student in self.students:
            if student["hakbun"] == hakbun:
                return student
        return None

    def find_student_by_name(self, name):
        for student in self.students:
            if student["name"] == name:
                return student
        return None

    def sort_students_by_total(self):
        self.students.sort(key=lambda student: student["total"], reverse=True)

    def count_students_with_avg_above(self, threshold):
        count = 0
        for student in self.students:
            if student["avg"] >= threshold:
                count += 1
        return count

    def print_students(self):
        print("\t\t 성적관리 프로그램")
        print("==============================================================================================")
        print(" 학번     이름      영어      C-언어      파이썬         총점       평균   학점        등수 ")
        print("==============================================================================================")
        for i, student in enumerate(self.students):
            grade = self.calculate_grade(student['avg'])
            rank = self.calculate_rank(student['hakbun'])
            print(f"{student['hakbun']:<10} {student['name']:<10} {student['eng']:<10} {student['C_language']:<10} {student['python']:<10} {student['total']:<10} {student['avg']:.2f} {grade:<10} {rank}")

if __name__ == "__main__":
    student_grades = StudentGrades()
    for _ in range(5):
        name = input("이름: ")
        hakbun = input("학번: ")
        eng = int(input("영어 점수: "))
        C_language = int(input("C언어 점수: "))
        python = int(input("파이썬 점수: "))
        student_grades.insert_student(name, hakbun, eng, C_language, python)

    while True:
        print("1. 학생 추가, 2. 학생 삭제, 3. 학생 검색, 4. 학생 정렬, 5. 80점 이상 학생 수, 6. 학생 출력, 7. 종료")
        choice = int(input("선택: "))
        if choice == 1:
            name = input("이름: ")
            hakbun = input("학번: ")
            eng = int(input("영어 점수: "))
            C_language = int(input("C언어 점수: "))
            python = int(input("파이썬 점수: "))
            student_grades.insert_student(name, hakbun, eng, C_language, python)
        elif choice == 2:
            hakbun = input("삭제할 학번: ")
            student_grades.delete_student(hakbun)
        elif choice == 3:
            hakbun = input("검색할 학번: ")
            print(student_grades.find_student_by_hakbun(hakbun))
        elif choice == 4:
            student_grades.sort_students_by_total()
        elif choice == 5:
            print(student_grades.count_students_with_avg_above(80))
        elif choice == 6:
            student_grades.print_students()
        elif choice == 7:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")