import random

class Crop:
    _id_counter = 1

    COLOR_CODES = {
        "primal": "\033[96m",
        "vivid": "\033[93m",
        "wild": "\033[95m",
        "wilted": "\033[90m",
        "reset": "\033[0m",
        "t1": "\033[90m",
        "t2": "\033[90m",
        "t3": "\033[38;5;117m",
        "t4": "\033[38;5;130m"
    }

    def __init__(self):
        self.id = Crop._id_counter
        self.plant = random.choice(["primal", "vivid", "wild"])
        # Need to playtest t1_count below to get accurate range
        self.t1_count = random.randint(12, 24)
        self.t2_count = 0
        self.t3_count = 0
        self.t4_count = 0
        self.state = 'harvestable'
        Crop._id_counter += 1

    def render(self):
        if self.state == 'wilted':
            color = Crop.COLOR_CODES.get(self.state, "")
            t1_color = Crop.COLOR_CODES.get(self.state, "")
            t2_color = Crop.COLOR_CODES.get(self.state, "")
            t3_color = Crop.COLOR_CODES.get(self.state, "")
            t4_color = Crop.COLOR_CODES.get(self.state, "")
        else:
            color = Crop.COLOR_CODES.get(self.plant, "")
            t1_color = Crop.COLOR_CODES["t1"]
            t2_color = Crop.COLOR_CODES["t2"]
            t3_color = Crop.COLOR_CODES["t3"]
            t4_color = Crop.COLOR_CODES["t4"]
        reset = Crop.COLOR_CODES["reset"]
        t1_text = f"{t1_color}T1 Seeds: {self.t1_count:<21}{reset}"
        t2_text = f"{t2_color}T2 Seeds: {self.t2_count:<21}{reset}"
        t3_text = f"{t3_color}T3 Seeds: {self.t3_count:<21}{reset}"
        t4_text = f"{t4_color}T4 Seeds: {self.t4_count:<21}{reset}"

        return [
            f"{color}Crop {f'#{self.id} {self.plant.upper():<6} ({self.state})':<20}{reset}",
            t1_text,
            t2_text,
            t3_text,
            t4_text,
        ]

    def __str__(self):
        return f"plant color: {self.plant}, plant state: {self.state}"