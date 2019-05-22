# Grid World Path Planning
This project contains a small python library for path planning problems in Grid World environment.
There are multiple planning algorithms implemented here such as random planner, random planner with short memory, A-star planner, Dijkstra's planner.

#### Inputs 
The algorithms take as an input a 2D arrays of 1's and 0's, where 1 deifnes an obstacle in the environment. It also takes as input the start and goal position of the point robot. And finally it takes as an input the number of allowed actions, i.e. 4 for orthogonal movements and 8 for king moves.

#### Pseudocode for Random Search Algorithm
```
- current state = initial position
- for i in maximum steps:
    - if current state is not goal position: 
        - generate all possible neighbour from current position
        - for all the neighbours:
            - remove the neighbours that are barriers if any
        - Choose a random state from the remaining neighbours
        - Update the current state
        - Append the path
    - else if the robot at goal pose return the path
- if goal position is not reached return no solution found
```

#### Pseudocode for Random Search with Memory Algorithm
```
- current state = initial position
- for i in maximum steps:
    - if current state is not goal position: 
        - find memory of the robot
        - generate all possible neighbour from current position
        - for all the neighbours:
            - remove the neighbours that are barriers if any
            - remove the neighbour in the memory of the robot if any
        - Choose a random state from the remaining neighbours
        - if no neighbours in the previous step choose a random neighbour which is not a barrier
        - Update the current state
        - Append the path
    - else if the robot at goal pose return the path
- if goal position is not reached return no solution found
```

#### Pseudocode for Astar Search Algorithm
```
 - Initialize a closed list
 - Initialize an open list with initial position
 - Initialize parent nodes
 - while open list has elements:
    - Find the state with lowest total estimated cost in open list and set it to current position of robot
    - If current state is goal position:
        - Check if the total cost is arbitrary high suggesting it generated a path through barriers since no other path exists and return No solution found
    - else return the path obtained
    - Find the neighbours of the current state 
    - Remove the ones already in closed list, add the new ones in open list and replace the parent if a lower movement cost obtained from some other node
    - Calculate the estimated total cost of the new added neighbour using the Manhattan heuristic
    - Since the node is processed remove it from open list and add it to closed list
```

#### Pseudocode for Dijkstra's Search Algorithm
```
 - Initialize a closed list
 - Initialize an open list with initial position
 - Initialize parent nodes
 - while open list has elements:
    - Find the state with lowest total cost from start to current position in open list and set it to current position of robot
    - If current state is goal position:
        - Check if the total cost is arbitrary high suggesting it generated a path through barriers since no other path exists and return No solution found
    - else return the path obtained
    - Find the neighbours of the current state 
    - Remove the ones already in closed list, add the new ones in open list and replace the parent if a lower movement cost obtained from some other node
    - Calculate the total cost of the new added neighbour
    - Since the node is processed remove it from open list and add it to closed list
```

