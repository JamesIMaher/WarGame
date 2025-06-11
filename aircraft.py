from enemy import EnemyClass
from random import randint
from util import cell_to_start_pix
import pythonGraph as pg

class AircraftClass(EnemyClass):

    def __init__(self, max_x_cells, max_y_cells, tile_width, line_width, x_pos = -1, y_pos = -1):
        super().__init__(max_x_cells, max_y_cells, tile_width, line_width, x_pos, y_pos)

        if x_pos == -1 and y_pos == -1: #Enemy locaiton was not specified. Generate a random location
            random_x = randint(1, 10)
            
            self.x_pos = randint(1, max_x_cells)
            self.y_pos = randint(1, max_y_cells)
    
    def draw_unit(self):
        super().draw_unit()
        pg.draw_image("tiles/Forest_Tile_Plane.png", 
                      self.start_pos_tuple[0] + self.line_width - 1, 
                      self.start_pos_tuple[1] + self.line_width, 
                      self.tile_width, 
                      self.tile_width)
