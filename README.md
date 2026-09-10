## Extension Task: Create a Character Management Program

Create a console-based program that allows the user to create and interact with multiple character objects. Your program should use a class to organize each character's data and behaviours, while `main.py` handles user input and decides which actions should occur.

This task extends the class concepts from the lesson, including properties, `__init__`, methods, multiple instances, and storing a class in its own module.    

### Program Requirements

Your program must:

* Include a `Character` class stored in a separate file named `character.py`.
* Import the `Character` class into `main.py`.
* Give every character at least **4 properties**.

  * At least **2 properties must receive their starting values through `__init__` parameters**.
  * At least **1 property** must have a default starting value set inside `__init__`**.
* Include at least **4 methods** in the `Character` class.
* Each method should have one clear responsibility rather than performing several unrelated tasks. 
* At least **2 methods must modify one or more properties**.
* At least **1 method must receive a parameter** other than `self`.
* At least **1 method must display information about the character.
* At least **1 method must call another method using `self.method_name()`**. 
* Create at least **2 separate `Character` objects** from the same class.
* The two characters must contain different property values.
* Use `input()` to allow the user to interact with the program.
* Give the user a menu containing at least **4 different commands**.
* Allow the user to select which character they want to interact with.
* Keep the program running until the user chooses an option such as `quit` or `exit`.
* Display an error message if the user enters an invalid command.
* After an action changes a character, the updated information must still be stored in that character object during the rest of the program.

### Your Design Choices

You may decide:

* What kind of characters the program represents.
* What properties each character stores.
* What actions the characters can perform.
* How the user's commands are worded.
* How information is displayed in the console.

Possible themes include RPG characters, athletes, robots, pets, racers, superheroes, or another appropriate idea of your choice.

### Example Program Structure

Your finished program could behave something like this:

```text
Choose a character:
1. Nova
2. Bolt

> 1

Nova
Health: 100
Energy: 50

Choose an action:
1. Take Damage
2. Heal
3. Use Energy
4. Show Status
5. Switch Character
6. Quit

> 1

How much damage?
> 20

Nova took 20 damage.

Choose an action:
> 4

Nova
Health: 80
Energy: 50
```

You do **not** need to recreate this example. Your program should use your own properties, methods, and behaviours.

### Submission Checklist

Before submitting, verify that your program contains:

* `main.py`
* `character.py`
* 1 `Character` class
* 4 or more properties
* 4 or more methods
* 2 or more instantiated character objects
* 4 or more user commands
* `input()` used for interaction
* A repeating menu
* A way to quit the program
* Invalid-input handling
* At least 1 method calling another method through `self`
* Character data that changes and remains changed while the program is running
* Clear variable, property, and method names


| Criteria          | Requirements                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| Class Structure   | `Character` class is correctly created in its own module and imported into `main.py`. |
| Properties        | At least 4 appropriate properties are created and stored using `self`.                |
| Methods           | At least 4 focused methods are implemented correctly.                                 |
| Object Instances  | At least 2 independent objects are created with different values.                     |
| User Interaction  | The program uses `input()` and provides at least 4 usable commands.                   |
| Program Flow      | The menu repeats correctly, allows character selection, and can be exited.            |
| Object Behaviour  | User actions correctly call methods and modify the selected object's data.            |

