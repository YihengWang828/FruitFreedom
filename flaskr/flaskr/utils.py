import time

def get_time():
    time_str = time.strftime("%Y {} %m {} %d %X")
    return time_str.format("年", "月", "日")
