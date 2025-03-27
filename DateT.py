from datetime import datetime,timedelta

target = input("請輸入目標日期 ( 格式:YYYY-MM-DD )：")
target = datetime.strptime(target,'%Y-%m-%d')
now = datetime.now()
day = now.weekday()
tomo = now+timedelta(days=1)
week = {0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期日'}
dist = abs(now.date()-target.date())


print(f'今天 {now.strftime("%Y-%m-%d")} {week[day]}')
print(f'明天 {tomo.strftime("%Y-%m-%d")}')
if target.date() > now.date():
    print(f'距離 {target.strftime("%Y-%m-%d")} 還有 {dist.days} 天')
elif target.date() == now.date():
    print(f'{target.strftime("%Y-%m-%d")} 就是今天')
else:
    print(f'{target.strftime("%Y-%m-%d")} 已經過去 {dist.days} 天')