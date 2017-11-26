"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""
send_receive_text_phone = []
for text in texts:
    if text[0] not in send_receive_text_phone:
        send_receive_text_phone.append(text[0])
    elif text[1] not in send_receive_text_phone:
        send_receive_text_phone.append(text[0])

receive_phone = []
for call in calls:
    if call[1] not in receive_phone:
        receive_phone.append(call[1])

telemarketers = []
for call in calls:
    if call[0] not in send_receive_text_phone and call[0] not in receive_phone:
        telemarketers.append(call[0])

print("\"These numbers could be telemarketers: \"")
unique_telemarketers = []
for telemarketer in telemarketers:
    if telemarketer not in unique_telemarketers:
        unique_telemarketers.append(telemarketer)

for unique_telemarketer in unique_telemarketers:
    print(unique_telemarketer)

