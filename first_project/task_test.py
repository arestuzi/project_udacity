"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

import csv
with open('test1.csv', 'r') as f:
    reader = csv.reader(f)
    calls1 = list(reader)


"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
phone_number = {}
sum_call = 0
for call in calls:
    if call[0] not in phone_number:
        phone_number[call[0]] = int(call[3])
    elif call[0] in phone_number:
        phone_number[call[0]] += int(call[3])
    elif call[1] not in phone_number:
        phone_number[call[1]] = int(call[3])
    elif call[1] in phone_number:
        phone_number[call[1]] += int(call[3])
print(phone_number)

max_time = 0
for number in phone_number:
    print(phone_number[number])
    if phone_number[number] > max_time:
        max_time = phone_number[number]
        print(str(phone_number[number]) + " " + number)