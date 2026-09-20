from character import Character

character1 = Character("Nova", "Warrior")
character2 = Character("Bolt", "Mage")

character = character1

while True:
    print("\nCurrent Character:", character.name)
    print("1. Take Damage")
    print("2. Heal")
    print("3. Use Energy")
    print("4. Level Up")
    print("5. Show Status")
    print("6. Switch Character")
    print("7. Quit")

    choice = input("Choose an action: ")

    if choice == "1":
        damage = int(input("How much damage? "))
        character.take_damage(damage)

    elif choice == "2":
        amount = int(input("How much do you want to heal? "))
        character.heal(amount)

    elif choice == "3":
        amount = int(input("How much energy do you want to use? "))
        character.use_energy(amount)

    elif choice == "4":
        character.level_up()

    elif choice == "5":
        character.show_status()

    elif choice == "6":
        if character == character1:
            character = character2
        else:
            character = character1

        print("Switched to", character.name)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid command.")