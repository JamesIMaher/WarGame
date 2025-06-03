class RadarClass:
    # A radar will contain a CPT with the probabilites of detecting an aircraft at different ranges
    # The CPT will include True Positive, False Positive, True Negative, and False Negatives for each radius from the radar
    # Beacuse, the grid is not circular, we will floor the Manhattan distance to the grid square
    cpt_prob_table = {}
    #Initalizer.
    #cpt_prob_table: Definition of each radius and the probability of detection for each object. Currently we will have subs and airplanes. Land radars cannot detect subs.
    #           The max radius will be the max dimension of the grid.
    #           A future expansion would allow a directional table so that the radar is weak in different directions.
    #max_dim: Integer that is the max x or y direction of the game grid.
    def __init__(self,max_radius, start_prob, decrease_per_grid, max_dist max_dim):
        for distance in range (0, max_dist):
            if distance > max_dist: #There is no probabilty of the radar detecting at this distance
                self.cpt_prob_table[distance] = 0

