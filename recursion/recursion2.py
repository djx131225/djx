'''主函数'''
def list_insert_number():
    print("数列顺序排列并按顺序插入数字----")
    '''字符串数列转换为数字数列'''
    a = input("请输入数列：")
    h = a.replace("[","").replace("]","").split(",")
    m=[]
    for i in h:
        i = int(i)
        m.append(i)
    n = int(input("请输入数字："))
    '''数列排序'''
    m.sort()
    '''查看类型'''
    #print(m,type(m),type(n))
    '''调用递归'''
    count = hr(0,m,n)
    '''单个插入'''
    m.insert(count,n)
    return m

'''递归排序'''
def hr(count,m,n):
    if m[count] > n:
        return count
    return hr(count+1,m,n)
