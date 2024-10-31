#  Day 9 - Beginner - Dictionaries, Nesting and the Secret Auction
# 定义一个嵌套字典
data = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "courses": ["Math", "Science"],
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "courses": ["Literature", "History"],
    },
}


# 函数：打印所有学生的信息
def print_students_info(nesting_dict):
    for student_id, info in nesting_dict.items():
        print(f"ID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Courses: {', '.join(info['courses'])}")
        print()


# 函数：添加新学生
def add_student(nesting_dict, student_id, name, age, courses):
    nesting_dict[student_id] = {
        "name": name,
        "age": age,
        "courses": courses,
    }


# 测试：打印原始学生信息
print("Original Student Information:")
print_students_info(data)

# 测试：添加新学生
add_student(data, "student3", "Charlie", 21, ["Physics", "Chemistry"])

# 测试：打印更新后的学生信息
print("Updated Student Information:")
print_students_info(data)
