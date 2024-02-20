#!/usr/bin/env python3 
"""Draw a sankey diagram using data from a given input file.

    Modified by : 20021899
    Date: 16/3/2022

    Contains: 
    Section 1-7
    Challenge Question 2
"""

import sys
from ezgraphics import GraphicsWindow

##### Constants #####
WIDTH = 1000        # Width of the window in pixels
HEIGHT = 700        # Height of the window in pixels
GAP = 30            # Gap between disagram arrows in pixels
REC_X_POS = 300     # X position of rectangle
REC_Y_POS = 100     # Y position of rectangle
REC_LENGTH = 400    # Length of rectangle

COLOURS = [(230, 25, 75), (60, 180, 75), (255, 225, 25), (0, 130, 200),
(245,	130,	48),	(145,	30, 180), (70, 240,	240),	(240, 50, 230),
(210,	245,	60),	(250,	190, 212), (0, 128,	128),	(220, 190, 255),
(170, 110, 40), (255, 250, 200), (128, 0, 0), (170, 255, 195),
(128,	128,	0), (255, 215, 180), (0, 0, 128), (128, 128, 128)]

##### Function defined #####
def read_file(file_name):
    """Opens and reads the file. Returns the title, left-hand axis label and 
    the data values in the file.

    Args:
        file_name (str): file containing the data.

    Raises:
        FileNotFoundError: If file not found or is not readable, 
                            this exception is raised

    Returns:
        str(title): diagram title
        str(axis_label): left-hand axis label
        list(data_list): Each element contains one line of data from the file
    """
    # read text file
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
        graph_title (str): title for the window
        
    Returns:
        GraphicsWindow(win): reference to the window
    """
    # set up graph window to variable "win"
    win = GraphicsWindow(WIDTH, HEIGHT)
    # set graph title
    win.setTitle(graph_title)
    return win

def parse_value (str) :
    """Parses and returns a floating point value from a string, cleaning required characters (e.g. white spaces).
       
    Args:
        str: string from which the value must be read

    Raises: 
        ValueError: raised if the string cannot be read as a float, datailing content and line number    

    Returns:
        list (split_list): the processed list
    """

    # cleaning required characters
    replace_str = str.replace(" ", "")
    replace_str = replace_str.replace("\n", "")
    split_list = replace_str.split(',')

    return split_list


def process_data(data_list) :
    """Returns a dictionary produced by processing the data in the list. 

    Args:
        data_list (list): list containing the data read from the file

    Raises:
        ValueError: raised if there are errors in the data values in the file

    Returns:
        dictionary (data_dictionary): the data dictionary contains:
                                         the key value of its name and values
    """

    # initialize line number
    line_number = 2
    # create list to store value
    data_dictionary = {}

    for n in data_list:
        try:
            # extract value from function parse_value
            split_list = parse_value(n)

            # dict values number and name
            if "." in split_list[1]:
                values = list(map(float, split_list[1:]))
            else:
                values = list(map(int, split_list[1:]))
            data_dictionary[split_list[0]] = values
            line_number += 1        

        # if error, print its type and line number
        except ValueError as error:
            print(f"Error in Line {line_number} : Value provided is not a number.")  
            print(error)
            return     

    return data_dictionary



def draw_triangle(draw, border_size, cal_pixels, keys, i, r, g, b):
    """Draw the triangle

    Args:
        draw (GraphicsWindow): contains the graph
        gap_size (int): number of pixels to leave between destination arrows
        border_size (int): Minimum separation to other edges of the window
        keys (str): name of each factor
        i (int): count number of loops
        r, g, b (int): RGB color value
    """

    # set triangle colors
    draw.setFill(r, g, b)
    # draw triangle
    draw.drawPolygon(border_size, 550, border_size + cal_pixels, 550, 
                    border_size + cal_pixels/2, 600)
    # set text color
    draw.setColor(255 - r, 255 - g, 255 - b)
    # draw text from the i-th element in keys
    draw.drawText(border_size + cal_pixels/3 - 10, 550, keys[i])


def draw_connected_line(draw, border_size, cal_pixels, pos, pos_upper, pos_x1, r, g, b):
    """Draw the connection between: diagram

    Args:
        draw (canvas): draw on the graph
        border_size (int): Minimum separation to other edges of the window
        cal_pixels (int): The longest side of a triangle
        pos (float): position value
        pos_upper (float): another position value
        pos_x1 (float): position value for calculation
        r, g, b (int):  RGB color value

    Return:
        the graph
    """
    # initialize variables
    y = 0
    x1 = 0
    x2 = 0
    # assign new variables with given value 
    r_new = r
    g_new = g
    b_new = b

    # calculate gradual progress of the position
    x_1 = (pos_x1 - border_size) / 400
    x_2 = (REC_X_POS + pos + pos_upper - border_size - cal_pixels) / 400

    # for loop in range 400 to fill the -
    # - connection between rectangle and triangle with lines
    for i in range(400):
        # assign color to the line
        r_new, g_new , b_new = draw_connected_color(draw, r_new, g_new , b_new, r, g, b)
        # draw lines
        draw.drawLine(border_size + x1, 550 - y, border_size + cal_pixels + x2, 550 - y)
        x2 += x_2
        x1 += x_1
        y += 1
    return



def draw_connected_color(draw, r_new, g_new , b_new, r, g, b):

    """change the color of each line

    Args:
        draw (canvas): draw on the graph
        n (list): RGB color value
        r_new, g_new , b_new (float): RGB color value due to be processed
        r, g, b (int): RBG color value 
    returns:
        r_new, g_new , b_new (float): RGB color value due to be processed
    """


    # change RGB color value
    r_new -= r / 400
    g_new -= g / 400
    b_new -= b / 400

    # turn float to interger
    r_int = int(r_new)
    g_int = int(g_new)
    b_int = int(b_new)

    draw.setColor(r_int, g_int, b_int)

    return r_new, g_new, b_new

def assigned_color(n, each_flow_width):

    """assign color to each factor that needs to be draw

    Args:
        n (list): pre-set RGB color value
        each_flow_width (list): a list extracted from data_dic contains values assigned to each key
    returns:
        r, g, b (int): processed (changed) r, g, b value
    """

    # assign color value from the list
    color = each_flow_width[1:]

    # condition to make a distinction of what color needs to be assigned
    # assign color by default
    if len(color) == 0:
        r = n[0]
        g = n[1]
        b = n[2]

    # assign color by different position required
    if len(color) == 1:
        color_no = color[0] - 1
        color_value = COLOURS[color_no]
        r = color_value[0]
        g = color_value[1]
        b = color_value[2]

    # assign color by given RGB value
    if len(color) == 3:
        r = color[0]
        g = color[1]
        b = color[2]

    return r, g, b
    

def draw_rectangle(draw, title):

    """draw rectangle

    Args:
        draw (canvas): draw on the graph
        title (str): diagram title
    returns:
        draw graph
    """
    
    # draw rectangle by setting color, position
    draw.setFill("black")
    draw.drawRectangle(REC_X_POS, REC_Y_POS, REC_LENGTH, 50)
    # draw text by setting color, position
    draw.setColor("white")
    draw.drawText(480, 115, title)
    return 


def draw_sankey(window, title, data_dic, gap_size, border_size):
    """Draw the sankey diagram

    Args:
        window (GraphicsWindow): contains the graph
        title (string): contains the label to overlay on the source arrow
        data_dic (dictionary): contains the data for the graph
        gap_size (int): number of pixels to leave between destination arrows
        border_size (int): Minimum separation to other edges of the window
    returns:
        the draw graph
    """
    # calculate each variable
    keys = list(data_dic.keys())
    sum_list = [sum(value) for value in zip(*data_dic.values())]
    total_float = sum_list[0]
    flow_width = list(data_dic.values())
    total_pixels = ((WIDTH - 2 * 100 - (len(data_dic) - 1) * gap_size)/total_float)
    pos = REC_LENGTH / len(data_dic)
    
    # initializing values
    cal_pixels = 0
    i = 0
    pos_upper = 0
    pos_x1 = 300

    # set up canvas and draw rectangle
    draw = window.canvas()
    draw_rectangle(draw, title)

    # draw triangle and lines connect triangle with rectangel
    for n in COLOURS:
        if i < len(data_dic):
            each_flow_width = flow_width[i]
            cal_pixels =  total_pixels * each_flow_width[0]
            r, g, b = assigned_color(n, each_flow_width)
            draw_triangle(draw, border_size, cal_pixels, keys, i, r, g, b)
            draw_connected_line(draw, border_size, cal_pixels, pos, pos_upper, pos_x1, r, g, b)
            border_size = border_size + gap_size + cal_pixels
            pos_upper = pos + pos_upper
            pos_x1 += pos
            i += 1
        else:
            return

##### Deprecated functions (duplication of functions) #####
def draw_connection(draw, data_dic, gap_size, border_size, cal_pixels):
    """Draw the polygonal

    Args:
        draw (GraphicsWindow): contains the graph
        data_dic (dictionary): contains the data for the graph
        gap_size (int): number of pixels to leave between destination arrows
        border_size (int): Minimum separation to other edges of the window
        cal_pixels (int): The longest side of a triangle
    returns:
        the draw graph
    """
    # initializing values
    i = 0
    pos = REC_LENGTH / len(data_dic)
    pos_upper = 0

    # loop to travel n times to draw the graph
    for n in COLOURS:
        if i < len(data_dic):
            draw.drawPolygon(REC_X_POS + pos_upper, 150, 
                        REC_X_POS + pos + pos_upper, 150, 
                        border_size + cal_pixels, 550,
                        border_size, 550)
            pos_upper = pos + pos_upper
            border_size = border_size + gap_size + cal_pixels
            i += 1
        else:
            return 
          
##### Main Program #####
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