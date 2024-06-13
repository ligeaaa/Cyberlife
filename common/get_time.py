import datetime


def get_real_time():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%y%m%d%H%M%S")
    return formatted_time
