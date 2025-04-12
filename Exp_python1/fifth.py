def input_data():
    # 创建一个空列表，用来存储学生数据
    students = []

    # 输入5个学生的数据
    for i in range(5):
        print(f"请输入第 {i + 1} 个学生的信息：")

        student_id = input("学号: ")
        name = input("姓名: ")
        scores = []

        # 输入三门课程的成绩
        for j in range(3):
            score = float(input(f"课程 {j + 1} 的成绩: "))
            scores.append(score)

        # 将学生的学号、姓名和成绩作为一个元组添加到列表中
        students.append((student_id, name, scores))

    return students


def output_data(students):
    # 输出所有学生的数据
    print("\n学生信息：")
    for student in students:
        student_id, name, scores = student
        print(f"学号: {student_id}, 姓名: {name}, 成绩: {scores}")


# 主程序
students = input_data()  # 获取学生数据
output_data(students)  # 输出学生数据
