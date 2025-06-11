import pythonGraph as pg
from cpt import CPTClass
from radar import RadarClass
from util import id_euclid_cells
from aircraft import AircraftClass

def initialize_game():
    pg.clear_window("white")
    x_tile_count = 1
    y_tile_count = 1
    for x_start_pos in range(LINE_WIDTH,WINDOW_WIDTH, TILE_WIDTH + LINE_WIDTH):
        for y_start_pos in range(LINE_WIDTH,(WINDOW_HEIGHT - BUTTON_AREA), TILE_WIDTH + LINE_WIDTH):
            #Record the pixel positions of each tile
            tile_start_pos_dictionary[(x_tile_count, y_tile_count)] = (x_start_pos, y_start_pos)
            y_tile_count += 1
            if y_start_pos < (WINDOW_HEIGHT - BUTTON_AREA) / 2:
                pg.draw_image("tiles/Ocean_tile.png", x_start_pos, y_start_pos, TILE_WIDTH, TILE_WIDTH)
            else:
                pg.draw_image("tiles/Forest_tile.png", x_start_pos, y_start_pos, TILE_WIDTH, TILE_WIDTH)
        x_tile_count += 1
        y_tile_count = 1
    #Testing
    pg.draw_image("tiles/Forest_tile.png", tile_start_pos_dictionary[(1,2)][0], tile_start_pos_dictionary[(1,2)][1], TILE_WIDTH, TILE_WIDTH)
    #Create an airplane for testing
    testAirplane = AircraftClass(X_NUM_TILES, Y_NUM_TILES, TILE_WIDTH, LINE_WIDTH)
    testAirplane.draw_unit()

#Receives the x and y coordinates of a mouse click and then determine the grid position of the click
def determine_cell_coords(x,y):
    cell_width = TILE_WIDTH + LINE_WIDTH
    if (y >= WINDOW_HEIGHT - (100 + LINE_WIDTH)): #Click is located in the button area
        return (-1, -1)
    else:
        x_cell_number = (x // cell_width) + 1
        y_cell_number = (y // cell_width) + 1
        return(x_cell_number,y_cell_number)
    
#Game Setup Parameters
#These contstants can be adjusted to change the size of the game
X_NUM_TILES = 24
Y_NUM_TILES = 18
#Width of the lines between the grids
LINE_WIDTH = 3
#Width of the square cells in pixels
TILE_WIDTH = 32
#The total number of tiles in the grid programatically
TOTAL_TILES = X_NUM_TILES * Y_NUM_TILES
#Start with a prior probability so that we are not multiplying the CPT by 0
PRIOR_PROB = 1 / TOTAL_TILES
#Add some space at the bottom for buttons and text from the game
BUTTON_AREA = 100

WINDOW_WIDTH = (X_NUM_TILES * TILE_WIDTH) + ((X_NUM_TILES + 1) * LINE_WIDTH)
WINDOW_HEIGHT = (Y_NUM_TILES * TILE_WIDTH) + ((Y_NUM_TILES + 1) * LINE_WIDTH) + BUTTON_AREA

#Initalize a dictionary of start postions. The key will be a tuple of the x and y cell position. The value will be a tuple of the pixel position
tile_start_pos_dictionary = {} 
#Initialize the CPT Object
current_cpt = CPTClass(PRIOR_PROB, X_NUM_TILES, Y_NUM_TILES)

#Ok, let's see if we can build a grid

pg.open_window(WINDOW_WIDTH,WINDOW_HEIGHT)
pg.set_window_title("WarGames - An AI Training Environment")


initialize_game()

#Test adding a radar site
testRadar = RadarClass(start_prob=0, 
                       decrease_per_grid=0.1, 
                       max_dist=5, 
                       max_x_cells=X_NUM_TILES, 
                       max_y_cells=Y_NUM_TILES, 
                       line_width=LINE_WIDTH, 
                       cell_width=TILE_WIDTH)
test_dist_dict = id_euclid_cells(testRadar.radar_position_x, testRadar.radar_position_y, 2, X_NUM_TILES, Y_NUM_TILES) 
#Try tiling everything with Ocean Tiles
while pg.window_not_closed():
    if(pg.mouse_button_pressed("LEFT")):
        initialize_game()
        x_click = pg.get_mouse_x()
        y_click = pg.get_mouse_y()
        position_tuple = determine_cell_coords(x_click, y_click)
        output_string = "The X grid position is: " + str(position_tuple[0]) + " and the Y grid position is: " + str(position_tuple[1])
        pg.draw_text(output_string, 50, WINDOW_HEIGHT - 50, "BLACK")
    testRadar.color_cells(TILE_WIDTH, test_dist_dict)
    pg.update_window()


