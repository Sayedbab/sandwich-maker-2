class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for ingredient, amount in ingredients.items():
            if self.machine_resources[ingredient] < amount:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        if self.check_resources(order_ingredients):
            for ingredient, amount in order_ingredients.items():
                self.machine_resources[ingredient] -= amount
            return f"{sandwich_size} sandwich made successfully."
        else:
            return "Insufficient resources to make the sandwich."
