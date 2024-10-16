# loop
import random

# random生成一个 list 复杂一点 用于测试冒泡排序
a = [random.randint(1, 100) for i in range(10)]
print(a)


# 冒泡排序
def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


bubble_sort(a)

print(a)
