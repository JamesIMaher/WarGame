import random
import pythonGraph as pg
from util import cell_to_start_pix

class EnemyClass:
    x_pos = -1
    y_pos = -1
    max_x_cells = -1 
    max_y_cells = -1
    tile_width = -1
    line_width = -1
    start_pos_tuple = (-1, -1)

    def __init__(self, max_x_cells, max_y_cells, tile_width, line_width, x_pos = -1, y_pos = -1):
        self.max_x_cells = max_x_cells
        self.max_y_cells = max_y_cells
        self.tile_width = tile_width
        self.line_width = line_width        
    
    def draw_unit(self):
        self.start_pos_tuple = cell_to_start_pix(self.x_pos, self.y_pos, self.tile_width, self.line_width) 

    def move_unit(self, new_x_pos, new_y_pos):
        self.x_pos = new_x_pos
        self.y_pos = new_y_pos



            