# Filename:unzip.py
import os

#source_dir = input("Please input in source_dir:")      

#unzip_dir = input("Please input in unzip_dir:")
source_dir = os.getcwd()        #获取脚本文件所在路径

unzip_dir = '%s\\unzip\\' % source_dir    #创建解压缩文件存储路径

#windows RAR解压缩命令
rar_command = '"C:\\Program Files\\WinRAR\\Rar.exe" x %s\\*.rar * %s\\' \
              % (source_dir, unzip_dir)

if os.system(rar_command):
    print('successful!!!')
