from itertools import permutations
import ast
import sys

def cost(cuts,w,h):
    width_cuts=[]
    height_cuts=[]

    for i in cuts:
        width_cuts.append(i[0])
        height_cuts.append(i[1])

    width_cuts= [0]+width_cuts+[w]
    height_cuts = [0] + height_cuts + [h] 
    
    m = len(width_cuts)
    sum=0
    for i in range(1,m-1):
        key1,key2=0,0
        if (width_cuts[i]>width_cuts[i-1] and height_cuts[i]>height_cuts[i-1]):
            b1 = (width_cuts[i]-width_cuts[i-1])  * (height_cuts[i] - height_cuts[i-1])
            b2 = (width_cuts[-1] - width_cuts[i]) * (height_cuts[i] - height_cuts[i-1])
            b3 = (width_cuts[i]-width_cuts[i-1])  * (height_cuts[-1] - height_cuts[i])
            b4 = (width_cuts[-1] - width_cuts[i]) * (height_cuts[-1] - height_cuts[i])

        elif (width_cuts[i]<width_cuts[i-1] and height_cuts[i]<height_cuts[i-1]):
            for j in range(len(width_cuts)-1):
                if width_cuts[i]>width_cuts[j] and width_cuts[i]<width_cuts[j+1]:
                    key1 = j
                    break
            for j in range(len(height_cuts)-1):
                if height_cuts[i]>height_cuts[j] and height_cuts[i]<height_cuts[j+1]:
                    key2 = j
                    break
            b1 = abs(width_cuts[i]-width_cuts[key1])  * abs(height_cuts[i] - height_cuts[key2])
            b2 = abs(width_cuts[key1+1] - width_cuts[i]) * abs(height_cuts[i] - height_cuts[key2])
            b3 = abs(width_cuts[i]-width_cuts[key1])  * abs(height_cuts[key2+1] - height_cuts[i])
            b4 = abs(width_cuts[key1+1] - width_cuts[i]) * abs(height_cuts[key2+1] - height_cuts[i])
        # insert
            width_cuts.insert(key1+1,width_cuts[i])
            del width_cuts[i]
            height_cuts.insert(key2+1,height_cuts[i])
            del height_cuts[i]
        sum+=b1+b2+b3+b4
    return sum*2

Input_File = open("input2.txt","r")
Data=[]
int_list=[]
for lines in Input_File:
    Data.append(lines.rstrip("\n"))

w,h=0,0
for x in Data:
    try:
        x=x.split(" ")
        w=int(x[0])
        h=int(x[1])
    except:
        int_list = ast.literal_eval(x[0])

    # Using permutations
        Total_orders = list(permutations(int_list))
        length = len(Total_orders)
    # Print each permutation
        if length<10:
            min_cost = sys.maxsize
            Optimal_Order = []
            for perm in Total_orders:
                cuts = list(perm)
                Final_cost = cost(perm,w,h)
                if Final_cost<min_cost:
                    min_cost = Final_cost
                    Optimal_Order.clear()
                    Optimal_Order.append(cuts)
            print("The minimum cost is {0}. The optimal order of the cuts is  {1}".format(min_cost,Optimal_Order[0]))