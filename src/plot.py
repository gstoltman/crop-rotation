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

    def wilt(self, crop):
        crop.state = 'wilted'
        crop.t1_count = 0
        crop.t2_count = 0
        crop.t3_count = 0
        crop.t4_count = 0

    def harvest(self, crop_id):
        if self.left_crop.id == crop_id:
            harvested_crop = self.left_crop
            sibling_crop = self.right_crop2
        elif self.right_crop.id == crop_id:
            harvested_crop = self.right_crop
            sibling_crop = self.left_crop
        self.wilt(harvested_crop)
        roll = random.random()
        if roll >= .6:
            self.wilt(sibling_crop)
        return harvested_crop
    