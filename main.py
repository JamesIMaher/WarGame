import pythonGraph as pg

#Game Setup Parameters
X_NUM_TILES = 24
Y_NUM_TILES = 18
LINE_WIDTH = 3
TILE_WIDTH = 32

WINDOW_WIDTH = (X_NUM_TILES * TILE_WIDTH) + ((X_NUM_TILES + 1) * LINE_WIDTH)
WINDOW_HEIGHT = (Y_NUM_TILES * TILE_WIDTH) + ((Y_NUM_TILES + 1) * LINE_WIDTH)

#Initalize a dictionary of start postions. The key will be a tuple of the x and y cell position. The value will be a tuple of the pixel position
tile_start_pos_dictionary = {} 

#Ok, let's see if we can build a grid

pg.open_window(WINDOW_WIDTH,WINDOW_HEIGHT)
pg.set_window_title("WarGames - An AI Training Environment")
pg.clear_window("white")

#Try tiling everything with Ocean Tiles
x_tile_count = 1
y_tile_count = 1
for x_start_pos in range(LINE_WIDTH,WINDOW_WIDTH, TILE_WIDTH + LINE_WIDTH):
    for y_start_pos in range(LINE_WIDTH,WINDOW_HEIGHT, TILE_WIDTH + LINE_WIDTH):
        #Record the pixel positions of each tile
        tile_start_pos_dictionary[(x_tile_count, y_tile_count)] = (x_start_pos, y_start_pos)
        y_tile_count += 1
        if y_start_pos < WINDOW_HEIGHT / 2:
            pg.draw_image("tiles/Ocean_tile.png", x_start_pos, y_start_pos, TILE_WIDTH, TILE_WIDTH)
        else:
            pg.draw_image("tiles/Forest_tile.png", x_start_pos, y_start_pos, TILE_WIDTH, TILE_WIDTH)
    x_tile_count += 1
    y_tile_count = 1
#Testing
pg.draw_image("tiles/Forest_tile.png", tile_start_pos_dictionary[(1,2)][0], tile_start_pos_dictionary[(1,2)][1], TILE_WIDTH, TILE_WIDTH)
pg.update_window()

pg.wait_for_close()