class Ingredient(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_cost(self):
        return self.cost


class Pizza(object):
    def __init__(self, name):
        self.name = name
    
    ingredient = []

    def add_ingredient(self, ingredient):
        self.ingredient.append(ingredient)

    def get_name(self):
        return self.name

    def get_weight(self):
        weight = 0
        for i in self.ingredient:
            weight += i.get_weight()
        return weight / 1000

    def get_cost(self):
        cost = 0
        for i in self.ingredient:
            cost += i.get_cost()
        return cost
        

class Order(object):
    pizza = list()
    def add_pizza(self, pizza):
        self.pizza.append(pizza)

    def get_cost(self):
        cost = 0
        for i in self.pizza:
            cost += i.get_cost()
        return cost

    def print_receipt(self):
        for i in self.pizza:
            print(f'{i.get_name()} ({"%.3f" % i.get_weight()}кг) - {"%.2f" % i.get_cost()}руб')