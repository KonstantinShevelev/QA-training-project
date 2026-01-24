# utils/helpers.py

def get_valid_float(prompt: str) -> float:
    """Safely reads a float from user input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input format. Please enter a number.")


def get_valid_index(prompt: str, max_index: int) -> int:
    """
    Safely reads a 1-based choice from user and returns 0-based index.
    max_index is the maximum allowed number (e.g., len(list)).
    """
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= max_index:
                return value - 1
            print(f"Error: Please enter a number between 1 and {max_index}.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer number.")
