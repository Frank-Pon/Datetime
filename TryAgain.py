from datetime import datetime,timedelta

target = input("請輸入目標日期 ( 格式:YYYY-MM-DD )：")
target = datetime.strptime(target,'%Y-%m-%d')
now = datetime.now() #今天日期時間
tomo = now+timedelta(days= 1)
week = {0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期日'}
day = now.weekday()
tomo_day = tomo.weekday()
dist = abs(now.date()-target.date())


print(f'今天 {now.strftime("%Y-%m-%d")} {week[day]}')
print(f'明天 {tomo.strftime("%Y-%m-%d")} {week[tomo_day]}')
if target.date() > now.date():
    print(f'距離 {target.date()} 還有 {dist.days} 天')
elif target.date() == now.date():
    print(f'今天就是 {target.date()}')
else:
    print(f'{target.date()} 已經過去 {dist.days} 天')