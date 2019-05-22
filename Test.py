import numpy as np
import matplotlib.pyplot as plt
from AstarSearch import Search

if __name__=="__main__":
    
    #Test Case 1
    world_state = np.array([[0, 0, 1, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1, 0],
                            [0, 0, 1, 1, 1, 0],
                            [0, 0, 0, 0, 0, 0]])
    
    path = Search(world_state, (2,0), (5,5), 8)
    
    #Plotting the result
    barriers = np.asarray(np.where(world_state==1))
    barriers=barriers.tolist()
    if isinstance(path, str):
        print(path)
    else:
        print("Path:",path)
        plt.plot([v[1] for v in path], [v[0] for v in path])    
    plt.plot(barriers[1],barriers[0],'ro')
    plt.xlim(-1,6)
    plt.ylim(-1,6)
    plt.gca().invert_yaxis()
    plt.savefig('Optimal1.png')
    plt.show()
    
    
    #Test Case 2
    world_state = np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 1, 1, 1, 1, 1, 1, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 1, 0],
                            [0, 0, 0, 1, 0, 0, 0, 1, 0],
                            [0, 0, 0, 1, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 1, 1, 1, 1, 1, 1, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0, 0]])

    path = Search(world_state, (1,0), (7,8), 8)
    
    #Plotting the result
    barriers = np.asarray(np.where(world_state==1))
    barriers=barriers.tolist()
    if isinstance(path, str):
        print(path)
    else:
        print("Path:",path)
        plt.plot([v[1] for v in path], [v[0] for v in path])    
    plt.plot(barriers[1],barriers[0],'ro')
    plt.xlim(-1,9)
    plt.ylim(-1,9)
    plt.gca().invert_yaxis()
    plt.savefig('Optimal2.png')
    plt.show()
    
