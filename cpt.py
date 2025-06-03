class CPTClass:
    #Dictionary containing the Conditional Probability Table for each grid. This will update based on observations and past probabilities 
    cpt_table = {}

    #Setup the game's initial CPT state with the prior probability (usually 1 / the number of tiles in the game)
    def __init__(self, prior_probability, x_tiles, y_tiles):
        #Initialize the cpt_table with the prior probabilities. Creates a dictionary that is the size of the game board
        for x in range(1, x_tiles):
            for y in range(1, y_tiles):
                self.cpt_table[(x,y)] = prior_probability
