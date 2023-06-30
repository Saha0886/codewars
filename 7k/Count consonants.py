def consonant_count(s):
    glas="aeiou _!@#$%^&*№:? AEIOU"
    a=0
    for i in s:
        if not i in glas and  not i.isdigit():
            a+=1
    return a
