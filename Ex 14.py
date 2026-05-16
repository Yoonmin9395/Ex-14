class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name}')
        print(f'Тип кухни: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} открыт!')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def flavors_list(self, flavors):
        if flavors in self.flavors:
            print("Мороженое в наличии")
        else:
            self.flavors = self.flavors + flavors
        print(f'Мороженое в продаже: {self.flavors}')

newIceCreamStand = IceCreamStand("Кимчи", "Корейская", "Фисташковое ")

newIceCreamStand.flavors_list("Мятное ")
newIceCreamStand.flavors_list("Шоколадное ")