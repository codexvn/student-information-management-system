import hashlib
import sys
import json
import os
userdata = []
GID = -1
myusername=''
mypassword=0


# -1为初始值，0为超级管理员,1为管理员，2为教师，3为学生
# userdata为列表，其中的元素为字典
# userdata[0]为{'username':??,'password':??,'gid':??}
# 密码使用sha256校验
def locatedata(datalist: list, data):
    """用于在列表中查找元素,-1表示未找到"""
    i = 0
    for j in datalist:
        if j == data:
            return i
        else:
            i += 1
    return -1


def loginin():
    """使用账号密码登陆,密码校验为SHA-256"""
    global userdata
    global GID
    global myusername
    global mypassword
    if  os.path.exists('userdata.json'):
        with open('userdata.json', 'r') as userdatafile:
            userdata=json.load(userdatafile)
    else:
        print('无任何登陆信息,请添加一个超级管理员!')
        myusernameusername = input('请输入账号:')
        mypasswordpassword = input('请输入密码:')
        if mypasswordpassword == input('请再次输入你的密码:'):
            mypasswordpassword = hashlib.sha256(mypasswordpassword.encode('utf-8')).hexdigest()
            userdata=[]
            userdata.append({'username': myusernameusername, 'password': mypasswordpassword, 'gid': 0})
            writeuserdatafile()
            GID=0
            return True
        else:
            sys.stderr.write('2次密码不同，请重试!\n')
            return False
    myusername = input('请输入账号:\n')
    mypassword = input('请输入密码:\n')
    password = hashlib.sha256(mypassword.encode('utf-8')).hexdigest()
    usernamelist = [oneuser['username'] for oneuser in userdata]
    if myusername not in usernamelist:
        sys.stderr.write('用户不存在!\n')
        return False
    if password == userdata[locatedata(usernamelist, myusername)]['password']:
        GID = userdata[locatedata(usernamelist, myusername)]['gid']
        return True
    else:
        sys.stderr.write('密码错误!\n')


def useradd():
    """添加用户"""
    global userdata
    global GID
    global myusername
    global mypassword
    icanadd=('普通管理员','老师','学生')
    print('当前你可以添加的用户类型有:{}'.format('、'.join(icanadd[GID::])))
    if mypassword == input('请输入已登录账号的密码:'):
        username = input('请输入账号:\n')
        password = input('请输入密码:\n')
        if password == input('请再次输入密码:'):
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        else:
            sys.stderr.write('2次密码不同，请重试!\n')
            return 1
    else:
        sys.stderr.write('2次密码不同，请重试!\n')
        return 1
    usernamelist = [oneuser['username'] for oneuser in userdata]
    if username in usernamelist:
        sys.stderr.write('用户已存在!\n')
        return 1
    else:
        gid = int(input('请输入所添加用户的GID: \n0) 超级管理员组\n1) 普通管理员组\n2) 教师\n3) 学生\n:'))
    if gid <= GID:
        sys.stderr.write('你没有添加此用户的权限，请联系上级成员!\n')
        return 1
    else:
        userdata.append({'username': username, 'password': password, 'gid': gid})
        writeuserdatafile()
        return 0


def userdel():
    """删除用户"""
    global userdata
    global GID
    global mypassword
    if mypassword == input('请输入已登录账号的密码:'):
        username = input('请输入要删除账号:')
        usernamelist = [oneuser['username'] for oneuser in userdata]
        if username not in usernamelist:
            sys.stderr.write('用户不存在!\n')
            return 1
        if userdata[locatedata(usernamelist, username)]['gid'] <= GID:
            sys.stderr.write('你没有添加此用户的权限，请联系上级成员!\n')
            return 1
        password = input('请输入你的密码:')
        if password != input('请再次输入你的密码:'):
            sys.stderr.write('2次密码不同，请重试!\n')
            return 1
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if password != userdata[locatedata(usernamelist, username)]['password']:
            sys.stderr.write('密码错误，请重试!\n')
            return 1
        else:
            userdata.pop(locatedata(usernamelist, username))
            usernamelist.pop(locatedata(usernamelist, username))
            writeuserdatafile()
            return 0
    else:
        sys.stderr.write('2次密码不同，请重试!\n')
        return 1

def passwordedit ():
    """修改用户密码"""
    global userdata
    global GID
    global mypassword
    global myusername
    if mypassword == input('请输入已登录账号的密码:'):
        username = input('请输入要修改的账号:')
        usernamelist = [oneuser['username'] for oneuser in userdata]
        if username not in usernamelist:
            sys.stderr.write('用户不存在!\n')
            return 1
        if userdata[locatedata(usernamelist, username)]['gid'] < GID or (userdata[locatedata(usernamelist, username)]['gid'] == GID and username!=myusername):
            sys.stderr.write('你没有修改此用户的权限，请联系上级成员!\n')
            return 1
        password = input('请输入新密码:')
        if password == input('请确认新密码:'):
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            userdata[locatedata(usernamelist, username)]['password'] = password
            writeuserdatafile()
            return 0
        else:
            sys.stderr.write('2次密码不同，请重试!\n')
            return 1
    else:
        sys.stderr.write('2次密码不同，请重试!\n')
        return 1
def mypasswordedit ():
    """修改我的密码"""
    global userdata
    global mypassword
    global myusername
    if mypassword == input('请输入已登录账号的密码:'):
        password = input('请输入新密码:')
        if password == input('请确认新密码:'):
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            usernamelist = [oneuser['username'] for oneuser in userdata]
            userdata[locatedata(usernamelist, myusername)]['password'] = password
            writeuserdatafile()
            return 0
        else:
            sys.stderr.write('2次密码不同，请重试!\n')
            return 1
    else:
        sys.stderr.write('2次密码不同，请重试!\n')
        return 1
def writeuserdatafile():
    """写出登陆信息文件"""
    global userdata
    with open('userdata.json', 'w') as userdatafile:
        json.dump(userdata,userdatafile)
    return 0
