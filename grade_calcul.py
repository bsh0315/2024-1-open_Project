#2023041017 백승헌
stu_list = ["stu1", "stu2", "stu3", "stu4", "stu5"]
scores = {"eng": [], "C_language": [], "python": []}
sum_stu = [0, 0, 0, 0, 0]
avg_stu = [0, 0, 0, 0, 0]
rank_stu = [1, 1, 1, 1, 1]  # 모든 학생들을 1등으로 초기화합니다.

for i in range(5):
    print("----------------------------------")
    print(f"{stu_list[i]}의 점수 입력")
    eng = int(input("영어점수 : "))
    C_language = int(input("C언어 점수 : "))
    python = int(input("파이썬 점수 : "))

    scores["eng"].append(eng)
    scores["C_language"].append(C_language)
    scores["python"].append(python)

    sum_stu[i] = eng + C_language + python
    avg_stu[i] = float(sum_stu[i] / 3.0)

# 등수 매기기
def calculate_rank(sum_stu):
    for i in range(5):
        for j in range(5):
            if sum_stu[i] < sum_stu[j]:
                rank_stu[i] += 1

# 학점 계산
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif 80 <= avg:
        return "B"
    elif 70 <= avg:
        return "C"
    elif 60 <= avg:
        return "D"
    else:
        return "F"

for i in range(5):
    print(f"{stu_list[i]}의 총점 : {sum_stu[i]}")
    print(f"{stu_list[i]}의 평균 : {avg_stu[i]}")
    print(f"{stu_list[i]}의 등수 : {calculate_rank(sum_stu[i])}등")
    print(f"{stu_list[i]}의 학점 : {calculate_grade(avg_stu[i])}")
    print("======================================")
