from datetime import datetime, timedelta, timezone

# 获取当前的datetime
now = datetime.now()
print('now = ', now)
print('type(now) = ', type(now))

# 用指定日期的时间创造datetime
dt = datetime(2019, 12, 29, 16, 54)
print('dt = ', dt)

# 把datetime转换为timestamp
print('datetime -> timestamp:', dt.timestamp())

# 把timestamp转换为datetime
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t))
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))

# 从str读取datetime
cday = datetime.strptime('2019-12-29 16:58:36', '%Y-%m-%d %H:%M:%S')
print('strptime:', cday)

# 把datetime格式化输出
print('strftime:', cday.strftime('%a, %b %d %H:%M'))

# 对日期进行加减
print('curren datetime = ', cday)
print('current + 10 hours = ', cday+timedelta(hours=10))
print('current - 1day =', cday - timedelta(days=1))
print('curren + 2.5 days = ', cday + timedelta(days=2, hours=12))

# 把时间从UTC+0时区转换为UTC+8
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now = ', utc_dt)
print('UTC+8:00 now = ', utc8_dt)
