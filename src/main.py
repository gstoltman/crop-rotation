import os
from crop import Crop
from plot import Plot
from grove import Grove

def handle_input(state):
    # clear_screen()
    # grove = state.get("grove")
    # print(grove.render())
    command = input("Type 1 to harvest, 2 for instructions, 3 to quit> ").strip().lower()
    return command

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def update(command, state):
    clear_screen()
    grove = state.get("grove")
    print(state["grove"].render())

    if command == "3":
        state["running"] = False

    elif command == "1":
        try:
            crop_id = int(input("Enter the Crop Number you want to harvest: "))
            if crop_id < 1 or crop_id > len(grove.plots) * 2:
                print(f"Invalid Crop ID: must be between 1 and {len(grove.plots) * 2}")
                return
            plot_id = (crop_id - 1) // 2
            harvested_crop = grove.plots[plot_id].harvest(crop_id)
            grove.upgrade(harvested_crop)

        except ValueError:
            print("Invalid input: Please enter a numeric Crop ID.")
            return

    elif command == "2":
        grove.upgrade(1)

    clear_screen()
    grove = state.get("grove")
    print(state["grove"].render())

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

if __name__ == "__main__":
    main()
