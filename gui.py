import os
import subprocess


spacer = "_-  _-  _-  _-  _-  _-  _-"

def disvar(x,y,z):
    while True:
        os.popen("powershell")
        whoami = os.popen('whoami').read()
        cd = os.popen('cd').read()
        whoami = whoami.strip()
        cd = cd.strip()



        cmdIN = input(f'{cd} | {whoami}>')
        cmdIN = cmdIN.split(" ")

        if cmdIN[0] == "cd" and cmdIN[1] != "":
            # cmdIN = cmdIN.replace(x[:3],"")
            print("ok")
            cmdOUT = os.chdir(cmdIN[1])
            print(os.popen("cd"))

        else:
            cmdOUT = os.popen(cmdIN[0]).read()
            print(cmdOUT)
    #
    # print("x = ",x)
    # print("y = ",y)
    # print("z = ",z)
    #


def enumwin():
    whoami = os.popen("whoami").read()
    netuser = os.popen("net user").read()
    localgroup = os.popen("net localgroup").read()
    print(f'''
cmd: whoami
out: {whoami}
{spacer}
    
cmd: net user
out: {netuser}
{spacer}
     
cmd: localgroup
out: {localgroup}
{spacer}    
''')


program = '''
1) Username Search
2) search username online
3) enum windows user
4) open cmd
'''


def main():
    while True:
        print(program)
        choice = input("what to do? ")
        if choice == "1":
            print("1")
            search()
        elif choice == "2":
            import monocle
            print("2")
        elif choice == "3":
            print("3")
            enumwin()
        elif choice == "4":
            x = "5"
            y = "6"
            z = "7"
            disvar(x,y,z)


def rdpen():
    localgroup = os.popen("net localgroup").read()
    localgroup.splitlines()
    rdp = "*Remote Desktop Users"
    print(localgroup)
    if True:
        print("ok")
        return "1"

main()