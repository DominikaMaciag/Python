# 2. Napisać program, który będzie wyświetlał bieżący czas aktualizowany dynamicznie

from datetime import datetime
import time

while True:
    now = datetime.now()
    second_now = str(now.second)
    minute_now = str(now.minute)
    hour_now = str(now.hour)

    if len(second_now) < 2:
        second_now = '0'+ second_now
    if len(minute_now) < 2:
        minute_now = '0'+ minute_now
    if len(hour_now) < 2:
        hour_now = '0'+ hour_now
        
    print(hour_now, ":", minute_now, ":", second_now, " ", end='\r')
    time.sleep(0.5)  

