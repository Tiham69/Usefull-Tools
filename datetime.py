from _datetime import date, time, datetime, timedelta

today = date.today()

print(f'DATE: {today}')

yesterday = today - timedelta(days= 1)

print(f'YESTERDAY: {yesterday}')

tomorrow = today + timedelta(days= 1)

print(f'TOMORROW: {tomorrow}')

now = datetime.now()
todayT = datetime.today()
utc = datetime.utcnow()

print(f'Datetime Now: {now}')
print(f'Datetime Today: {todayT}')
print(f'Datetime UTC: {utc}')
