import datetime

date = "{}/{}/{} - {}:{}:{}".format(datetime.datetime.today().day, datetime.datetime.today().month, datetime.datetime.today().year, datetime.datetime.today().hour, datetime.datetime.today().minute, datetime.datetime.today().second)

print(date)