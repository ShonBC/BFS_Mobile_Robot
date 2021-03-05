import numpy as np
import copy
import cv2

map = 255*np.ones([301, 401, 3], dtype = np.uint8)

def obstacles_chk(node): # Check if position is in obstacle space.
   
    # Rectangle 
    if node[1] >= (node[0] * 0.7) + 74.39 and node[1] <= (node[0] * 0.7) + 98.568 and node[1] >= (node[0] * -1.428) + 176.554 and node[1] <= (node[0] * -1.428) + 438.068:
        return True

    # Circle
    elif (node[0] - 90)**2 + (node[1] - 70)**2 <= 35**2:
        return True

    # Elipse
    elif ((node[0] - 246)**2)/(60**2) + ((node[1] - 145)**2)/(30**2) <= 1:
        return True
    
    # 3 section Rectangular Area
    elif node[0] >= 200 and node[0] <= 210 and node[1] >= 230 and node[1] <= 280: # First section
        return True
    elif node[0] >= 210 and node[0] <= 230 and node[1] >= 270 and node[1] <= 280: # Second section
        return True
    elif node[0] >= 210 and node[0] <= 230 and node[1] >= 230 and node[1] <= 240: # Third section
        return True
    
    # Irregular Polygon
    elif node[1] >= node[0] - 265 and node[1] >= -node[0] + 391 and node[1] <= 1.03 * node[0] - 188.33 and node[1] <= -0.24 * node[0] + 223.45 and node[1] <= - 0.815 * node[0] + 426.44:
        return True
    elif node[0] <= 381 and node[1] <= 1.22 * node[0] - 294.67 and node[1] >= -0.815 * node[0] + 426.44:
        return True
 
    else:
        return False

# def obstacles_chk_test(node): # Check if position is in TEST MAP obstacle space.
#
#     # Square
#     if node[0]>=90 and node[0]<= 110 and node[1]>=40 and node[1]<=60:
#         return True
#
#     # Circle
#     if (node[0]-160)**2+(node[1]-50)**2 <= 15**2:
#         return True
#
#     else:
#         return False

def move_up(node): # Move point_bot up. Takes current node state.
    x_1 = node[0]
    y_1 = node[1] + 1

    move = 'up'

    child_node = [x_1, y_1, parent_index]
    return child_node, move

def move_up_right(node): # Move point_bot diagonally up, right. Takes current node state.
    x_1 = node[0] + 1
    y_1 = node[1] + 1

    move = 'up_right'

    child_node = [x_1, y_1, parent_index]
    return child_node, move

def move_right(node): # Move point_bot right. Takes current node state.
    x_1 = node[0] + 1
    y_1 = node[1]

    move = 'right'
    
    child_node = [x_1, y_1, parent_index]
    return child_node, move

def move_down_right(node): # Move point_bot diagonally down, right. Takes current node state.
    x_1 = node[0] + 1
    y_1 = node[1] - 1

    move = 'down_right'
    
    child_node = [x_1, y_1, parent_index]
    return child_node, move

def move_down(node): # Move point_bot down. Takes current node state.
    x_1 = node[0]
    y_1 = node[1] - 1

    move = 'down'
    
    child_node = [x_1, y_1, parent_index]
    return child_node, move

def move_down_left(node): # Move point_bot diagonally down, left. Takes current node state.
    x_1 = node[0] - 1
    y_1 = node[1] - 1

    move = 'down_left'

    child_node = [x_1, y_1, parent_index]
    return child_node, move

def move_left(node): # Move point_bot left. Takes current node state.
    x_1 = node[0] - 1
    y_1 = node[1]

    move = 'left'

    child_node = [x_1, y_1, parent_index]
    return child_node, move

def move_up_left(node): # Move point_bot diagonally up, left. Takes current node state.
    x_1 = node[0] - 1
    y_1 = node[1] + 1

    move = 'up_left'

    child_node = [x_1, y_1, parent_index]
    return child_node, move

def str_state(node): # Create row-wise string of node
    x = ""
    for i in range(len(node) - 1):
        x += str(node[i]) + ", "
    return x

def move_check(child_node, move): # Check if the move is allowed. If it is, add the child node to the visited_list and children_nodes list
    child_node = copy.deepcopy(child_node)

    # Check if out of puzzle boundary
    if child_node[0] < 0 or child_node[1] < 0 or child_node[0] >= map.shape[1] or child_node[1] >= map.shape[0]:
        return

    # Check if obstacle
    elif obstacles_chk(child_node):
        return

    # Check if child node has been visited before
    try:
        visited_list.index([child_node[0], child_node[1]])

    except ValueError:
        
        # Add child to visited and parent nodes list
        visited_list.append([child_node[0], child_node[1]])
        
        parent_nodes.append(child_node)
        child_node[2] = parent_index
        children_nodes.append(child_node)
        # print(move) # For debugging
    else:
        return

def BFS(start_node): # Bredth First Search Path Planning
    global open_nodes, parent_index
    
    count = 0

    while len(open_nodes) != 0:
        count += 1
        for i in range(len(open_nodes)):
            
            parent_node = copy.deepcopy(open_nodes.pop())
            parent_index = visited_list.index([parent_node[0], parent_node[1]])
            parent_node[2] = parent_index
                        
            child_node, move = move_up(parent_node)
            move_check(child_node, move)
            child_node, move = move_up_right(parent_node)
            move_check(child_node, move)
            child_node, move = move_right(parent_node)
            move_check(child_node, move)
            child_node, move = move_down_right(parent_node)
            move_check(child_node, move)
            child_node, move = move_down(parent_node)
            move_check(child_node, move)
            child_node, move = move_down_left(parent_node)
            move_check(child_node, move)
            child_node, move = move_left(parent_node)
            move_check(child_node, move)
            child_node, move = move_up_left(parent_node)
            move_check(child_node, move)

        cv2.imshow("map", map)

        # Check if goal is in visited list
        try:
            visited_list.index([goal_node[0],goal_node[1]])
        except ValueError:
            for i in range(len(children_nodes)):
                visualize_BFS(children_nodes)
                open_nodes.append(children_nodes.pop())

        else:
            print("Goal state found!")
            break

        # Refresh rate in ms
        i = cv2.waitKey(10)

        # Condition to break the while loop
        if i == 27:
            break

    cv2.imshow("map", map)

    try:
            visited_list.index([goal_node[0],goal_node[1]])
    except ValueError:
        print("Goal not found :[")   
             

def backtrack(parent_nodes): # Backtrack a path from goal to start position.

    path = []
    id = visited_list.index([goal_node[0], goal_node[1]])
    path.append(parent_nodes[id])
    node = parent_nodes[id]
    id = node[2]

    while id > 0:

        path.append(parent_nodes[id])
        node = parent_nodes[id]
        id = node[2]
    path.append(parent_nodes[id])
    return path
    
def begin(): # Ask for user input of start and goal pos. Start and goal much be positive integers
    while True:
        
        start_x, start_y = input("Enter starting x and y coordinates separated with a space: ").split()
        goal_x, goal_y = input("Enter goal x and y coordinates separated with a space: ").split()
        
        start_node = [int(start_x), int(start_y), parent_index]
        goal_node = [int(goal_x), int(goal_y)]

        # Check if obstacle
        if obstacles_chk(start_node):
            print("Start position is in an obstacle.")
        elif obstacles_chk(goal_node):
            print("Goal position is in an obstacle.")

        # Check if values are positive and within the map
        elif start_node[0] < 0 or start_node[1] < 0 or start_node[0] > map.shape[1] or start_node[1] > map.shape[0]:
            print("Please enter positive integer values (0 <= x <= 400, 0 <= y <= 300).")
        elif goal_node[0] < 0 or goal_node[1] < 0 or goal_node[0] > map.shape[1] or goal_node[1] > map.shape[0]:
            print("Please enter positive integer values (0 <= x <= 400, 0 <= y <= 300).")

        else:
            break
    return start_node, goal_node

def visualize_BFS(node):
    
    for i in range(len(node)):
        point = node[i]
        map[point[1]][point[0]] = [0, 255, 0]

def visualize_path(node): 
    
    while len(node) != 0:
        point = node.pop()
        map[point[1]][point[0]] = [0, 0, 255]

    cv2.imshow("Map", map)

if __name__ == "__main__":

    # Define BFS parameters for storing the queue, parent/children information, and initialize map
    open_nodes = []
    children_nodes = []
    parent_nodes = []
    parent_index = 0
    for i in range(len(map)): # Initialize map obstacles
        for j in range(len(map[i])):
            point = j, i 
            if obstacles_chk(point):
                map[i][j] = 0
    
    

    # Ask for user input of start and goal pos. Start and goal much be positive integers
    start_node, goal_node = begin()

    open_nodes.append(start_node)
    parent_nodes.append(start_node)
    visited_list = [[start_node[0], start_node[1]]]

    # Call BFS planner and backtrack the path from the goal to start position
    BFS(start_node)
    path = backtrack(parent_nodes)

    # Visualization 
    visualize_path(path)

    # cv2.imshow("Map", map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



    # print("start pos: " + str(start_node[0]) + ',' + str(start_node[1]))
    # print("goal pos: " + str(goal_node[0]) + ',' + str(goal_node[1]))
    # print(path)
