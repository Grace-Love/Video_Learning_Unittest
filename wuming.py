#1、手机号码可以做随机数取值
2、将获得的值，给参数中的'aac030'
from random import randint

tel_num = '13' + str(randint(100000000,999999999))
print(tel_num)