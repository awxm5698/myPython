import time
import datetime
import random

# print(time.ctime())
# print('90'+str(int(time.time()*1000))[-8:])
# time.sleep(0.01)
# print("当前时间：{}".format('99'+time.strftime("%d%H%M%S")))
# print(time.tzname)
#
#
# print(datetime.datetime.now())
# print((datetime.datetime.now()+datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime.timezone.utc)
# start = datetime.datetime.now().strftime("%I:00 %p")
# end = (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%I:00 %p")
# slot = '{} - {}'.format(start, end)
# ship = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:00:00")
# print(ship)
# s = str(datetime.datetime.now())[:-3].replace(' ', 'T')
# print(s)
# #
# d = '{}{}'.format(s, random.randint(10, 99))

# d = datetime.datetime.strptime('2019-07-05T10:00:00', '%Y-%m-%dT%H:%M:%S')
# print(d.strftime('%a %b %d, %I:%M %p'))

# t_hour = datetime.datetime.now().strftime('%I')
# AM_PM = datetime.datetime.now().strftime('%p')
# if AM_PM == 'AM':
#     start_time = (datetime.datetime.now()+datetime.timedelta(hours=8)).strftime('%I:00 %p') if int(t_hour) < 8 \
#         else datetime.datetime.now().strftime('%I:00 %p')
#     end_time = (datetime.datetime.now()+datetime.timedelta(hours=9)).strftime('%I:00 %p') if int(t_hour) < 8 \
#         else (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime('%I:00 %p')
# if AM_PM == 'PM':
#     start_time = (datetime.datetime.now()+datetime.timedelta(hours=-8)).strftime('%I:00 %p') if int(t_hour) > 18 \
#         else datetime.datetime.now().strftime('%I:00 %p')
#     end_time = (datetime.datetime.now()+datetime.timedelta(hours=-7)).strftime('%I:00 %p') if int(t_hour) > 18 \
#         else (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime('%I:00 %p')
#
# schedule_time_slot = '{} - {}'.format(start_time, end_time)
#
# print(schedule_time_slot)

import time
date1 = time.strptime('2019-07-11', "%Y-%m-%d")

date2 = time.strptime(datetime.datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")

print(date1)
print(date2)
d = date2.tm_yday-date1.tm_yday
age = '{}岁{}月{}天'.format(date2.tm_year-date1.tm_year,
                         date2.tm_mon-date1.tm_mon,
                         date2.tm_mday-date1.tm_mday)

print(age)