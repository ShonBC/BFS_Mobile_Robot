ENPM 661 - Planning for Autonomous Robots: 
Project 2 - Point Robot BFS using Polygon Obstacle Space
Shon Cortes

Packages Used:

	1. import numpy
    2. import copy
		- Used to do deep copy of lists
    3. import cv2 
        - Used for visualization of the path planning.

Run the program:

	1. Run the program using your prefered method (terminal...)

    2. Program asks for user input for the start and goal coordinates. 
        X-coordinates must be between integer values 0 and 400.
        Y-coordinates must be between integer values 0 and 300.
        -Enter the x and y coordinates for start position seperated by a space.
        -Enter the x and y coordinates for goal position seperated by a space.


    Example:
    Enter starting x and y coordinates separated with a space: 0 0
    Enter goal x and y coordinates separated with a space: 400 300
Program Summary:
    After user provides input for start and goal coordinates, a Breadth First Search (BFS) algorithm explores the map to find a path to the goal.
    The program opens a window that shows the map being explored. The white space represents the open map area, any black space represents an obstacel. 
    As the program runs, the explored space highlights green. Once a path to the goal is found, the path is highlighted in red.