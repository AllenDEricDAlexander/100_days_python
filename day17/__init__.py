# quiz project in oop
class Question:
    def __init__(self, question_text, options, correct_answer):
        """
        初始化问题
        :param question_text: 问题文本
        :param options: 选项列表
        :param correct_answer: 正确答案
        """
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        """
        判断用户的答案是否正确
        :param answer: 用户选择的答案
        :return: 如果用户答案正确则返回True，否则返回False
        """
        return answer == self.correct_answer


class Quiz:
    def __init__(self, title):
        """
        初始化测验
        :param title: 测验的标题
        """
        self.title = title
        self.questions = []
        self.score = 0

    def add_question(self, question):
        """
        向测验中添加问题
        :param question: Question 实例
        """
        self.questions.append(question)

    def take_quiz(self):
        """
        启动测验，展示问题并接受用户输入，计算得分
        """
        print(f"欢迎参加《{self.title}》测验！\n")
        for i, question in enumerate(self.questions):
            print(f"问题 {i + 1}: {question.question_text}")
            for idx, option in enumerate(question.options, 1):
                print(f"{idx}. {option}")
            answer = input("请选择你的答案（输入数字）：")

            if question.is_correct(int(answer)):
                print("回答正确！\n")
                self.score += 1
            else:
                print(f"回答错误！正确答案是：{question.correct_answer}\n")

        print(f"测验结束！你的得分是：{self.score}/{len(self.questions)}")


class QuizApp:
    def __init__(self):
        self.quiz = None

    def create_quiz(self):
        """
        创建测验并添加问题
        """
        quiz_title = input("请输入测验的标题：")
        self.quiz = Quiz(quiz_title)

        while True:
            question_text = input("请输入问题文本（输入'结束'来结束问题添加）：")
            if question_text.lower() == '结束':
                break

            options = []
            for i in range(4):
                option = input(f"请输入选项 {i + 1}: ")
                options.append(option)

            correct_answer = int(input("请输入正确答案的选项编号（1-4）："))

            question = Question(question_text, options, correct_answer)
            self.quiz.add_question(question)
            print("问题添加成功！\n")

    def start_quiz(self):
        """
        启动测验
        """
        if self.quiz:
            self.quiz.take_quiz()
        else:
            print("没有可用的测验！")

    def run(self):
        """
        运行应用
        """
        while True:
            print("1. 创建测验")
            print("2. 开始测验")
            print("3. 退出")
            choice = input("请输入选择：")

            if choice == '1':
                self.create_quiz()
            elif choice == '2':
                self.start_quiz()
            elif choice == '3':
                print("感谢使用！")
                break
            else:
                print("无效选择，请重新输入。\n")


if __name__ == "__main__":
    app = QuizApp()
    app.run()
