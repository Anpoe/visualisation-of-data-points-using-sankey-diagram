#!/usr/bin/env python3 
"""Draw a sankey diagram using data from a given input file.
"""
import sys
from ezgraphics import GraphicsWindow

WIDTH = 1000        # Width of the window in pixels
HEIGHT = 700        # Height of the window in pixels
GAP = 50            # Gap between disagram arrows in pixels
REC_X_POS = 300
REC_Y_POS = 100
REC_LENGTH = 400

COLOURS = [(230, 25, 75), (60, 180, 75), (255, 225, 25), (0, 130, 200),
(245,	130,	48),	(145,	30, 180), (70, 240,	240),	(240, 50, 230),
(210,	245,	60),	(250,	190, 212), (0, 128,	128),	(220, 190, 255),
(170, 110, 40), (255, 250, 200), (128, 0, 0), (170, 255, 195),
(128,	128,	0), (255, 215, 180), (0, 0, 128), (128, 128, 128)]


def read_file(file_name):
    """Opens and reads the file. Returns the title, left-hand axis label and 
    the data values in the file.

    Args:
        file_name (str): file containing the data.

    Raises:
        FileNotFoundError: If file not found or is not readable, 
                            this exception is raised

    Returns:
        str: diagram title
        str: left-hand axis label
        list: Each element contains one line of data from the file
    """
    with open(file_name) as f:
        data = f.readlines()
        title = data[0]
        axis_label = data[1] 
        data_list = data[2:]
    return title, axis_label, data_list

def set_up_graph(graph_title):
    """Creates a window and canvas. Displays the title, left-hand axis label.
    Returns a reference to the window. 

    Args:
        title (str): title for the window
        
    Returns:
        GraphicsWindow: reference to the window
    """
    win = GraphicsWindow(WIDTH, HEIGHT)
    win.setTitle(graph_title)
    return win

def parse_value (str) :
    """Parses and returns a floating point value from a string, cleaning required characters (e.g. white spaces).
       
    Args:
        str: string from which the value must be read
        line_number: line in the file, required in case errors need to be notified
        
    Raises: 
        ValueError: raised if the string cannot be read as a float, datailing content and line number    
    Returns:
        float: The number read        
    """
    number = []
    name = []
    line_number = 2
    
    for list in str:
        
        try:
            replace_str = list.replace(" ", "")
            replace_str = replace_str.replace("\n", "")
            split_list = replace_str.split(',')
            name.append(split_list[0])
            number.append(float(split_list[1]))
            line_number += 1
        except ValueError as error:
            print(f"Error in Line {line_number} : Value provided is not a number.")  
            print(error)
            return     

        
    return number, name


def process_data(data_list) :
    """Returns a dictionary produced by processing the data in the list. 

    Args:
        data_list (list): list containing the data read from the file

    Raises:
        ValueError: raised if there are errors in the data values in the file

    Returns:
        dictionary: contains data about the flows
    """

    name, number= parse_value(data_list)
    data_dictionary = dict(zip(number, name))
    return data_dictionary 

def draw_triangle(draw, data_dic, gap_size, border_size):
    """Draw the triangle

    Args:
        window (GraphicsWindow): contains the graph
        data_dic (dictionary): contains the data for the graph
        gap_size (int): number of pixels to leave between destination arrows
        border_size (int): Minimum separation to other edges of the window
    returns:
        draw: graph
    """
    keys = list(data_dic.keys())
    i = 0
    pos = REC_LENGTH / len(data_dic)
    cal_pixels = (WIDTH - 2 * 100 - (len(data_dic) - 1) * gap_size)/len(data_dic)

    for n in COLOURS:
        if i < len(data_dic):
            draw.setFill(n[0], n[1], n[2])
            draw.drawPolygon(border_size, 550, border_size + cal_pixels, 550, 
                            border_size + cal_pixels/2, 600)
            draw.setColor(255 - n[0], 255 - n[1], 255 - n[2])
            draw.drawText(border_size + cal_pixels/3 - 10, 550, keys[i])
            border_size = border_size + gap_size + cal_pixels
            i += 1
        else:
            return cal_pixels

def draw_connection(draw, data_dic, gap_size, border_size, cal_pixels):

    i = 0

    pos = REC_LENGTH / len(data_dic)
    pos_upper = 0
    for n in COLOURS:
        if i < len(data_dic):
            draw_connected_color(draw, border_size, cal_pixels, n)
            draw.drawPolygon(REC_X_POS + pos_upper, 150, 
                        REC_X_POS + pos + pos_upper, 150, 
                        border_size + cal_pixels, 550,
                        border_size, 550)
            pos_upper = pos + pos_upper
            border_size = border_size + gap_size + cal_pixels
            i += 1
        else:
            return 

def draw_connected_color(draw, border_size, cal_pixels, n):

    y = 0
    x = 0
    X = 200 / 400
    for i in range(400):
        draw.setColor(n[0], n[1], n[2])
        draw.drawLine(border_size + x, 550 - y, 
        border_size + cal_pixels + x, 550 - y)
        x += X
        y = y + 1
    return


def draw_sankey(window, title, data_dic, gap_size, border_size):
    """Draw the sankey diagram

    Args:
        window (GraphicsWindow): contains the graph
        title (string): contains the label to overlay on the source arrow
        data_dic (dictionary): contains the data for the graph
        gap_size (int): number of pixels to leave between destination arrows
        border_size (int): Minimum separation to other edges of the window
    """
    draw = window.canvas()
    draw.setFill("black")
    draw.drawRectangle(REC_X_POS, REC_Y_POS, REC_LENGTH, 50)
    draw.setColor("white")
    draw.drawText(480, 115, title)
    cal_pixels = draw_triangle(draw, data_dic, gap_size, border_size)
    draw_connection(draw, data_dic, gap_size, border_size, cal_pixels)

    return
          

def main():
    # DO NOT EDIT THIS CODE
    input_file = ""
    file_read = False
    # Try to read file name from input commands:
    args = sys.argv[1:]  
    if len(args) == 0 or len(args) > 1:
        print('\n\nUsage\n\tTo visualise data using a sankey diagram type:\
            \n\n\t\tpython sankey.py infile\n\n\twhere infile is the name of the file containing the data.\n')
        print('\nWe will ask you for a filename, as no filename was provided')    
       
    else:
        input_file = args[0]
    
    # Use file provided or ask user for valid filename (we will iterate until a valid file is provided)
    while not file_read :
        # Ask for filename if not available yet
        if input_file == "" :
            input_file = input("Provide name of the file to load: ")
        
        # Try to Read the file contents
        try:
            title, left_axis_label, data_list = read_file(input_file)
            file_read = True
        except FileNotFoundError:
            print(f"File {input_file} not found or is not readable.")
            input_file = ""
            

    # Section 2: Create a window and canvas
    win = set_up_graph(title)

    # Section 3: Process the data
    try:
        data_dic = process_data(data_list)
    except ValueError as error:
        print("Content of file is invalid: ")
        print(error)
        return

    # Section 4: Draw the graph
    draw_sankey(win, left_axis_label, data_dic, GAP, 100)

    win.wait()


if __name__ == "__main__":
    main()