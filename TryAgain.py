from datetime import datetime,timedelta

target = input("請輸入目標日期 ( 格式:YYYY-MM-DD )：") 
#2025-03-25(字串)
target = datetime.strptime(target,'%Y-%m-%d') 
#經過函數轉換成日期,格式相同但已是日期 2025-03-25
now = datetime.now() 
#今天日期時間 格式 2025-03-27 10:49:21.815313
tomo = now+timedelta(days= 1) 
#明天日期時間 格式 2025-03-27 10:49:21.
#days決定要多幾天(1、2、3)或少幾天(-1、-2、-3)
week = {0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期日'}
day = now.weekday()
tomo_day = tomo.weekday()
#^^^^ 得出星期幾代表的數字,代入week這個dict得出星期幾
# now.weekday() 今天換算出來是3, week[3] => 透過3這個key去dict裡找出星期四這個value
dist = abs(now.date()-target.date())
#因會有負數  但天數不會是負的所以加上abs來輸出絕對值
# datetime.now().date()只輸出日期的部分 2025-03-27
#日期與日期才可以相減與比較

print(f'今天 {now.strftime("%Y-%m-%d")} {week[day]}')
print(f'明天 {tomo.strftime("%Y-%m-%d")} {week[tomo_day]}')
if target.date() > now.date():
    print(f'距離 {target.date()} 還有 {dist.days} 天')
elif target.date() == now.date():
    print(f'今天就是 {target.date()}')
else:
    print(f'{target.date()} 已經過去 {dist.days} 天')