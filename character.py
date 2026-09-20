class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.energy = 50
        self.level = 1

    def take_damage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

        print(self.name, "took", damage, "damage.")

    def heal(self, amount):
        self.health += amount

        if self.health > 100:
            self.health = 100

        print(self.name, "healed", amount, "health.")

    def use_energy(self, amount):
        if self.energy >= amount:
            self.energy -= amount
            print(self.name, "used", amount, "energy.")
        else:
            print("Not enough energy.")

    def level_up(self):
        self.level += 1
        print(self.name, "leveled up!")

    def show_status(self):
        self.show_name()
        print("Class:", self.character_class)
        print("Health:", self.health)
        print("Energy:", self.energy)
        print("Level:", self.level)

    def show_name(self):
        print("\n" + self.name)