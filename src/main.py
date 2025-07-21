def handle_input():
    command = input("> ").strip().lower()
    return command

def update(command, state):
    if command == "quit":
        state["running"] = False
    else:
        print(f"Unknown command: {command}")

def main():
    state = {
        "running" = True
    }

    while state["running"]:
        command = handle_input()
        update(command, state)

    print("game over")

if __name__ == "__main__":
    main()
