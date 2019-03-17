import math
import numpy as np
import random
import sys

name = 0
def isPowerOfTwo(n):
    if(n > 1):
        return math.ceil(math.log(n,2) == math.floor(math.log(n,2)))
    else:
        return False

def readFromFile(fileName):
    f = open(fileName,"r")
    n = int(f.readline())
    #print(n)
    d = int(f.readline())
    #print(d)
    f.close()
    from itertools import islice
    with open(fileName) as lines:
        array = np.genfromtxt(islice(lines,2,n+2))
    return array,n,d

def writeToFile(array,n,d):
    global name
    out_0 = open("out_"+str(name),"w")
    name = name + 1
    out_0.write(str(n))
    out_0.write("\n")
    out_0.write(str(d))
    out_0.write("\n")
    for line in array:
        temp =  ""
        for i in range(d):
            if(i!= d-1 ):
                temp = temp + str(line[i]) + " "
            else:
                temp = temp + str(line[i])
        out_0.write(temp)
        out_0.write("\n")
    out_0.close()
    print("Completed Writing To File")
    
    
def kdpart(N,array,n,d):
    if(N!=1):
        nsample = (n)//10
        #print(nsample)
        #random.seed(10000)
        samplearray = random.sample(range(3,n),nsample)
        #print(samplearray)
        sarray = np.array(array[samplearray])
        print("Array Read And Sampling Done")
        rangearray = []
        for i in range(d):
            rangearray.append(np.max(sarray,axis = 0)[i] - np.min(sarray,axis = 0)[i])
        maxAxis = rangearray.index(max(rangearray))
        print("Max Axis is",maxAxis)
        median = np.median(sarray,axis = 0)
        print("Median is ",median)
        #code for file creation
        left = []
        right = []
        nleft = 0
        nright = 0
        for point in array:
            if point[maxAxis] <= median[maxAxis]:
                nleft = nleft + 1
                left.append(point)
            else:
                nright = nright + 1
                right.append(point)
        left = np.array(left)
        right = np.array(right)
        print(len(left))
        print(len(right))
        N = N//2
        kdpart(N,left,nleft,d)
        kdpart(N,right,nright,d)
    else:
        writeToFile(array,n,d)
    
if __name__ == "__main__":
    print("KD Partitioning")
    #fileName = "3d_road"
    fileName = "iris_data"
    N = 4
    if(len(sys.argv)!=3):
        print("Input Format : <KDSample.py> <Number Of Splits> <Input File>")
    else:
        N = int(sys.argv[1])
        fileName = str(sys.argv[2])
    if(isPowerOfTwo(N)):
        print("Correct Value Of N")
        array,n,d = readFromFile(fileName)
        kdpart(N,array,n,d)
    else:
        print("Insert Value Of N As Some Power Of 2")

