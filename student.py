import json
import os
import userdatatools
studentdata = []
studentlist = []
def studentdataload():
    """加载学生的成绩信息，此函数必须先执行"""
    global studentdata
    global studentlist
    if os.path.exists('studentdata.json'):
        with open('studentdata.json', 'r') as studentdatafile:
            studentdata = json.load(studentdatafile)
            if studentdata==[]:
                print('学生成绩信息库不存在!')
                return 1
            studentlist = [i['学号'] for i in studentdata]
            return 0
    else:
        print('学生成绩信息库不存在!')
        return 1


def addstudentdada():
    """添加学生成绩信息"""
    global studentdata
    if userdatatools.GID == 3:
        print('你没有权限修改学生数据!')
        return 1
    class_ = input('请输入该学生的班级:')
    ID = int(input('请输入该学生的学号:'))
    name = input('请输入该学生的姓名:')
    grades = {}
    for i in ('语文', '数学', '英语'):
        tmp = int(input('请输入该学生的{}成绩:'.format(i)))
        grades[i] = tmp
    studentdata.append({'班级': class_, '学号': ID, '姓名': name, '成绩': grades})
    writestudentdatafile()
    return 0


def delstudentdata():
    global studentlist
    global studentdata
    if userdatatools.mypassword != input('请输入已登录账号的密码:'):
        print('密码错误!')
        return 1
    if userdatatools.GID == 3:
        print('你没有权限修改学生数据!')
        return 1
    delid = int(input('请输入要删除学生的学号:'))
    if delid not in studentlist:
        print('该学生信息不存在，请联系管理员!')
        return 1
    studentdata.pop(userdatatools.locatedata(studentlist, delid))
    studentlist.pop(userdatatools.locatedata(studentlist, delid))
    return 0


def rewritestudentdata():
    """重新输入学生数据"""
    if userdatatools.mypassword != input('请输入已登录账号的密码:'):
        print('密码错误!')
        return 1
    if userdatatools.GID == 3:
        print('你没有权限修改学生数据!')
        return 1
    editid = int(input('请输入待修改信息所属学生的学号:'))
    if editid not in studentlist:
        print('该学生信息不存在，请联系管理员!')
        return 1
    class_ = input('请输入该学生的班级:')
    ID = int(input('请输入该学生的学号:'))
    name = input('请输入该学生的姓名:')
    grades = {}
    for i in ('语文', '数学', '英语'):
        tmp = int(input('请输入该学生的{}成绩:'.format(i)))
        grades[i] = tmp
    studentdata[userdatatools.locatedata(studentlist, editid)]({'班级': class_, '学号': ID, '姓名': name, '成绩': grades})
    writestudentdatafile()
    return 0


def viewstudentdata():
    global studentlist
    viewid = int(input('请输入待查看信息所属学生的学号:'))
    data=studentdata[userdatatools.locatedata(studentlist, viewid)]
    for i in ('班级', '学号', '姓名'):
        print('{}:{}'.format(i,data[i]))
    for i in ('语文', '数学', '英语'):
        print('{}:{}'.format(i,data['成绩'][i]))


def writestudentdatafile():
    """写出成绩信息文件"""
    global studentdata
    with open('studentdata.json', 'w') as studentdatafile:
        json.dump(studentdata, studentdatafile)
    return 0
