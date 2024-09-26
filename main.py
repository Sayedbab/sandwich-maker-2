import data
from cashier import Cashier
from sandwich_maker import SandwichMaker

def main():
    resources = data.resources
    recipes = data.recipes

    sandwich_maker = SandwichMaker(resources)
    cashier = Cashier()

    while True:
        sandwich_size = input("Choose sandwich size (small, medium, large) or 'exit' to quit: ")
        if sandwich_size.lower() == 'exit':
            break
        if sandwich_size in recipes:
            order_ingredients = recipes[sandwich_size]['ingredients']
            cost = recipes[sandwich_size]['cost']
            print(f"The cost of a {sandwich_size} sandwich is ${cost}.")
            coins = cashier.process_coins()
            if cashier.transaction_result(coins, cost):
                print(sandwich_maker.make_sandwich(sandwich_size, order_ingredients))
            else:
                print("Insufficient funds.")
        else:
            print("Invalid sandwich size selected.")

if __name__ == "__main__":
    main()
