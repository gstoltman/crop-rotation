import random
from plot import Plot

class Grove:
    def __init__(self):
        self.plot_count = random.randint(3, 5)
        self.plots = [Plot() for _ in range(plot_count)]

        for plot in range(self.plot_count):
            self.plots.append(Plot())