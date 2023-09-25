

import random

squad=['Aleksandre Grdzelidze', 'Nozadze Giorgi', 'Ilia Wiklauri', 'Mate Jorbenadze', 'Nika kandelaki', 'Natchkebia Nikolozi', 'Focxoraia Omari ', 'Giorgi Bibilashvili', 'Gurwkaia Giorgi', 'Zazashvili Luka']

choice1 = random.choice(squad)
choice2 = random.choice(squad)
choice3 = random.choice(squad)
        
if choice1[-1] == "i":
    print(choice1 , "cool")
else:
    print(choice1)

if choice2[-1] == "i":
    print(choice2 , "cool")
else:
    print(choice2)

if choice3[-1] == "i":
    print(choice3 , "cool")
else:
    print(choice3)
