
import numpy as np
import random
import sys
import csv 

class Node(object):
    def __init__(self):
        self.val = None
        self.child0 = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.signif = None



############################# to check output of a decision stump for a sample ############################
def liveordie(sample, root):
    if root.val == 0:
        if sample[0] == '1st':
            if root.child0 == 'yes':
                return 1
            else:
                return -1

        if sample[0] == '2nd':
            if root.child1 == 'yes':
                return 1
            else:
                return -1

        if sample[0] == '3rd':
            if root.child2 == 'yes':
                return 1
            else:
                return -1

        if sample[0] == 'crew':
            if root.child3 == 'yes':
                return 1
            else:
                return -1


    if root.val == 1:
        if sample[1] == 'child':
            if root.child0 == 'yes':
                return 1
            else:
                return -1

        if sample[1] == 'adult':
            if root.child1 == 'yes':
                return 1
            else:
                return -1


    if root.val == 2:
        if sample[2] == 'female':
            if root.child0 == 'yes':
                return 1
            else:
                return -1

        if sample[2] == 'male':
            if root.child1 == 'yes':
                return 1
            else:
                return -1

    



##################################### A D A B  O S T ##########################################

def adaboost(dataSet, attr):

    root0 = Node()
    root1 = Node()
    root2 = Node()


    for iter in range(3):

        root = Node()
        weight = []
        for i in range(len(dataSet)):
            weight.append(1/len(dataSet))

    
        ###############################  pclass  ####################
    
        yes = 0
        no = 0
        error0 = 0
    
        for sublist in dataSet:
            if sublist[0] == '1st':
                if sublist[3] == 'yes':
                    yes+=1
                else:
                    no+=1           ############# count yes no #################

        if yes>=no:
            root.child0 = 'yes'
            error0+= no
        else:                       ############ get error ####################
            root.child0 = 'no'
            error0+= yes
    
    
        yes = 0
        no = 0
    
        for sublist in dataSet:
            if sublist[0] == '2nd':
                if sublist[3] == 'yes':
                    yes+=1
                else:
                    no+=1       ############# count yes no #################

        if yes>=no:
            root.child1 = 'yes'
            error0+= no
        else:                       ############ get error ####################
            root.child1 = 'no'
            error0+= yes
    
        yes = 0
        no = 0
    
        for sublist in dataSet:
            if sublist[0] == '3rd':
                if sublist[3] == 'yes':
                    yes+=1
                else:
                    no+=1       ############# count yes no #################

        if yes>=no:
            root.child2 = 'yes'
            error0+= no
        else:                       ############ get error ####################
            root.child2 = 'no'
            error0+= yes
    
    
        yes = 0
        no = 0
    
        for sublist in dataSet:
            if sublist[0] == 'crew':
                if sublist[3] == 'yes':
                    yes+=1
                else:
                    no+=1       ############# count yes no #################

        if yes>=no:
            root.child3 = 'yes'
            error0+= no
        else:                       ############ get error ####################
            root.child3 = 'no'
            error0+= yes
    
    
    
        ###############################  age  ####################
    
        yes = 0
        no = 0
        error1 = 0
    
        for sublist in dataSet:
            if sublist[1] == 'child':
                if sublist[3] == 'yes':
                    yes+=1
                else:
                    no+=1       ############# count yes no #################

        if yes>=no:
            root.child0 = 'yes'
            error1+= no
        else:                       ############ get error ####################
            root.child0 = 'no'
            error1+= yes
    
    
        yes = 0
        no = 0
    
        for sublist in dataSet:
            if sublist[1] == 'adult':
                if sublist[3] == 'yes':
                    yes+=1
                else:
                    no+=1       ############# count yes no #################

        if yes>=no:
            root.child1 = 'yes'
            error1+= no
        else:                       ############ get error ####################
            root.child1 = 'no'
            error1+= yes
    
    
        ###############################  gender  ####################
    
        yes = 0
        no = 0
        error2 = 0
    
        for sublist in dataSet:
            if sublist[2] == 'female':
                if sublist[3] == 'yes':
                    yes+=1
                else:
                    no+=1       ############# count yes no #################
    
        if yes>=no:
            root.child0 = 'yes'
            error2+= no
        else:                       ############ get error ####################
            root.child0 = 'no'
            error2+= yes
    
    
        yes = 0
        no = 0
    
        for sublist in dataSet:
            if sublist[2] == 'male':
                if sublist[3] == 'yes':
                    yes+=1
                else:
                    no+=1       ############# count yes no #################

        if yes>=no:
            root.child1 = 'yes'
            error2+= no
        else:                       ############ get error ####################
            root.child1 = 'no'
            error2+= yes
    
    
        if error0 == min(error0,error1,error2) :
            error = error0/len(dataSet)
            select = 0
        if error1 == min(error0,error1,error2) :
            error = error1/len(dataSet)
            select = 1
        if error2 == min(error0,error1,error2) :
            error = error2/len(dataSet)
            select = 2              ############ least error rate #############

        if error == 0:
            error = (1/(len(dataSet)*100))
    
        ############################ significance #################################
        significance = (1/2) * np.log((1-error)/error) 

        if iter==0 :
            root0 = root
            root0.signif = significance
            root0.val = select
        if iter==1 :
            root1 = root
            root1.signif = significance
            root1.val = select
        if iter==2 :
            root2 = root
            root2.signif = significance
            root2.val = select

    
    
        ################################# weigh updation ##################################
        for i in range(len(dataSet)):
            if select == 0:
                if dataSet[i][0] == '1st':
                    if dataSet[i][3] == root.child0:
                        weight[i] = weight[i] * np.exp(-significance)   ## decrease weight
                    else:
                        weight[i] = weight[i] * np.exp(significance)    ## increase weight
    
                if dataSet[i][0] == '2nd':
                    if dataSet[i][3] == root.child1:
                        weight[i] = weight[i] * np.exp(-significance)   ## decrease weight
                    else:
                        weight[i] = weight[i] * np.exp(significance)    ## increase weight
    
                if dataSet[i][0] == '3rd':
                    if dataSet[i][3] == root.child2:
                        weight[i] = weight[i] * np.exp(-significance)   ## decrease weight
                    else:
                        weight[i] = weight[i] * np.exp(significance)    ## increase weight
    
                if dataSet[i][0] == 'crew':
                    if dataSet[i][3] == root.child3:
                        weight[i] = weight[i] * np.exp(-significance)   ## decrease weight
                    else:
                        weight[i] = weight[i] * np.exp(significance)    ## increase weight
    
    
    
    
            if select == 1:
                if dataSet[i][1] == 'child':
                    if dataSet[i][3] == root.child0:
                        weight[i] = weight[i] * np.exp(-significance)   ## decrease weight
                    else:
                        weight[i] = weight[i] * np.exp(significance)    ## increase weight
    
                if dataSet[i][1] == 'adult':
                    if dataSet[i][3] == root.child1:
                        weight[i] = weight[i] * np.exp(-significance)   ## decrease weight
                    else:
                        weight[i] = weight[i] * np.exp(significance)    ## increase weight
    
    
    
            if select == 2:
                if dataSet[i][2] == 'female':
                    if dataSet[i][3] == root.child0:
                        weight[i] = weight[i] * np.exp(-significance)   ## decrease weight
                    else:
                        weight[i] = weight[i] * np.exp(significance)    ## increase weight
    
                if dataSet[i][2] == 'male':
                    if dataSet[i][3] == root.child1:
                        weight[i] = weight[i] * np.exp(-significance)   ## decrease weight
                    else:
                        weight[i] = weight[i] * np.exp(significance)    ## increase weight
    
        totalwt = 0
    
        for i in range(len(weight)):
            totalwt+= weight[i]
    
        for i in range(len(weight)):
            weight[i] = weight[i]/totalwt ########## normalisation ##############


    
        ################## new dataset generation #######################
    
        new_data = []
        for i in range(len(dataSet)):
            num = random.random()
            copyhere = 0
            for j in range(len(dataSet)):
                if num <= (copyhere + weight[j]) and num >= copyhere :
                    new_data.append(dataSet[j])
                    copyhere+= weight[j]
                    break
                copyhere+= weight[j]
        
    
        dataSet = new_data


        ################# iteration ends

    ######################### training complete ############################

    testSet = []
    filename = "test3_19.csv"
    rows = [] 
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)  
        next(csvreader)  
        for row in csvreader: 
            rows = []
            for col in row:
                rows.append(col)
            testSet.append(rows)

    
    live = 0
    dead = 0
    acc = 0

    for sublist in testSet:
        live = 0
        dead = 0

        if liveordie(sublist, root0) == 1:
            live+= root0.signif
        else:
            dead+= root0.signif
        
        if liveordie(sublist, root1) == 1:
            live+= root1.signif
        else:
            dead+= root1.signif

        if liveordie(sublist, root2) == 1:
            live+= root2.signif
        else:
            dead+= root2.signif

        if live>dead and sublist[3]=='yes':
            acc+=1
        if dead>=live and sublist[3]=='no':
            acc+=1
        

    return acc/len(testSet) * 100 

    ######################## testing complete ##################




def main():
    # read file
    attr = np.array(['pclass', 'age', 'gender'])
    dataSet = []
    filename = "data3_19.csv"
    rows = [] 
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)  
        next(csvreader)  
        for row in csvreader: 
            rows = []
            for col in row:
                rows.append(col)
            dataSet.append(rows)
    
    result = adaboost(dataSet, attr)

    print(' Accuracy = ', result, '%')





if __name__ == '__main__':
	main()
