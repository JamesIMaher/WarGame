def cell_to_start_pix(cell_x, cell_y, cell_width, line_width):
    box_width = cell_width + line_width
    start_x = ((cell_x - 1) * box_width) + 1
    start_y = ((cell_y - 1) * box_width) + 1
    return (start_x, start_y)