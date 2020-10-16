'''
计算器  声明两个变量 输入运算符 稍微简单点了
如1+2
优化--浮点型与数值间空格可以去掉
'''

def reg(all_name):
    ls = ["+","-","*","/","&","|","^","//","**",">","<","=<","=>","!="]
    for i in ls:
        if i in all_name:
            x = all_name.split(i)
            x.append(i)
    return x

def cac():
    try:
        all_name = input("请输入‘1+2’格式：")
        h = reg(all_name)
        first_number = h[0]
        second_number = h[1]
        operation = h[2]
        return eval(first_number+operation+second_number)
    except:
        return "error input"