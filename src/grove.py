import random
from plot import Plot

class Grove:
    def __init__(self):
        self.plot_count = random.randint(3, 5)
        self.plots = [Plot() for _ in range(self.plot_count)]

    def render(self):
        output = [f"+-----------------------------PLOT 1----------------------------------------+"]
        for plot in self.plots:
            output.extend(plot.render())
            output.append(f"+-----------------------------PLOT {plot.id + 1}----------------------------------------+")
        return "\n".join(output)