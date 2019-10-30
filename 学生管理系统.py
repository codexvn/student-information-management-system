import userdatatools
import student
import os
import sys
def showoptions():
    """显示选项"""
    os.system("cls")
def loginasstudent():
    """学生可以查看学生的成绩信息，修改密码"""
    print('\t\t当前登录的用户身份为:  学生\n\n\n')
    while 1:
        print('请选择要进行的操作,退出请输入"exit":')
        print('1)查看学生成绩信息')
        print('2)修改我的密码')
        operand = input()
        if operand not in [ str(i)  for i in range(1,3)]+['exit']:
            print('请选择正确的操作')
            operand = input()
        elif operand == 'exit':
            sys.exit(0)
        elif operand=='1':
            student.viewstudentdata()
        else:
            userdatatools.mypasswordedit()
def loginasteacher():
    """老师可以查看学生的成绩信息，添加,重新录入,删除成绩学生信息，为学生添加,修改，删除登陆账号,修改自身密码"""
    print('\t\t当前登录的用户身份为:  老师\n\n\n')
    while 1:
        print('请选择要进行的操作,退出请输入"exit":')
        print('1)查看学生成绩信息')
        print('2)添加学生成绩信息')
        print('3)修改学生成绩信息')
        print('4)删除学生成绩信息')
        print('5)添加学生账户')
        print('6)修改学生密码')
        print('7)删除学生账户')
        print('8)修改我的密码')
        operand = input()
        if operand not in [ str(i)  for i in range(1,9)]+['exit']:
            print('请选择正确的操作')
            operand = input()
        elif operand == 'exit':
            sys.exit(0)
        elif operand=='1':
            student.viewstudentdata()
        elif operand == '2':
            student.addstudentdada()
        elif operand == '3':
            student.rewritestudentdata()
        elif operand == '4':
            student.delstudentdata()
        elif operand == '5':
            userdatatools.useradd()
        elif operand=='6':
            userdatatools.passwordedit()
        elif operand=='7':
            userdatatools.userdel()
        else:
            userdatatools.mypasswordedit()
def loginasadmire():
    """管理员可以查看学生的成绩信息，添加,重新录入,删除成绩学生信息，为老师,学生添加,修改，删除登陆账号，为自己修改密码"""
    print('\t\t当前登录的用户身份为:  管理员\n\n\n')
    while 1:
        print('请选择要进行的操作,退出请输入"exit":')
        print('1)查看学生成绩信息')
        print('2)添加学生成绩信息')
        print('3)修改学生成绩信息')
        print('4)删除学生成绩信息')
        print('5)添加成员账户')
        print('6)修改成员密码')
        print('7)删除成员账户')
        print('8)修改我的密码')
        operand = input()
        if operand not in [ str(i)  for i in range(1,9)]+['exit']:
            print('请选择正确的操作')
            operand = input()
        elif operand == 'exit':
            sys.exit(0)
        elif operand=='1':
            student.viewstudentdata()
        elif operand == '2':
            student.addstudentdada()
        elif operand == '3':
            student.rewritestudentdata()
        elif operand == '4':
            student.delstudentdata()
        elif operand == '5':
            userdatatools.useradd()
        elif operand=='6':
            userdatatools.passwordedit()
        elif operand=='7':
            userdatatools.userdel()
        else:
            userdatatools.mypasswordedit()
if __name__ == "__main__":
    while not userdatatools.loginin():
        pass
    student.studentdataload()
    if userdatatools.GID <=1:
        loginasadmire()
    elif userdatatools.GID == 2:
        loginasteacher()
    else:
        loginasstudent()




