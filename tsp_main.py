import Greedy
import NearestNeighbor
import christofides
import plot
import numpy as np
import time
import read_input
import math
import ga

#screenSize = 700

if __name__ == '__main__':
    #selectfile = input("Enter Filename: ")
    selectfile = 'dataset/kroA200.tsp'
    data = read_input.readfile(selectfile)
    #print(data)
    numCities = data.shape[0]

    #calculating path
    start_time = time.time()
    #opt_path, length = NearestNeighbor.algorithm(data)
    #opt_path, length = Greedy.algorithm(data)
    opt_path, length = christofides.algorithm(data)
    #ga.algorithm(data)

    print("Optimal route:", opt_path)
    print("Length:", round(length,2))
    print("--- %s seconds ---" % (time.time() - start_time))
    #displaying path
    plot.plotTSP(opt_path, data, 1)