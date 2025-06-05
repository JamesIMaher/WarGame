import pythonGraph as pg
from util import cell_to_start_pix

class RadarClass:
    # A radar will contain a CPT with the probabilites of detecting an aircraft at different ranges
    # The CPT will include True Positive, False Positive, True Negative, and False Negatives for each radius from the radar
    # Beacuse, the grid is not circular, we will floor the Manhattan distance to the grid square
    cpt_prob_table = {}
    max_x_cells = -1
    max_y_cells = -1
    max_dist = -1
    radar_position_x = -1
    radar_position_y = -1
    line_width = -1
    cell_width = -1

    #Initalizer.
    #cpt_prob_table: Definition of each radius and the probability of detection for each object. Currently we will have subs and airplanes. Land radars cannot detect subs.
    #           The max radius will be the max dimension of the grid.
    #           A future expansion would allow a directional table so that the radar is weak in different directions.
    #max_dim: Integer that is the max x or y direction of the game grid.
    def __init__(self, start_prob, decrease_per_grid, max_dist, max_x_cells, max_y_cells, line_width, cell_width):
        self.max_x_cells = max_x_cells
        self.max_y_cells = max_y_cells
        self.max_dist = max_dist
        self.line_width = line_width
        self.cell_width = cell_width
        
        for distance in range (0, max_dist):
            if distance > max_dist: #There is no probabilty of the radar detecting at this distance
                self.cpt_prob_table[distance] = 0
            else: #Distance should receive the prior probability
                self.cpt_prob_table[distance] = start_prob - (decrease_per_grid * distance)
    
    def color_cells(self, x_cell, y_cell, tile_width):
        start_pos_tuple = cell_to_start_pix(x_cell, y_cell, self.cell_width, self.line_width)
        for distance in range(1, self.max_dist):
            if distance == 1:
                pg.draw_image("tiles/Ocean_tile.png", start_pos_tuple[0], start_pos_tuple[1], tile_width, tile_width)

