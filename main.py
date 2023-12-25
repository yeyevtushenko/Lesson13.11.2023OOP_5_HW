class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def display_info(self):
        print(f"Бренд: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Потужність: {self.power}Вт")


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, coffee_type):
        super().__init__(brand, model, power)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"Приготування кави {self.coffee_type}")


class Blender(Device):
    def __init__(self, brand, model, power, speed_levels):
        super().__init__(brand, model, power)
        self.speed_levels = speed_levels

    def blend(self):
        print(f"Змішування на рівні швидкості {self.speed_levels}")


class MeatGrinder(Device):
    def __init__(self, brand, model, power, grind_type):
        super().__init__(brand, model, power)
        self.grind_type = grind_type

    def grind_meat(self):
        print(f"Перемелюю м'ясо для {self.grind_type}")


class Smartphone(Device):
    def __init__(self, brand, model, power, operating_system):
        super().__init__(brand, model, power)
        self.operating_system = operating_system

    def make_call(self, number):
        print(f"Дзвінок за номером {number} з використанням {self.brand} {self.model}")


class SmartWatch(Device):
    def __init__(self, brand, model, power, water_resistant):
        super().__init__(brand, model, power)
        self.water_resistant = water_resistant

    def display_time(self):
        print("Відображення поточного часу")


class Laptop(Device):
    def __init__(self, brand, model, power, screen_size):
        super().__init__(brand, model, power)
        self.screen_size = screen_size

    def run_application(self, app_name):
        print(f"Запуск {app_name} на ноутбуці {self.brand}")




coffee_machine = CoffeeMachine("Breville", "123", 1200, "Espresso")
coffee_machine.display_info()
coffee_machine.make_coffee()
print()

blender = Blender("Vitamix", "456", 1500, "High")
blender.display_info()
blender.blend()
print()

meat_grinder = MeatGrinder("KitchenAid", "789", 800, "Sausage")
meat_grinder.display_info()
meat_grinder.grind_meat()
print()

smartphone = Smartphone("Apple", "iPhone 13", 2000, "iOS")
smartphone.display_info()
smartphone.make_call("123-456-7890")
print()

smartwatch = SmartWatch("Samsung", "Galaxy Watch 4", 300, True)
smartwatch.display_info()
smartwatch.display_time()
print()

laptop = Laptop("Dell", "XPS 13", 120, 13.3)
laptop.display_info()
laptop.run_application("Word Processor")