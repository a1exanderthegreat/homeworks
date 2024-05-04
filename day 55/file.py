positivelist = [ ]
negativelist = [ ]

mlist = [1, 6, 2, 4, 45, -23, -2, -423]

for num in mlist:
    if num > 0:
        positivelist.append(mlist)
    else:
        negativelist.append(mlist)

print(positivelist,negativelist)