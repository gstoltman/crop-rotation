import random

class Crop:
    def __init__(self):
        self.plant = random.choice(["cyan", "yellow", "purple"])
        self.t1_count = random.randint(8, 16)
        self.t2_count = random.randint(4, 8)
        self.t3_count = 0
        self.t4_count = 0
        self.state = 'grown'

    def __str__(self):
        return f"plant color: {self.plant}, plant state: {self.state}"