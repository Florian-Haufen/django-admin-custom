from datetime import datetime, timedelta

date_time_str = '2018-06-29'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
print(date_time_obj.date())