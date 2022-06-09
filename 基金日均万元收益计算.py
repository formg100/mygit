
import datetime


#计算基金万元数乘以天数：daymoney 的函数

def daymoney(n):
    print("您买入第",n)
    year = int(input("笔基金的年份是："))
    month = int(input("月份是:"))
    day = int(input("您几号买入基金的:"))
    day1 = datetime.date(year,month,day)  #基金买入确认日期
    day2 = datetime.date.today()     #当前日期
    nday = day2-day1  #这是datetime.timedelta  日期相减差值后是timedelta类，形如25天，00:00:00
    print("基金买入确认日期到今天有",nday.days,"天")# 要引用datetime.timedelta  日期相减差值对象的天数，就要用nday.days对象,这是个数值类型
    money = float(input("请问您买了多钱基金："))
    money = money/10000
    print("您买了",money,"万元")
    return money*(nday.days)
#D1M1 = daymoney()
#D2M2 = daymoney()
#profit = float(input("请问您现在的收益是："))

t = int(input("这个基金你买了几笔？"))
i = 1 #次数循环
DM = 0 #万元数乘以天数
while t > 0:
    DM = DM + int(daymoney(i))
    t = t-1
    i = i+1
profit = float(input("请问您现在的收益是："))

x = profit/DM #万元每天收入x
print("1万元平均每天收入",x)


