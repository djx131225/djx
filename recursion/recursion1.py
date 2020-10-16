'''一个小例子'''
def ass():
    m = [1,3,4,8,2]
    n = 5
    count = 0
    m.sort()
    for i in m:
        if n > i:
            count += 1
    m.insert(count,n)
    return '{}{}'.format('example:',m)