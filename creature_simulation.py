class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp = max(0, target.hp - self.attack_power)

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"

# ===============================
# FlyingCreature Branch
# ===============================

class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power, altitude=0):
        super().__init__(name, hp, attack_power)
        self.altitude = altitude

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} swoops down from altitude {self.altitude}!")
        print(f"{self.name} performs an aerial attack on {target.name} for {self.attack_power} damage!")
        target.hp = max(0, target.hp - self.attack_power)
        print(f"{target.name} HP is now {target.hp}")

# ===============================
# SwimmingCreature Branch
# ===============================

class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power, depth=0):
        super().__init__(name, hp, attack_power)
        self.depth = depth

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks from underwater at depth {self.depth}!")
        print(f"It splashes {target.name} for {self.attack_power} damage!")
        target.hp = max(0, target.hp - self.attack_power)
        print(f"{target.name} HP is now {target.hp}")

# ===============================
# FireCreature Branch
# ===============================

class FireCreature(Creature):
    MIN_FIRE = 0
    MAX_FIRE = 100

    def __init__(self, name, hp, attack_power, fire_level=0):
        super().__init__(name, hp, attack_power)
        self.fire_level = self._clamp_fire(fire_level)

    def _clamp_fire(self, level):
        # Keep fire_level inside the 0–100 range
        return max(self.MIN_FIRE, min(self.MAX_FIRE, level))

    def emit_fire(self, new_fire_level):
        self.fire_level = self._clamp_fire(new_fire_level)
        print(f"{self.name} burns at fire level {self.fire_level}.")

    def fire_bonus(self):
        # Every 10 fire levels adds +1 damage
        return self.fire_level // 10

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        damage = self.attack_power + self.fire_bonus()
        print(f"{self.name} blazes at fire level {self.fire_level}!")
        print(f"{self.name} scorches {target.name} for {damage} damage "
              f"({self.attack_power} base + {self.fire_bonus()} fire)!")
        target.hp = max(0, target.hp - damage)
        print(f"{target.name} HP is now {target.hp}")

if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)  # Expected: Goblin (HP: 30)
    print()

    # Test 2: Basic attack
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Wolf attacks Sheep")
    wolf.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.hp}")
    print()

    # Test 3: HP does not go below zero
    dragon = Creature("Dragonling", 50, 100)
    mouse = Creature("Mouse", 20, 1)
    print("Test 3: Dragonling overkills Mouse")
    dragon.attack(mouse)
    print(f"Mouse HP should now be 0 → Actual: {mouse.hp}")
    print()

    # Test 4: is_alive()
    slime = Creature("Slime", 10, 2)
    print("Test 4: Slime alive?")
    print("Slime should be alive →", slime.is_alive())
    slime.hp = 0
    print("Slime should NOT be alive →", slime.is_alive())
    print()

    # Test 5: Dead creature cannot attack
    ghost = Creature("Ghost", 0, 10)
    knight = Creature("Knight", 50, 7)
    print("Test 5: Ghost tries to attack Knight")
    ghost.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()

    # Test 6: Multiple attacks
    print("Test 6: Goblin attacks Slime twice")
    slime.hp = 10
    goblin.attack(slime)
    goblin.attack(slime)
    print(f"Slime should be at HP 0 → Actual: {slime.hp}")
    print()
    print("=== Tests Completed ===")
    print()

    print("=== FlyingCreature Tests ===\n")
    hawk = FlyingCreature("Sky Hawk", 50, 8)
    hawk.fly_to(120)
    print(f"Altitude should be 120 → Actual: {hawk.altitude}")

    dummy = Creature("Practice Dummy", 40, 0)
    hawk.attack(dummy)
    print(f"Dummy HP should be 32 → Actual: {dummy.hp}")
    dummy.attack(hawk)
    print()
    print("=== Tests Completed ===")
    print()

    print("=== SwimmingCreature Tests ===\n")
    serpent = SwimmingCreature("Aqua Serpent", 60, 7)
    serpent.dive_to(30)
    print(f"Depth should be 30 → Actual: {serpent.depth}")

    dummy = Creature("Practice Dummy", 40, 0)
    serpent.attack(dummy)
    print(f"Dummy HP should be 33 → Actual: {dummy.hp}")
    print()
    print("=== Tests Completed ===")
    print()

    print("=== FireCreature Tests ===\n")

    # Test 1: Initialization and default fire_level
    salamander = FireCreature("Salamander", 45, 9)
    print("Test 1: Initialization")
    print(salamander)  # Expected: Salamander (HP: 45)
    print(f"Fire level should start at 0 → Actual: {salamander.fire_level}")
    print()

    # Test 2: emit_fire() changes fire_level
    print("Test 2: Salamander emits fire")
    salamander.emit_fire(80)
    print(f"Fire level should be 80 → Actual: {salamander.fire_level}")
    print()

    # Test 3: fire_level stays within 0–100
    print("Test 3: Fire level limits")
    salamander.emit_fire(150)
    print(f"Fire level should be capped at 100 → Actual: {salamander.fire_level}")
    salamander.emit_fire(-20)
    print(f"Fire level should not go below 0 → Actual: {salamander.fire_level}")
    phoenix = FireCreature("Phoenix", 60, 12, fire_level=500)
    print(f"Phoenix fire level should be capped at 100 → Actual: {phoenix.fire_level}")
    print()

    # Test 4: Fire attack adds a bonus (attack_power + fire_level // 10)
    print("Test 4: Salamander attacks at fire level 80")
    salamander.emit_fire(80)
    dummy = Creature("Practice Dummy", 40, 0)
    salamander.attack(dummy)
    print(f"Dummy HP should be 23 (40 - (9 + 8)) → Actual: {dummy.hp}")
    print()

    # Test 5: No fire means no bonus
    print("Test 5: Salamander attacks with no fire")
    salamander.emit_fire(0)
    dummy = Creature("Practice Dummy", 40, 0)
    salamander.attack(dummy)
    print(f"Dummy HP should be 31 (40 - 9) → Actual: {dummy.hp}")
    print()

    # Test 6: HP does not go below zero
    print("Test 6: Phoenix overkills Mouse")
    mouse = Creature("Mouse", 5, 1)
    phoenix.attack(mouse)
    print(f"Mouse HP should be 0 → Actual: {mouse.hp}")
    print()

    # Test 7: Defeated fire creature cannot attack
    print("Test 7: Defeated Ember tries to attack Knight")
    ember = FireCreature("Ember", 0, 10, fire_level=50)
    knight = Creature("Knight", 50, 7)
    ember.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()

    # Test 8: FireCreature is still a Creature (inheritance)
    print("Test 8: Inheritance check")
    print("Salamander should be a Creature →", isinstance(salamander, Creature))
    print("Salamander should be alive →", salamander.is_alive())
    print()
    print("=== Tests Completed ===")
