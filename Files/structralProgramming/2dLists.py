listData = [
    [2, 4, 6, 8],
    [1, 2, 4, 2]
]
update = []
for listData in listData:
    if listData not in update:
        update.append(listData)
    for cols in listData:
        print(cols)
print(update)
