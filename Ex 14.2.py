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
    def __init__(self, restaurant_name, cuisine_type, flavors, location, work_time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.work_time = work_time

        self.ice_lolly = []
        self.soft_ice = []
        self.sorbet = []

    def info_location_time(self):
        print(f'Локация: {self.location}')
        print(f'Время работы: {self.work_time}')

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f'Сорт "{flavor}" добавлен!')
        else:
            print(f'Сорт "{flavor}" уже есть')

    def delete_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f'Сорт "{flavor}" удален!')
        else:
            print(f'Сорта "{flavor}" нет')

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f'Да, "{flavor}" есть в наличии!')
        else:
            print(f'Нет, "{flavor}" нет в наличии')

    def flavors_list(self, flavors):
        print("Мороженое в наличии")
        if flavors in self.flavors:
            print(f"названия {flavors}")

    def add_ice_lolly(self, flavor):
        if flavor not in self.ice_lolly:
            self.ice_lolly.append(flavor)
            print(f'Мороженое на палочке "{flavor}" добавлено')

    def show_ice_lolly(self):
        print(f'Мороженое на палочке: {self.ice_lolly}')

    def add_soft_ice(self, flavor):
        if flavor not in self.soft_ice:
            self.soft_ice.append(flavor)
            print(f'Мягкое мороженое "{flavor}" добавлено')

    def show_soft_ice(self):
        print(f'Мягкое мороженое: {self.soft_ice}')

    def add_sorbet(self, flavor):
        if flavor not in self.sorbet:
            self.sorbet.append(flavor)
            print(f'Сорбет "{flavor}" добавлен')

    def show_sorbet(self):
        print(f'Сорбет: {self.sorbet}')

newIceCreamStand = IceCreamStand("Кимчи", "Корейская", ["Фисташковое", "Мятное", "Шоколадное"], "ул. Пушкина, д.10", "10:00 - 21:00")
newIceCreamStand.flavors_list("Мятное")
newIceCreamStand.flavors_list("Шоколадное")