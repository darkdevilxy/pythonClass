def find_max(num):
    xxx = num[0]
    for i in num:
        if xxx < i:
            xxx =  i
    return xxx