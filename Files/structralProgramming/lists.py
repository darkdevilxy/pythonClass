listData = [1, 13, 3, 5, 7, 9, 4]
max = listData[0]
for x in listData:
    if max < x:
        max = x
print(max)
