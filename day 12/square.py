
side = int(input("Enter the side of a square : "))

def p_square(any_side):                                 
    print("Perimeter of a square :" ,any_side * 4)

p_square(side)


length = int(input("Enter the length of the rectangle : "))
width = int(input("Enter the width of the rectangle : "))

def calc_rect_area(any_width , any_length ):
    print("Area of the rectangle :" , any_length * any_width)

calc_rect_area(length , width)