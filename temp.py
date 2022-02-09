from datetime import datetime
def current_time():
    return datetime.now().strftime("%H:%M:%S")

if current_time() == '10:00:00':
    print('10:00:00')
else:
    print('check tommorrow')
