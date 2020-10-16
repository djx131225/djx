import re
'''
移动号码开头的：139，137，158，150
联通：120,131,132,185,186,145
电信：133,153,180,189
'''
def checkCellPhone(cellphone):
    regex = "^((13[0-9])|(14[5|7])|(15[0-3]|[5-9])|(18[0,5-9]))\d{8}$"
    result =re.findall(regex,cellphone)
    if result:
        print("success")
        return True
    else:
        return False
cellphone = "13726263205"
print(checkCellPhone(cellphone))
print(checkCellPhone("1545626266"))