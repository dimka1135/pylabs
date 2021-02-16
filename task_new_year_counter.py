from datetime import datetime


def counter():
    ny = datetime.today().year + 1
    dleft = datetime(ny, 1, 1) - datetime.today()
    delta = dleft.days
    h = int(dleft.seconds / 60 / 60)
    m = int((dleft.seconds / 60) - ((int(dleft.seconds / 60 / 60)) * 60))

    if int(str(delta)[-1:]) == 1 and not 10 < int(delta) < 14:
        day = "день"
    elif 1 < int(str(delta)[-1:]) < 4 and not 10 < int(delta) < 14:
        day = "дня"
    else:
        day = "дней"

    if int(str(h)[-1:]) == 1 and not 10 < int(h) < 14:
        hour = "час"
    elif 1 < int(str(h)[-1:]) < 4 and not 10 < int(h) < 14:
        hour = "часа"
    else:
        hour = "часов"

    if int(str(m)[-1:]) == 1 and not 10 < int(m) < 14:
        minute = "минута"
    elif 1 < int(str(m)[-1:]) < 4 and not 10 < int(m) < 14:
        minute = "минуты"
    else:
        minute = "минут"

    return f'{delta} {day} {h} {hour} {m} {minute}'