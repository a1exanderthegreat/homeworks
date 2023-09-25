squad=['Aleksandre Grdzelidze', 'Nozadze Giorgi', 'Ilia Wiklauri', 'Mate Jorbenadze', 'Nika kandelaki', 'Natchkebia Nikolozi', 'Focxoraia Omari ', 'Giorgi Bibilashvili', 'Gurwkaia Giorgi', 'Zazashvili Luka']

squad2 = []

max_len = 0
for element in squad:
    if len(element) > max_len:
        max_len = len(element)
        res = element

squad2.append(res)
squad.remove(res)

max_len = 0
for element in squad:
    if len(element) > max_len:
        max_len = len(element)
        res = element

squad2.append(res)
print(squad2)