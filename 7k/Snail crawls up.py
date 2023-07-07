def snail(column, daym, nightm):
    day=0
    metr=0
    while metr<column:
        metr+=daym
        if metr>=column:
            return day+1
        metr-=nightm
        day+=1
    return day
