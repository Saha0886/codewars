def longest(a1, a2):
    a3=""
    for i in a2 :
        if not i  in a3:
            a3+=i
    for i in a1 :
        if not i in a3:
            a3+=i
    return("".join(sorted(a3)))
    
