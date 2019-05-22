from generateMapProperties import genGridProp
 
def Search(world_state, robot_pose, goalPos):
    
    MapProperties = genGridProp(world_state)
    
    #Initiating a closed and open set to track the vertices and store the parent node 
    #Each position of the robot is stored as a tuple
    ClosedList = set()
    OpenList = set([robot_pose])
    ParentNode = {}
 
    #Actual movement cost from start to current position
    MovementCost = {} 
    MovementCost[robot_pose] = 0 
    
    #Estimated total cost from current to goal position
    TotalCost = {} 
    TotalCost[robot_pose] = MapProperties.Mdist_heuristic(robot_pose, goalPos)
 
    while len(OpenList) > 0:
        
        #Replacing current state with state that has lowest total estimated cost
        currPos = []
        currPosTotalCost = []
        for pos in OpenList:
            if len(currPos) == 0 or TotalCost[pos] < currPosTotalCost:
                currPosTotalCost = TotalCost[pos]
                currPos = pos
 
        #Check if we have reached the goal position
        if currPos == goalPos:
            #Retrace the path backward using parent nodes
            path = [currPos]
            while currPos in ParentNode:
                currPos = ParentNode[currPos]
                path.append(currPos)
            path.reverse()
            
            #Returning No solution exists if no error found in input and no path exists
            if TotalCost[goalPos] == float('inf'):
                return "No solution found"
            else:
                return path                
 
        #Generate costs for neighboring vertices for the current position
        for neighbour in MapProperties.NeighbourVertices(currPos, world_state, 4):
            
            if neighbour in ClosedList: 
                continue 
            Gscore = MovementCost[currPos] + MapProperties.stepCost(currPos, neighbour)
 
            if neighbour not in OpenList:
                OpenList.add(neighbour) 
            elif Gscore >= MovementCost[neighbour]:
                continue 

            ParentNode[neighbour] = currPos
            MovementCost[neighbour] = Gscore
            HeuristicCost = MapProperties.Mdist_heuristic(neighbour, goalPos)
            TotalCost[neighbour] = MovementCost[neighbour] + HeuristicCost
        
        #Append the current state to closed vertices and remove the same from open vertices
        OpenList.remove(currPos)
        ClosedList.add(currPos)
        
    return "Error in Map properties"
