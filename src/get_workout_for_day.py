from datetime import datetime

SUNDAY_WORKOUT = 'https://www.instagram.com/p/B9woVmapcdH/'
MONDAY_WORKOUT = 'https://www.instagram.com/p/B9y7T1vpNXN/'
TUESDAY_WORKOUT = 'https://www.instagram.com/p/B91h_C9p3Sr/'
WED_WORKOUT = 'https://www.instagram.com/p/B94TdkDJZHj/'
THU_WORKDAY = 'https://www.instagram.com/p/B96sYevJQqF/'
FRI_WORKOUT = 'https://www.instagram.com/p/B-CguYyJ2lH/'
SAT_WORKOUT = 'https://www.instagram.com/p/B-E6vGKJfHZ/'


def return_work_out():
    weekday = datetime.today().weekday()
    if weekday == 6:
        return SUNDAY_WORKOUT
    elif weekday == 0:
        return MONDAY_WORKOUT
    elif weekday == 1:
        return TUESDAY_WORKOUT
    elif weekday == 2:
        return WED_WORKOUT
    elif weekday == 3:
        return THU_WORKDAY
    elif weekday == 4:
        return FRI_WORKOUT
    elif weekday == 5:
        return SAT_WORKOUT
