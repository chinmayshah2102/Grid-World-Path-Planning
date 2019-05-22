import numpy as np

class genGridProp(object):
 
    def __init__(self, world_state):          
        #Create a list of all barriers
        self.barriers = []
        temp = np.asarray(np.where(world_state==1))
        for i in range(temp.shape[1]):
            self.barriers.append((temp[0][i],temp[1][i]))
    
    def NeighbourVertices(self, currPos, world_state, number_of_neighbour):
        n = []
        #Define neighbour based on types of movements allowed (Orthogonal(4 neighbours) or King's moves(8 neighbours))
        if number_of_neighbour == 4:
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x2 = currPos[0] + dx
                y2 = currPos[1] + dy
                #Checking for boundary of map
                if x2 < 0 or x2 > (world_state.shape[0]-1) or y2 < 0 or y2 > (world_state.shape[1]-1):
                    continue
                n.append((x2, y2))
            return n
        elif number_of_neighbour == 8:
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]:
                x2 = currPos[0] + dx
                y2 = currPos[1] + dy
                #Checking for boundary of map
                if x2 < 0 or x2 > (world_state.shape[0]-1) or y2 < 0 or y2 > (world_state.shape[1]-1):
                    continue
                n.append((x2, y2))
            return n

    def stepCost(self, currPos, possNeighbour):
        for barriers in enumerate(self.barriers):
            if possNeighbour in barriers:
                return float('inf')
        return 1
     
    def Mdist_heuristic(self, robot_pose, goal):
        #Using Manhattan distance as a heuristic since only orthogonal movements are allowed
        dx = abs(robot_pose[1] - goal[1])
        dy = abs(robot_pose[0] - goal[0])
        return (dx + dy)
      
    def Ddist_heuristic(self, robot_pose, goal):
        #Using Diagonal distance as a heuristic since diagonal movements are allowed
        dx = abs(robot_pose[1] - goal[1])
        dy = abs(robot_pose[0] - goal[0])
        return (dx + dy) + (np.sqrt(2)-2)*min(dx,dy)
      
