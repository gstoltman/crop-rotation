from crop import Crop
from plot import Plot
from grove import Grove

def handle_input():
    command = input("> ").strip().lower()
    return command

def update(command, state):
    if command == "quit":
        state["running"] = False
    elif command == "test":
        test_grove = Grove()
        state["grove"] = test_grove
        for test_plot in test_grove.plots:
            for test_crop in test_plot.crops:
                print(test_crop)
    elif command == "harvest":
        target_plot = state["grove"].plots[2]
        target_plot.harvest()
        for test_plot in state["grove"].plots:
            for test_crop in test_plot.crops:
                print(test_crop)
    else:
        print(f"Unknown command: {command}")

def main():
    state = {
        "running": True
    }

    while state["running"]:
        command = handle_input()
        update(command, state)

    print("game over")

if __name__ == "__main__":
    main()
