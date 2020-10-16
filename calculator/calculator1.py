'''
计算器  声明两个变量 输入运算符 复杂的一笔
如1+2
'''
def op():
    all_name = input("请输入‘1 + 2’格式：")
    h = all_name.strip().split(" ")
    first_name = h[0]
    operation = h[1]
    second_name = h[2]

    if "." in first_name or "." in second_name:
        first_name = float(first_name)
        second_name = float(second_name)
    else:
        first_name = int(first_name)
        second_name = int(second_name)

    result = 0
    if operation == "+":
        result = first_name + second_name
    elif operation == "-":
        result = first_name - second_name
    elif operation == "*":
        result = first_name * second_name
    elif operation == "/":
        result = first_name / second_name
    elif operation == "**":
        result = first_name ** second_name
    elif operation == "&":
        result = first_name & second_name
    elif operation == "|":
        result = first_name | second_name
    elif operation == "^":
        result = first_name ^ second_name
    elif operation == "%":
        result = first_name % second_name
    elif operation == ">>":
        result = first_name >> second_name
    elif operation == "<<":
        result = first_name << second_name

    return result
