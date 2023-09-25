


squad=['Aleksandre Grdzelidze', 'Nozadze Giorgi', 'Ilia Wiklauri', 'Mate Jorbenadze', 'Nika kandelaki', 'Natchkebia Nikolozi', 'Focxoraia Omari ', 'Giorgi Bibilashvili', 'Gurwkaia Giorgi', 'Zazashvili Luka']

i_count = 0
superlist = []


for element in squad:
    i_count = 0
    for char in element:
        if char == "i":
            i_count += 1

    if i_count > 2:
        superlist.append(element.capitalize())

print(superlist)