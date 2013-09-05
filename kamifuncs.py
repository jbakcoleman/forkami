import numpy as np
import random
def g_test(mat):
    '''This function returns a g-test statsitics for a matrix'''
    pass

def shake_up(mat):
    '''This function sums up along the columns and returns a matrix
    if the data were randomly distributed'''

    
    pass

def rand_array(arr):
    ''' This function takes an array, sums it and distributes the remainder randomly'''
    #Total amount to distribute
    total = sum(arr)
    

    #Uses a list comprehsnion to generate 4 random "cuts" have dan check to
    #ensure this is a valid method of  randomly assigning values. 
    cuts = [random.randrange(0, total) for item in range(arr.size - 1)]
    cuts = cuts + [0, total]
    
    #organize cuts from smallest to largest
    cuts.sort()

    #Another list comprehension that uses the gaps between cuts as the amounts
    #distributed to each in the array
    out = np.array([cuts[ii+1] - cuts[ii] for ii in range(len(cuts) -1)])
    
    print(cuts)
    print(out)
    return out


'''The following if statement executes the code if it's being ran
from this file, but not if the file is being imported'''

if __name__ == "__main__":
    testData = np.array([[4,3,3,3,2],[3,4,2,4,3],[4,3,2,4,5], [4,3,2,4,2],\
                         [2,3,4,2,5]])
    print(rand_array(testData[:, 0]))
    
