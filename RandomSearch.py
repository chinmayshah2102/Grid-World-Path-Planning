from generateMapProperties import genGridProp
import random as rd
 
 
def Search(world_state, robot_pose, goal_pose, number_of_actions):
    
    MapProperties = genGridProp(world_state)
    barriers = MapProperties.barriers
    
    max_step_number = 200
    
    currPos = robot_pose
    path = [robot_pose]

    for i in range(max_step_number):
        
        #Checking if we have reached the goal
        if currPos != goal_pose:
            possibleNeighbours = MapProperties.NeighbourVertices(currPos, world_state, number_of_actions)
            actualNeighbours = []
            
            for neighbour in possibleNeighbours:
                if neighbour not in barriers:
                    actualNeighbours.append(neighbour)
            
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
    
