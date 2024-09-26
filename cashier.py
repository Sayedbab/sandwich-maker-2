class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            return True
        else:
            return False

