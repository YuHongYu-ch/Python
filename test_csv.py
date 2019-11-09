import csv

#读取csv文件内容
reader = csv.reader(open(r'D:\Temp\1.csv'))
for list in reader:
    print(list)