import random
from crop import Crop

class Plot:
    def __init__(self):
        self.left_crop = Crop()
        self.right_crop = Crop()

    def harvest(self, crop_number):
        
        self.left_crop.state = 'wilted'
        self.left_crop.t1_count = 0
        self.left_crop.t2_count = 0
        self.left_crop.t3_count = 0
        self.left_crop.t4_count = 0
        self.right_crop.state = "upgraded"
        self.right_crop.amount = self.right_crop.amount + 200
    
