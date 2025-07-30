import random
from plot import Plot

class Grove:
    def __init__(self):
        ### Use this for final
        # self.plot_count = random.randint(3, 5)
        ### Use this for testing
        self.plot_count = 6
        self.plots = [Plot() for _ in range(self.plot_count)]
        self.vivid_lifeforce = 0
        self.primal_lifeforce = 0
        self.wild_lifeforce = 0

    def render(self):
        output = [
                    "░█▀▀░█▀▄░█▀█░█▀█░░░█▀▄░█▀█░▀█▀░█▀█░▀█▀░▀█▀░█▀█░█▀█░░░█▀█░█▀▄░█▀█░█▀▀░▀█▀░▀█▀░█▀▀░█▀▀",
                    "░█░░░█▀▄░█░█░█▀▀░░░█▀▄░█░█░░█░░█▀█░░█░░░█░░█░█░█░█░░░█▀▀░█▀▄░█▀█░█░░░░█░░░█░░█░░░█▀▀",
                    "░▀▀▀░▀░▀░▀▀▀░▀░░░░░▀░▀░▀▀▀░░▀░░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀░░░▀░░░▀░▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀",
                    "",
                    f"+-----------------------------PLOT 1----------------------------------------+"]
        for plot in self.plots:
            output.extend(plot.render())
            if plot == self.plots[-1]:
                output.append(f"+---------------------------------------------------------------------------+")
            else:
                output.append(f"+-----------------------------PLOT {plot.id + 2}----------------------------------------+")
        
        output.append("")
        output.append(f"Vivid Lifeforce Collected:  6")
        output.append(f"Primal Lifeforce Collected: 5")
        output.append(f"Wild Lifeforce Collected:   7")
        output.append("")
        return "\n".join(output)

    def upgrade(self, harvested_crop):
        t1_to_t2_chance = .25
        t2_to_t3_chance = .20
        t3_to_t4_chance = .035
        for plot in self.plots:
            for crop in plot.crops:
                if crop.id != harvested_crop.id and crop.plant != harvested_crop.plant and crop.state != 'wilted':
                    crop.t1_change = round(crop.t1_count * t1_to_t2_chance)
                    crop.t2_count += crop.t1_change
                    crop.t1_count -= crop.t1_change
                    crop.t2_change = round(crop.t2_count * t2_to_t3_chance)
                    crop.t3_count += crop.t2_change
                    crop.t2_count -= crop.t2_change
                    crop.t3_change = round(crop.t3_count * t3_to_t4_chance)
                    crop.t4_count += crop.t3_change
                    crop.t3_count -= crop.t3_change