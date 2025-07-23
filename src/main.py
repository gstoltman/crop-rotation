import os
from crop import Crop
from plot import Plot
from grove import Grove

def handle_input(state):
    clear_screen()
    grove = state.get("grove")
    print(grove.render())
    command = input("Type 1 to harvest, 2 for instructions, 3 to quit> ").strip().lower()
    return command

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def update(command, state):
    clear_screen()

    grove = state.get("grove")

    print(state["grove"].render())

    if command == "quit":
        state["running"] = False

    elif command == "1":
        try:
            crop_id = int(input("Enter the Crop Number you want to harvest: "))
            grove.plot.harvest(crop_id)
        except ValueError:
            print("Invalid input: Please enter a numeric Crop ID.")
            return
        for plot in grove.plots:
            crop_ids = [plot.left_crop.id, plot.right_crop.id]
            if crop_id in crop_ids:
                plot.harvest(crop_id)
                print(f"Harvested crop ID #{crop_id} in Plot.")
                break
        else:
            print(f"No crop found with ID {crop_id}.")
    else:
        print(f"Unknown command: {command}")

def main():
    state = {
        "running": True,
        "grove": Grove()
    }

    clear_screen()  # optional: makes the output clean
    print(state["grove"].render())  # display the grove before the first command

    while state["running"]:
        command = handle_input(state)
        update(command, state)

    print("game over")

if __name__ == "__main__":
    main()
