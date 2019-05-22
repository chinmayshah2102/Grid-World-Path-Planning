import numpy as np
from generateMapProperties import genGridProp
import random as rd
 
 
def Search(world_state, robot_pose, goal_pose):
    
    MapProperties = genGridProp(world_state)
    barriers = MapProperties.barriers
    
    max_step_number = 200
    #defining Memory size
    memory_length = int(round(np.sqrt(max_step_number)))
    
    currPos = robot_pose
    path = [robot_pose]

    for i in range(max_step_number):
        
        #Checking if we have reached the goal
        if currPos != goal_pose:
            #Generate memory for each step
            memory = path[-min(memory_length,len(path)):]
            possible_motion = []
            possibleNeighbours = MapProperties.NeighbourVertices(currPos, world_state, 4)
            actualNeighbours = []
            
            for neighbour in possibleNeighbours:
                if neighbour not in barriers:
                    actualNeighbours.append(neighbour)
                    if neighbour not in memory:
                        possible_motion.append(neighbour)
            
            #Check if possible motion is empty, if so choose a neighbour from actual neighbours        
            if len(possible_motion)!=0:
                index = rd.randrange(len(possible_motion))
                newPos = possible_motion[index]
            else:
                index = rd.randrange(len(actualNeighbours))
                newPos = actualNeighbours[index]
                            
            currPos = newPos
            path.append(currPos)
        
        #If current position is goal position return the path
        else:
            return path
    #if after maximum steps the current position is not the goal position then return no solution
    if path[-1] != goal_pose:
        return "No solution found"
    