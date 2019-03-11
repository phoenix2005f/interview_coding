import numpy as np
from collections import Counter

test = np.array([[1,1,1,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]])

def sol2(test):
    area={}
    
    rows = test.shape[0]
    cols = test.shape[1]
    continent_id = 0
    
    for i in range(rows):
        
        for j in range(cols):
            
            label = test[i,j]
            if label == 1:
                
                check = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                is_inarea = any([ coord in area for coord in check])
                if is_inarea:
                    coord = None
                    for ele in check:
                        if ele in area:
                            coord = ele
                            break
                            
                    area[(i,j)] = area[coord]
                    
                else:
                    area[(i,j)] = continent_id
                    continent_id = continent_id+1
                    
            
    print(area)
    
    return Counter(area.values()).most_common()[0][1]
    
    
sol2(test)
