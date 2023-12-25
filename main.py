class Ship:
    def __init__(self, name, displacement, length):
        self.name = name
        self.displacement = displacement
        self.length = length

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Displacement: {self.displacement} tons")
        print(f"Length: {self.length} meters")


class Frigate(Ship):
    def __init__(self, name, displacement, length, num_missiles):
        super().__init__(name, displacement, length)
        self.num_missiles = num_missiles

    def fire_missile(self):
        print(f"{self.name} is firing a missile! Remaining missiles: {self.num_missiles}")


class Destroyer(Ship):
    def __init__(self, name, displacement, length, num_cannons):
        super().__init__(name, displacement, length)
        self.num_cannons = num_cannons

    def fire_cannon(self):
        print(f"{self.name} is firing a cannon! Remaining cannons: {self.num_cannons}")


class Cruiser(Ship):
    def __init__(self, name, displacement, length, num_torpedoes):
        super().__init__(name, displacement, length)
        self.num_torpedoes = num_torpedoes

    def launch_torpedo(self):
        print(f"{self.name} is launching a torpedo! Remaining torpedoes: {self.num_torpedoes}")



frigate = Frigate("FrigateA", 1500, 100, 20)
frigate.display_info()
frigate.fire_missile()
print()

destroyer = Destroyer("DestroyerB", 2000, 120, 30)
destroyer.display_info()
destroyer.fire_cannon()
print()

cruiser = Cruiser("CruiserC", 2500, 150, 15)
cruiser.display_info()
cruiser.launch_torpedo()
