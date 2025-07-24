import random
from crop import Crop

class Plot:
    _id_counter = 0

    def __init__(self):
        self.id = Plot._id_counter
        self.crops = []
        self.left_crop = Crop()
        self.right_crop = Crop()
        self.crops.append(self.left_crop)
        self.crops.append(self.right_crop)
        Plot._id_counter += 1

    def render(self):
        left_lines = left_lines = self.left_crop.render()
        right_lines = self.right_crop.render()
        return [f"{l:<40} | {r:<40}" for l, r in zip(left_lines, right_lines)]

    def harvest(self, crop_id):
        if self.left_crop.id == crop_id:
            harvested_crop = self.left_crop
            sibling_crop = self.right_crop
        elif self.right_crop.id == crop_id:
            harvested_crop = self.right_crop
            sibling_crop = self.left_crop
        harvested_crop.state = 'wilted'
        harvested_crop.plant = 'wilted'
        harvested_crop.t1_count = 0
        harvested_crop.t2_count = 0
        harvested_crop.t3_count = 0
        harvested_crop.t4_count = 0
        # handle sibling living
        sibling_crop.t1_count = sibling_crop.t1_count + 200
    