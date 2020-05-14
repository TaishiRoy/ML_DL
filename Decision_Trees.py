


########### IMPLEMENTING DECISION TREE FROM SCRATCH FOR THE TITANIC PROBLEM (SEE KAGGLE) #################



from __future__ import print_function
import sys
import csv 
import numpy as np
import math
np.set_printoptions(threshold=sys.maxsize)

class Node(object):
    def __init__(self):
        self.val = None
        self.child0 = None
        self.child1 = None
        self.child2 = None
        self.child3 = None

############################################################################################################################

def getCount(data, key):
    data2array = np.array(data)
    transp = data2array.transpose()
    return np.count_nonzero(transp == key)




        
###########################################################################################################################

def getEntropy(strng, data, index):
    if strng=='':
        y = -(getCount(data, 'yes')/(1.0*(len(data)))) * (np.log2((getCount(data, 'yes')/(1.0*(len(data))))))
        n = -(getCount(data, 'no')/(1.0*(len(data)))) * (np.log2((getCount(data, 'no')/(1.0*(len(data))))))
        return y+n
    ycount = 0
    ncount = 0
    for i in range(len(data)):
        if data[i][index] == strng:
            if data[i][3] == 'yes':
                ycount+=1
            if data[i][3] == 'no':
                ncount+=1
    p = (1.0*(ycount + ncount))/len(data) 
    y = -ycount/(1.0*(ycount + ncount)) * (np.log2(ycount/(1.0*(ycount + ncount))))
    n = -ncount/(1.0*(ycount + ncount)) * (np.log2(ncount/(1.0*(ycount + ncount))))

    return p*(y+n)






###########################################################################################################################
            

def getTotalEntropy(strng, data):

    if strng=='pclass':
        return getEntropy('1st', data, 0) + getEntropy('2nd',data,0) +  getEntropy('3rd', data, 0) + getEntropy('crew',data, 0)

    if strng=='age':
        return getEntropy('adult', data, 1) + getEntropy('child',data,1 )

    if strng=='gender':
        return getEntropy('female', data, 2) + getEntropy('male',data, 2)



    


#################################################################################################################################

def getInfoGain(strng, dataSet):

    return getEntropy('', dataSet, 0) - getTotalEntropy(strng, dataSet)




#################################################################################################################################   

def chooseAttr(attr, dataSet):
    maxval = 0
    if len(attr) == 1:
        return 0
    for elem in range(len(attr)):
        x = getInfoGain(attr[elem], dataSet)
        if x > maxval :
            maxval = x
            y = elem

    return y





################################################################################################################################



def buildTree(attr, dataSet, node, minval, maxval):


    yes=0
    no=0

    for sublist in range(len(dataSet)):
            if dataSet[sublist][3] == 'yes':
                yes+=1
            if dataSet[sublist][3] == 'no':
                no+=1

    if no==0:
        print(' -> yes', end=' ')
        return

    if yes==0:
        print(' -> no', end=' ')
        return

    if len(attr)==0:
            if yes>no:
                print(' -> likely yes', end=' ')
            else:
                print(' -> likely no', end=' ')
            return

    if minval == maxval:
        return
    if len(attr) == 0:
        return

    bestAttr = chooseAttr(attr, dataSet[minval:(maxval+1)])
    node.val = attr[bestAttr]
    new_attr = np.delete(attr, bestAttr)
    max0=0
    max1=0
    max2=0
    min0=0
    min1=0
    min2=0

    dataSet = np.array(dataSet)
    if attr[bestAttr]=='pclass':
        sortedArr = dataSet[dataSet[:,0].argsort()]
    if attr[bestAttr]=='age':
        sortedArr = dataSet[dataSet[:,1].argsort()]
    if attr[bestAttr]=='gender':
        sortedArr = dataSet[dataSet[:,2].argsort()]


    ##################################################

    if attr[bestAttr] == 'pclass':
        print('\n', end=' ')
        for el in range(3-len(attr)):
            print('\t', end=' ')
        print( node.val + '= 1st', end=' ')
        yes=0
        no=0

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == '1st':
                if sortedArr[sublist][3] == 'yes':
                    yes+=1
                else:
                    no+=1

        if no==0:
            print(' -> yes', end=' ')
            return

        if yes==0:
            print(' -> no', end=' ')
            return

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == '1st':
                max0 = sublist


        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == '1st':
                min0 = sublist
                break

        node.child0 = Node()

        buildTree(new_attr, sortedArr[min0:(max0+1)], node.child0, min0, max0)

        print('\n', end=' ')
        for el in range(3-len(attr)):
            print('\t', end=' ')

        print( node.val + '= 2nd', end=' ')


        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == '2nd':
                if sortedArr[sublist][3] == 'yes':
                    yes+=1
                else:
                    no+=1

        if no==0:
            print(' -> yes', end=' ')
            return

        if yes==0:
            print(' -> no', end=' ')
            return

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == '2nd':
                max0 = sublist


        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == '2nd':
                min0 = sublist
                break

        node.child1 = Node()
        
        buildTree(new_attr, sortedArr[min0:(max0+1)], node.child1, min0, max0)

        print('\n', end=' ')
        for el in range(3-len(attr)):
            print('\t', end=' ')

        print( node.val + '= 3rd', end=' ')

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == '3rd':
                if sortedArr[sublist][3] == 'yes':
                    yes+=1
                else:
                    no+=1

        if no==0:
            print(' -> yes', end=' ')
            return

        if yes==0:
            print(' -> no', end=' ')
            return

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == '3rd':
                max0 = sublist


        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == '3rd':
                min0 = sublist
                break

        node.child2 = Node()
        
        buildTree(new_attr, sortedArr[min0:(max0+1)], node.child2, min0, max0)

        print('\n', end=' ')
        for el in range(3-len(attr)):
            print('\t', end=' ')

        print( node.val + '= crew', end=' ')

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == 'crew':
                if sortedArr[sublist][3] == 'yes':
                    yes+=1
                else:
                    no+=1

        if no==0:
            print(' -> yes', end=' ')
            return

        if yes==0:
            print(' -> no', end=' ')
            return

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == 'crew':
                max0 = sublist


        for sublist in range(len(dataSet)):
            if sortedArr[sublist][0] == 'crew':
                min0 = sublist
                break

        node.child3 = Node()
        
        buildTree(new_attr, sortedArr[min0:(max0+1)], node.child3, min0, max0)


    #####################################################

    if attr[bestAttr] == 'age':

        print('\n', end=' ')
        for el in range(3-len(attr)):
            print('\t', end=' ')
        print( node.val + '= adult', end=' ')

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][1] == 'adult':
                if sortedArr[sublist][3] == 'yes':
                    yes+=1
                else:
                    no+=1

        if no==0:
            print(' -> yes', end=' ')
            return

        if yes==0:
            print(' -> no', end=' ')
            return

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][1] == 'adult':
                max1 = sublist


        for sublist in range(len(dataSet)):
            if sortedArr[sublist][1] == 'adult':
                min1 = sublist
                break

        node.child0 = Node()
        
        buildTree(new_attr, sortedArr[min1:(max1+1)], node.child0, min1, max1)

        print('\n', end=' ')
        for el in range(3-len(attr)):
            print('\t', end=' ')

        print( node.val + '= child', end=' ')

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][1] == 'child':
                if sortedArr[sublist][3] == 'yes':
                    yes+=1
                else:
                    no+=1

        if no==0:
            print(' -> yes', end=' ')
            return

        if yes==0:
            print(' -> no', end=' ')
            return

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][1] == 'child':
                max1 = sublist

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][1] == 'child':
                min1 = sublist
                break

        node.child1 = Node()
        
        buildTree(new_attr, sortedArr[min1:(max1+1)], node.child1, min1, max1)

    #########################################


    if attr[bestAttr] == 'gender':

        print('\n', end=' ')
        for el in range(3-len(attr)):
            print('\t', end=' ')

        print( node.val + '= female', end=' ')

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][2] == 'female':
                if sortedArr[sublist][3] == 'yes':
                    yes+=1
                else:
                    no+=1

        if no==0:
            print(' -> yes', end=' ')
            return

        if yes==0:
            print(' -> no', end=' ')
            return

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][2] == 'female':
                max2 = sublist


        for sublist in range(len(dataSet)):
            if sortedArr[sublist][2] == 'female':
                min2 = sublist
                break

        node.child0 = Node()
        
        buildTree(new_attr, sortedArr[min2:(max2+1)], node.child0, min2, max2)

        print('\n', end=' ')
        for el in range(3-len(attr)):
            print('\t', end=' ')

        print( node.val + '= male', end=' ')

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][2] == 'male':
                if sortedArr[sublist][3] == 'yes':
                    yes+=1
                else:
                    no+=1

        if no==0:
            print(' -> yes', end=' ')
            return

        if yes==0:
            print(' -> no', end=' ')
            return

        for sublist in range(len(dataSet)):
            if sortedArr[sublist][2] == 'male':
                max2 = sublist


        for sublist in range(len(dataSet)):
            if sortedArr[sublist][2] == 'male':
                min2 = sublist
                break

        node.child1 = Node()
        
        buildTree(new_attr, sortedArr[min2:(max2+1)], node.child1, min2, max2)




def main():
    attr = np.array(['pclass', 'age', 'gender'])
    dataSet = []
    filename = "data1_19.csv"
    fields = [] 
    rows = [] 
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)  
        fields = csvreader.next()  
        for row in csvreader: 
            rows = []
            for col in row:
                rows.append(col)
            dataSet.append(rows)

 
    
    root = Node()
    buildTree(attr, dataSet, root, 0, 2200)
    print('\n')

if __name__ == '__main__':
	main()
