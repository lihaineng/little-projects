"""
pass:用来测试,跳过不想执行的代码块
"""
# 导包
import sys
import os

# 定义全局变量
info_list = []
userName = "admin"
passWord = "123456"

# 定义函数
def loadInfo():
    global info_list
    if os.path.exists("info_list.text"):
        f = open("info_list.text", "r", encoding="utf-8")
        data = f.read()
        info_list = eval(data)
        f.close()
    else:
        f = open("info_list.text", "w", encoding="utf-8")
        f.write("[]")
        f.close()

def saveInfo():
    global info_list
    f = open("info_list.text", "w", encoding="utf-8")
    f.write(str(info_list))
    f.close()

def print_menu():
    menu = """
       -----------名片管理系统V1.01----
               1,添加名片
               2,删除名片
               3,修改名片
               4,查询名片
               5,打印名片
               6,修改密码
               7,保存数据
               8,退出系统
       --------------------------------
       """
    print(menu)


def start():
    n = 0
    while True:
        user = input("欢迎使用卡片系统请输入用户姓名:")
        psw = input("欢迎使用卡片系统请输入用户密码:")
        n += 1
        if (user == userName) and (psw == passWord):
            print("密码正确,欢迎使用!")
            break
        else:
            print("用户名或密码输入错误,你还有%s次机会!" % (3 - n))
            if n == 3:
                print("系统关闭!")
                sys.exit()


def addCard():
    name = input("请输入姓名:")
    age = input("请输入年龄:")
    sex = input("请输入性别:")
    new_dic = {"姓名": name, "年龄": age, "性别": sex}  # 创建局部变量
    info_list.append(new_dic)
    print("[info]添加成功")
    #    print(info_list)                      用来测试所写功能是否正确


def deleCard():
    name = input("请输入你要删除人的姓名:")
    for i in info_list:
        if name in i.values():
            info_list.remove(i)
            print(info_list)
            print("删除成功")
            break
    else:
        print("输入的人不在")


def changeMessage():
    name = input("请输入你要修改的人姓名:")
    for i in info_list:
        if name in i.values():
            age = input("请输入年龄:")
            sex = input("请输入性别:")
            info_list[info_list.index(i)]["姓名"] = name
            info_list[info_list.index(i)]["年龄"] = age
            info_list[info_list.index(i)]["性别"] = sex
            print("修改成功")
            print(info_list)
            break
    else:  # 请注意else的位置,当出现for if break else 结构是要注意
        print("你输入的人不存在")
        print(info_list)


def searchCard():
    name = input("请输入你要查询的人姓名:")
    for i in info_list:
        if name in i.values():
            print(i)
            break
    else:
        print("你输入的人不存在")


def printfCard():
    name1 = input("请你输入用户名:")
    psw = input("请你输入密码:")
    if (userName == name1) and (passWord == psw):
        print(info_list)
    else:
        print("你输入的用户名或密码错误")
        sys.exit()


def checkPSW():
    global  userName
    global passWord
    name = input("请你输入用户名:")
    psw = input("请你输入密码:")
    if (userName == name) and (passWord == psw):
        userName = input("用户名改为:")
        passWord = input("密码改为:")


def exitCard():
    saveInfo()
    temp = input("确定删除(yes or no):")
    if temp.lower() in "yes":
        sys.exit()


def main():
    # 打印开始菜单
    print_menu()
    # 导入数据
    loadInfo()
    # 登入验证
    start()
    # 执行函数
    while True:
        # 输入要执行的操作
        command = input("请输入你想要的操作,数字1-8表示:")  # 这里用字符串要比数字好
        # 1,添加名片
        if command == "1":
            addCard()
        # 2,删除名片
        elif command == "2":
            deleCard()
        # 3,修改名片
        elif command == "3":
            changeMessage()
        # 4,查询名片
        elif command == "4":
            searchCard()
        # 5,打印名片
        elif command == "5":
            printfCard()
        # 6,修改密码
        elif command == "6":
            checkPSW()
        # 7,保存信息
        elif command == "7":
            saveInfo()
        # 8,退出系统
        elif command == "8":
            exitCard()
        else:
            print("指令错误!请输入正确的命令")

main()
