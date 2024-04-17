def calculate_rank(sum_stu):
    rank = [0] * len(sum_stu)
    for i in range(len(sum_stu)):
        rank[i] = 1
        for j in range(len(sum_stu)):
            if sum_stu[i] < sum_stu[j]:
                rank[i] += 1
    return rank


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

def search_student(stu_list, target_name):
    for i, name in enumerate(stu_list["name"]):
        if name == target_name:
            return i  # 해당 이름의 인덱스 반환
    return -1  # 이름이 없는 경우 -1 반환


def sort_students(scores, sum_stu, stu_list, stu_num):
    # 총점에 따라 학생들을 정렬
    sorted_indices = sorted(range(len(sum_stu)), key=lambda k: sum_stu[k], reverse=True)
    sorted_sum_stu = [sum_stu[i] for i in sorted_indices]
    sorted_stu_list = {"name": [stu_list["name"][i] for i in sorted_indices]}
    sorted_stu_num = {"num": [stu_num["num"][i] for i in sorted_indices]}
    sorted_scores = {"eng": [scores["eng"][i] for i in sorted_indices],
                     "C_language": [scores["C_language"][i] for i in sorted_indices],
                     "python": [scores["python"][i] for i in sorted_indices]}
    return sorted_scores, sorted_sum_stu, sorted_stu_list, sorted_stu_num


def insert_student(scores, sum_stu, stu_list, stu_num):
    hakbun = int(input("새 학생의 학번 입력: "))
    name = input("새 학생의 이름 입력: ")
    print(f"{name}의 점수 입력")
    eng = int(input("영어점수: "))
    C_language = int(input("C언어 점수: "))
    python = int(input("파이썬 점수: "))

    scores["eng"].append(eng)
    scores["C_language"].append(C_language)
    scores["python"].append(python)
    stu_num["num"].append(hakbun)
    stu_list["name"].append(name)

    sum_stu.append(eng + C_language + python)

    return scores, sum_stu, stu_list, stu_num


def remove_student(scores, sum_stu, stu_list, stu_num):
    target_name = input("삭제할 학생의 이름 입력: ")
    if target_name in stu_list["name"]:
        index = stu_list["name"].index(target_name)
        del scores["eng"][index]
        del scores["C_language"][index]
        del scores["python"][index]
        del stu_num["num"][index]
        del stu_list["name"][index]
        del sum_stu[index]
        print(f"{target_name}의 정보가 삭제되었습니다.")
    else:
        print("해당 학생이 존재하지 않습니다.")

    return scores, sum_stu, stu_list, stu_num


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

    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 학생 추가")
        print("2. 학생 삭제")
        print("3. 학생 정보 정렬")
        print("4. 종료")
        choice = int(input("선택: "))

        if choice == 1:
            scores, sum_stu, stu_list, stu_num = insert_student(scores, sum_stu, stu_list, stu_num)
        elif choice == 2:
            scores, sum_stu, stu_list, stu_num = remove_student(scores, sum_stu, stu_list, stu_num)
        elif choice == 3:
            scores, sum_stu, stu_list, stu_num = sort_students(scores, sum_stu, stu_list, stu_num)
            for i in range(5):
                avg_stu = float(sum_stu[i] / 3.0)
                rank = calculate_rank(sum_stu)
                grade = calculate_grade(avg_stu)
                print(f"{stu_num['num'][i]:<10} {stu_list['name'][i]:<10} {scores['eng'][i]:<10} {scores['C_language'][i]:<10} {scores['python'][i]:<10} {sum_stu[i]:<10} {avg_stu:.2f}    {grade:<10} {rank[i]:<10}")
        elif choice == 4:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

        print("\t\t 성적관리 프로그램")
        print("==============================================================================================")
        print(" 학번     이름      영어      C-언어      파이썬         총점       평균   학점        등수 ")
        print("==============================================================================================")
        for i in range(len(stu_list['name'])):  # 학생 리스트의 길이를 사용
            avg_stu = float(sum_stu[i] / 3.0)
            rank = calculate_rank(sum_stu)
            grade = calculate_grade(avg_stu)
            print(f"{stu_num['num'][i]:<10} {stu_list['name'][i]:<10} {scores['eng'][i]:<10} {scores['C_language'][i]:<10} {scores['python'][i]:<10} {sum_stu[i]:<10} {avg_stu:.2f}    {grade:<10} {rank[i]:<10}")

if __name__ == "__main__":
    main()
