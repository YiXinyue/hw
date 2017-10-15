import re
str= '我的电子邮件tom@gmail.com。 将什么发送到jerry123@163.com或者3123432@qq.com.若遇特殊情况打电话给182123445678.'
print(re.findall(r'[A-Za-z0-9]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+',str))
print(re.findall(r'1\d{11}',str))

#输出邮箱地址
mail=list(re.findall(r'[a-zA-Z0-9]+@(?:[a-zA-Z0-9]+\.)+[a-zA-Z]+',str))
i=0
while i<len(mail):
    print('mail',i+1,':',mail[i])
    i=i+1


#输出电话号码
phone=list(re.findall(r'1\d{11}',str))
j=0
while j<len(phone):
          print('phone',j+1,':',phone[j])
          j=j+1
