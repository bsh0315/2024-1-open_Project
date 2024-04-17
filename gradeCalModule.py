def input_scores():
    stu_num = {"num": []}
    scores = {"eng": [], "C_language": [], "python": []}
    stu_list = {"name": []}
    sum_stu = [0, 0, 0, 0, 0]

    for i in range(5):
        print("----------------------------------")
        
        hakbun = int(input(f"{i+1}번째 학생의 학번 입력: "))
        name = input(f"{i+1}번째 학생의 이름 입력: ")
        print(f"{name}의 점수 입력")
        eng = int(input("영어점수: "))
        C_language = int(input("C언어 점수: "))
        python = int(input("파이썬 점수: "))
        
        scores["eng"].append(eng)
        scores["C_language"].append(C_language)
        scores["python"].append(python)
        stu_num["num"].append(hakbun)
        stu_list["name"].append(name) 

        sum_stu[i] = eng + C_language + python

    return scores, sum_stu, stu_list, stu_num


def calculate_rank(sum_stu):
    rank_stu = [1] * 5
    for i in range(5):
        for j in range(5):
            if sum_stu[i] < sum_stu[j]:
                rank_stu[i] += 1
    return rank_stu


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif 80 <= avg < 90:
        return "B"
    elif 70 <= avg < 80:
        return "C"
    elif 60 <= avg < 70:
        return "D"
    else:
        return "F"


def main():
    scores, sum_stu, stu_list, stu_num = input_scores()
    print("\t\t 성적관리 프로그램")
    print("==============================================================================================")
    print(" 학번     이름      영어      C-언어      파이썬         총점       평균   학점        등수 ")
    print("==============================================================================================")
    for i in range(5):
        avg_stu = float(sum_stu[i] / 3.0)
        rank = calculate_rank(sum_stu)
        grade = calculate_grade(avg_stu)
        print(f"{stu_num['num'][i]:<10} {stu_list['name'][i]:<10} {scores['eng'][i]:<10} {scores['C_language'][i]:<10} {scores['python'][i]:<10} {sum_stu[i]:<10} {avg_stu:.2f}    {grade:<10} {rank[i]:<10}")


if __name__ == "__main__":
    main()