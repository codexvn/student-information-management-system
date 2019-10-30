import userdatatools
import os
def showoptions():
    """显示选项"""
    os.system("cls")
def student():
    print('\t\t当前登录的用户身份为:  学生\n\n\n')
if __name__ == "__main__":
    while not userdatatools.loginin():
        pass


