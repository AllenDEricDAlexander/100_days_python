# Scope & Number Guessing Game
# 全局作用域
x = 10  # x 是全局变量


def outer_function():
    # 外部函数的作用域
    y = 20  # y 是外部函数的局部变量

    def inner_function():
        # 内部函数的作用域
        z = 30  # z 是内部函数的局部变量
        print("Inside inner_function:")
        print("x =", x)  # 访问全局变量
        print("y =", y)  # 访问外部函数变量
        print("z =", z)  # 访问内部函数变量

    inner_function()  # 调用内部函数

    print("\nInside outer_function:")
    print("x =", x)  # 访问全局变量
    print("y =", y)  # 访问外部函数变量
    # print("z =", z)  # 这里会报错，因为 z 只在 inner_function 中定义


# 调用外部函数
outer_function()

# 外部作用域中访问全局变量
print("\nOutside functions:")
print("x =", x)  # 访问全局变量
# print("y =", y)  # 会报错，因为 y 只在 outer_function 中定义
