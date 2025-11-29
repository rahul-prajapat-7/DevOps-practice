def calculate(a, b):
    add = a + b
    diff = a - b
    return add, diff

x, y = calculate(10, 5)
print("Sum:", x)
print("Difference:", y)


def user_details(**info):
    for key, value in info.items():
        print(key, ":", value)

user_details(name="Rahul", role="DevOps Engineer", experience=2)




