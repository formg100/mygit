#使用OS模块执行操作系统命令
import os
if os.name == "nt" :
    command = "e:"
else :
    command = "ls -l"
os.chdir("D:\\")
os.system(command)
os.system("cmd")
os.system("f:")
os.system("cd liulun")