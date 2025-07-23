import random

class Crop:
    _id_counter = 1

    COLOR_CODES = {
        "primal": "\033[96m",
        "vivid": "\033[93m",
        "wild": "\033[95m",
        "reset": "\033[0m"
    }

    def __init__(self):
        self.id = Crop._id_counter
        self.plant = random.choice(["primal", "vivid", "wild"])
        self.t1_count = random.randint(8, 16)
        self.t2_count = random.randint(4, 8)
        self.t3_count = 0
        self.t4_count = 0
        self.state = 'harvestable'
        Crop._id_counter += 1

    def render(self):
        color = Crop.COLOR_CODES.get(self.plant, "")
        reset = Crop.COLOR_CODES["reset"]

        return [
            f"{color}Crop {f'#{self.id} {self.plant.upper():<6} ({self.state})':<20}{reset}",
            f"{color}{f'T1 Seeds: {self.t1_count}':<20}{reset}",
            f"{color}{f'T2 Seeds: {self.t2_count}':<20}{reset}",
            f"{color}{f'T3 Seeds: {self.t3_count}':<20}{reset}",
            f"{color}{f'T4 Seeds: {self.t4_count}':<20}{reset}",
        ]

    def __str__(self):
        return f"plant color: {self.plant}, plant state: {self.state}"