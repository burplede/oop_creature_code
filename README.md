# Creature Battle Project (OOP + Git Branching Practice)

This project is designed to help me learn **object-oriented programming** in Python — especially **inheritance** — while also practicing key **Git concepts** like branching, merging, conflict resolution, and version history.

I will begin with a base class (`Creature`) and create additional subclasses on separate Git branches to simulate a real development workflow.

---

## Learning Objectives

### Python / OOP
- Understand and implement **classes**
- Use **inheritance** to extend behaviors
- Override and extend methods (e.g., `attack()`)
- Practice writing simple test code in `main`

### Git / Version Control
- Create and switch branches
- Merge branches into `main`
- Resolve merge conflicts
- View commit history (`git log --graph --all`)


---

## Project Structure

```
oop_creature_code/
│
├── creature_simulation.py # Base class + subclasses
└── README.md
```

The classes I made:
- `Creature` - the base class (on `main`)
- `FlyingCreature` - can `fly_to()` an altitude and attacks from above (`flying_creature` branch)
- `SwimmingCreature` - can `dive_to()` a depth and attacks from underwater (`swimming_creature` branch)
- `FireCreature` - can `emit_fire()` (fire level 0-100) and does extra damage when its fire is higher (`fire_creature` branch)

---

## How to Run and Test

You just need Python 3, nothing else to install.

Run this in the project folder:

```
python3 creature_simulation.py
```

(on Windows it might be `python` instead of `python3`)

All the tests are at the bottom of the file under `if __name__ == "__main__":`, so running the file runs all of them. Each test prints what the value should be and what it actually is, like:

```
Dummy HP should be 23 (40 - (9 + 8)) → Actual: 23
```

If the two numbers match then the test passed.

To see the branches and merges I did:

```
git log --all --graph
```
