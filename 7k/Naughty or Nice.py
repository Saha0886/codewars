def naughty_or_nice(data):
    Naughty=0
    Nice=0
    for i in data:
        for j in data[i]:
            if data[i][j]=="Naughty":
                Naughty+=1
            else:
                Nice+=1
    if Naughty>Nice:
        return("Naughty!")
    elif Nice>Naughty:
        return("Nice!")
    else:
        return("Nice!")
