import math

def cell_to_start_pix(cell_x, cell_y, cell_width, line_width):
    box_width = cell_width + line_width
    start_x = ((cell_x - 1) * box_width) + 1
    start_y = ((cell_y - 1) * box_width) + 1
    return (start_x, start_y)

#Identify all cells in the game within a Eucledian radius of the start cell. Used for radar rings
#Returns a dictionary with key tuples (x,y) and a true or false value. If the tuple is true, that cell is within the Eucledian distance.
#False is outside the Eucledian distance

def id_euclid_cells(start_x, start_y, distance, num_x_cells, num_y_cells):
    dist_dict = {}
    for x in range(1, num_x_cells):
        for y in range(1, num_y_cells):
            euclid_dist = math.sqrt((x - start_x)**2 + (y-start_y)**2)
            rounded_euclid_dist = math.floor(euclid_dist)
            if rounded_euclid_dist == distance:
                dist_dict[(x,y)] = True
            else:
                dist_dict[(x,y)] = False
    return dist_dict
