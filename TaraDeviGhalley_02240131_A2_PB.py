
import bisect

class PokemonCardBinder:
    MAX_POKEDEX_NUMBER = 1025
    GRID_ROWS = 8
    GRID_COLS = 8

    def __init__(self):
        self.CARDS_PER_PAGE = self.GRID_ROWS * self.GRID_COLS
        self.binder = []

    def calculate_position(self, index: int):
        page = index // self.CARDS_PER_PAGE + 1
        index_within_page = index % self.CARDS_PER_PAGE
        row = index_within_page // self.GRID_COLS + 1
        col = index_within_page % self.GRID_COLS + 1
        return page, row, col

    def add_card(self, pokedex_number: int):
        if not (1 <= pokedex_number <= self.MAX_POKEDEX_NUMBER):
            print("Error: Invalid Pokedex number!")
            return
        if pokedex_number in self.binder:
            index = self.binder.index(pokedex_number)
            page, row, col = self.calculate_position(index)
            print("Error: Duplicate card. Already in binder.")
            print(f"Location: Page {page}, Row {row}, Column {col}")
            return
        bisect.insort(self.binder, pokedex_number)
        index = self.binder.index(pokedex_number)
        page, row, col = self.calculate_position(index)
        print(f"Output:\nPage: {page}")
        print(f"Position: Row {row}, Column {col}")
        print(f"Status: Added Pokedex #{pokedex_number} to binder")

    def view_binder(self):
        if not self.binder:
            print("The binder is empty.")
            return
        print("Current Binder Contents:\n------------------------")
        for idx, pokedex_number in enumerate(self.binder):
            page, row, col = self.calculate_position(idx)
            print(f"Pokedex #{pokedex_number}:\n Page: {page}\n Position: Row {row}, Column {col}\n")
        print(f"Total cards in binder: {len(self.binder)}")
        print(f"% completion: {len(self.binder) / self.MAX_POKEDEX_NUMBER * 100:.1f}%")
        if len(self.binder) == self.MAX_POKEDEX_NUMBER:
            print("You have caught them all!!")

    def reset_binder(self, confirm_input: str):
        if confirm_input.upper() == "CONFIRM":
            self.binder.clear()
            print("The binder reset was successful! All cards have been removed.")
        else:
            print("Reset cancelled.")
def main():
    binder_manager = PokemonCardBinder()
    print("Welcome to Pokemon Card Binder Manager!")
    while True:
        print("\nMain Menu:")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")
        try:
            option = int(input("Select option: "))
        except ValueError:
            print("Invalid input. Enter a number between 1 and 4.")
            continue

        if option == 1:
            try:
                number = int(input("Enter Pokedex number: "))
                binder_manager.add_card(number)
            except ValueError:
                print("Invalid number. Please enter a valid integer.")
        elif option == 2:
            print("WARNING: This will delete ALL Pokemon cards from the binder.\nThis action cannot be undone.")
            user_input = input("Type 'CONFIRM' to reset or anything else to cancel: ")
            binder_manager.reset_binder(user_input)
        elif option == 3:
            binder_manager.view_binder()
        elif option == 4:
            print("Thank you for using Pokemon Card Binder Manager!")
            break
        else:
            print("Invalid option. Choose between 1 and 4.")

if __name__ == "__main__":
    main()
