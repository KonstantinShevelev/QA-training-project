# main.py

from shapes import Circle, Rectangle, Triangle
from utils import get_valid_float, get_valid_index


def main():
    shapes_db = []

    while True:
        print("\n--- MENU ---")
        print("1. Add new shape")
        print("2. List all shapes")
        print("3. Show shape details")
        print("4. Remove shape")
        print("5. Show sum of all areas")
        print("6. Show sum of all perimeters")
        print("7. Exit")

        option = input("Choose an option: ").strip()

        # 1) Add new shape
        if option == "1":
            print("\nTypes: 1. Circle, 2. Rectangle, 3. Triangle")
            shape_type = input("Select type: ").strip()

            if shape_type not in ("1", "2", "3"):
                print("Error: Invalid shape type. Please choose 1, 2, or 3.")
                continue

            color = input("Enter color: ").strip()

            try:
                if shape_type == "1":
                    radius = get_valid_float("Enter radius: ")
                    shape = Circle(color, radius)

                elif shape_type == "2":
                    width = get_valid_float("Enter width: ")
                    height = get_valid_float("Enter height: ")
                    shape = Rectangle(color, width, height)

                else:  # "3"
                    a = get_valid_float("Enter side a: ")
                    b = get_valid_float("Enter side b: ")
                    c = get_valid_float("Enter side c: ")
                    shape = Triangle(color, a, b, c)

                shapes_db.append(shape)
                print("Success: Shape added!")

            except ValueError as e:
                print(f"Logic Error: {e}")

        # 2) List all shapes
        elif option == "2":
            if not shapes_db:
                print("List is empty.")
                continue

            print("\n--- ALL SHAPES ---")
            for i, shape in enumerate(shapes_db, 1):
                print(f"{i}. {shape}")

        # 3) Show shape details
        elif option == "3":
            if not shapes_db:
                print("List is empty.")
                continue

            print("\n--- SHAPE DETAILS ---")
            idx = get_valid_index(f"Enter shape number (1-{len(shapes_db)}): ", len(shapes_db))
            shape = shapes_db[idx]

            print("------------------------------")
            print(f"Info:      {shape}")
            print(f"Area:      {shape.get_area():.2f}")
            print(f"Perimeter: {shape.get_perimeter():.2f}")
            print("------------------------------")

        # 4) Remove shape
        elif option == "4":
            if not shapes_db:
                print("List is empty.")
                continue

            print("\n--- REMOVE SHAPE ---")
            idx = get_valid_index(
                f"Enter shape number to remove (1-{len(shapes_db)}): ",
                len(shapes_db)
            )
            removed = shapes_db.pop(idx)
            print(f"Success: Removed {removed}")

        # 5) Show sum of all areas
        elif option == "5":
            total_area = sum(s.get_area() for s in shapes_db)
            print(f"Total Area of {len(shapes_db)} shapes: {total_area:.2f}")

        # 6) Show sum of all perimeters
        elif option == "6":
            total_perimeter = sum(s.get_perimeter() for s in shapes_db)
            print(f"Total Perimeter of {len(shapes_db)} shapes: {total_perimeter:.2f}")

        # 7) Exit
        elif option == "7":
            print("Goodbye!")
            break

        # Invalid option
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
