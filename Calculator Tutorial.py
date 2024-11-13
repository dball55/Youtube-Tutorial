import math
print('Welcome to the Area Finder app!')
print('To start, select 1 for Triangle, or 2 for Square/Rectangle , or 3 for circle, or 4 to terminate programme')


def main():
    while True:
        choice = int(input('Your choice here: '))

        if choice == 1:
            base = float(input('Base length: '))
            height = float(input('Height length: '))
            new_area = base * height
            factor = 0.5
            correct_area = new_area * factor
            print(f"The area of the triangle is {correct_area} cm^2")

        elif choice == 2:
            base = float(input('Base length: '))
            height = float(input('Height length: '))
            new_area = base * height
            if base == height:
                print(f"The area of the square is {new_area} cm^2")
            else:
                print(f"The area of the rectangle is {new_area} cm^2")

        elif choice == 3:
            radius = float(input('Radius length: '))
            area = pow(radius, 2)
            circle_area = math.pi * area
            print(f"The area of the cirlce is {float(round(circle_area, 2))} cm^2")

        elif choice == 4:
            print('Have a nice day!')
            break
            
                        

main()
        
