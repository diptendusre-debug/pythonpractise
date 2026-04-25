num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())


def create_set(num1, num2, num3, num4):
    return [[i, j, k]
            for i in range(num1 + 1)
            for j in range(num2 + 1)
            for k in range(num3 + 1)
            if i + j + k != num4]

result = sorted(create_set(num1, num2, num3, num4))
print(result)
