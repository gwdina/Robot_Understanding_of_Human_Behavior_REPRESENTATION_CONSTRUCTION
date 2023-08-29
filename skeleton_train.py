#!/usr/bin/python3    
import cmath
import string
import time
import random
import csv
import json
import math
import numpy as np
import os
import math
from pathlib import Path
import matplotlib.pyplot as plt


# joint 1 is the center for each frame 

# Joint: center:1, head 1:4, right hand 2:8, left hand 3:12, right foot 4:16, left foot 5:20
# angles: 1 = 8-4, 2 = 4-12, 3 = 12-20, 4 = 20-16, 5 = 16-8

# # Creating an array
# List = [1, 2, 3, 4, 5]
# Array = numpy.array(List)
 
# # Displaying the array
# print('Array:\n', Array)
# file = open("rad_d1_train.txt.txt", "w+")
 
# # Saving the array in a text file
# content = str(Array)
# file.write(content)
# file.close()
 
# # Displaying the contents of the text file
# file = open("file1.txt", "r")
# content = file.read()
 
# print("\nContent in file1.txt:\n", content)
# file.close()



data_folder = Path("dataset/train/")
file_to_open = data_folder / "a08_s01_e01_skeleton_proj.txt"


center = []

table = {}

distance_rhand = [] #8 d1

distance_head = [] #4 d2

distance_lhand = [] #12 d3

distance_lfoot = [] #20 d4

distance_rfoot = [] #16 d5

####
angle_1 = [] #8-4

angle_2 = [] #4-12

angle_3 = [] #12-20

angle_4 = [] #20-16

angle_5 = [] #16-8



def file_read(fname):
        with open(fname) as f:
                i = 1
                joints = []
                for line in f:
                    numbers_str = line.split()
                    numbers_float = [float(x) for x in numbers_str]

                    # frame, joint, x, y, z
                    if(numbers_float[1] == 1):
                        center.append(numbers_float)

                    #if(numbers_float[1] % 4 == 0 and (numbers_float[0] == 1 or numbers_float[0] == 2)):
                    if(numbers_float[1] % 4 == 0):
                        #print(numbers_float)
                        joints.append(numbers_float)
                        if(numbers_float[1] == 20):
                            jon = joints
                            table[i] = jon
                            i += 1
                            joints = []
                    
                   
         

# file_read('a08_s01_e01_skeleton_proj.txt')






def distance(frame,x,y,z):
    # do we need the center
    # result = math.sqrt(x**2 + y**2 + z**2)
    result = math.sqrt((x - center[frame][2])**2 + (y - center[frame][3])**2 + (z - center[frame][4])**2)
    #print(result)
    return result

def angle(x1,y1,z1,x2,y2,z2):
    top = x1*x2 + y1*y2 + z1*z2 
    bottom = math.sqrt((x1**2 + y1**2 + z1**2) * (x2**2 + y2**2 + z2**2))
    calc = top / bottom
    return math.acos(calc) * (180 / math.pi)


def build_table():
    for keys in table.keys():
        distance_head.append(distance(keys-1, table[keys][0][2],table[keys][0][3], table[keys][0][4])) # head 4

        distance_rhand.append(distance(keys-1, table[keys][1][2],table[keys][1][3], table[keys][1][4])) # right hand 8
    
        distance_lhand.append(distance(keys-1, table[keys][2][2],table[keys][2][3], table[keys][2][4])) # left hand 12

        distance_rfoot.append(distance(keys-1, table[keys][3][2],table[keys][3][3], table[keys][3][4])) # right foot 16

        distance_lfoot.append(distance(keys-1, table[keys][4][2],table[keys][4][3], table[keys][4][4])) # left foot 20

        # angles: 1 = 8-4, 2 = 4-12, 3 = 12-20, 4 = 20-16, 5 = 16-8 
        angle_1.append(angle(table[keys][1][2], table[keys][1][3], table[keys][1][4], table[keys][0][2], table[keys][0][3], table[keys][0][4])) # 8-4

        angle_2.append(angle(table[keys][0][2], table[keys][0][3], table[keys][0][4], table[keys][2][2], table[keys][2][3], table[keys][2][4])) # 4-12

        angle_3.append(angle(table[keys][2][2], table[keys][2][3], table[keys][2][4], table[keys][4][2], table[keys][4][3], table[keys][4][4])) # 12-20

        angle_4.append(angle(table[keys][4][2], table[keys][4][3], table[keys][4][4], table[keys][3][2], table[keys][3][3], table[keys][3][4])) # 20-16

        angle_5.append(angle(table[keys][3][2], table[keys][3][3], table[keys][3][4], table[keys][1][2], table[keys][1][3], table[keys][1][4])) # 16-8


# file_read(file_to_open)

# print(len(table))

file = open("rad_d1_train.txt", "w")
file.close()

Path = "dataset/train/"
filelist = os.listdir(Path)
for i in filelist:
    if i.endswith(".txt"):
        # print(Path+i)
        file_read(Path+i)
        # print(len(table))
        build_table()
        

        fix1 = np.array(distance_rhand)
        d1, bin1 = np.histogram(fix1[~np.isnan(fix1)])

        d1  = d1 / len(table)

        fix2 = np.array(distance_head)
        d2, bin2 = np.histogram(fix2[~np.isnan(fix2)])

        d2  = d2 / len(table)

        fix3 = np.array(distance_lhand)
        d3, bin3 = np.histogram(fix3[~np.isnan(fix3)])
        
        d3  = d3 / len(table)

        fix4 = np.array(distance_lfoot)
        d4, bin4 = np.histogram(fix4[~np.isnan(fix4)])

        d4  = d4 / len(table)

        fix5 = np.array(distance_rfoot)
        d5, bin5 = np.histogram(fix5[~np.isnan(fix5)])

        d5  = d5 / len(table)

        fix_angle_1 = np.array(angle_1)
        theta1, bin6 = np.histogram(fix_angle_1[~np.isnan(fix_angle_1)])

        theta1  = theta1 / len(table)

        fix_angle_2 = np.array(angle_2)
        theta2, bin7 = np.histogram(fix_angle_2[~np.isnan(fix_angle_2)])

        theta2  = theta2 / len(table)

        fix_angle_3 = np.array(angle_3)
        theta3, bin8 = np.histogram(fix_angle_3[~np.isnan(fix_angle_3)])

        theta3  = theta3 / len(table)

        fix_angle_4 = np.array(angle_4)
        theta4, bin9 = np.histogram(fix_angle_4[~np.isnan(fix_angle_4)])

        theta4  = theta4 / len(table)

        fix_angle_5 = np.array(angle_5)
        theta5, bin10 = np.histogram(fix_angle_5[~np.isnan(fix_angle_5)])

        theta5  = theta5 / len(table)

        con = np.concatenate((d1, d2, d3, d4, d5, theta1, theta2, theta3, theta4, theta5))
        file = open("rad_d1_train.txt", "a")
        file.write(i[:11])
        file.write(": ")
        file.write(" ".join([str (x) for x in con]))
        # file.write(content.replace('\n','').replace(' ',''))
        file.write('\n')
        angle_4 = [] #20-16
        angle_5 = [] #16-8

        file.close()
        
        center = []
        table = {}
        distance_rhand = [] #8 d1
        distance_head = [] #4 d2
        distance_lhand = [] #12 d3
        distance_lfoot = [] #20 d4
        distance_rfoot = [] #16 d5
        ####
        angle_1 = [] #8-4
        angle_2 = [] #4-12
        angle_3 = [] #12-20
        angle_4 = [] #20-16
        angle_5 = [] #16-8






# print(np.histogram(distance_head, density=True))
# print(np.histogram(distance_rhand, density=True))
# print(np.histogram(distance_lhand, density=True))
# print(np.histogram(distance_rfoot, density=True))
# print(np.histogram(distance_lfoot, density=True))


# print(np.histogram(angle_1, density=True))
# print(np.histogram(angle_2, density=True))
# print(np.histogram(angle_3, density=True))
# print(np.histogram(angle_4, density=True))
# print(np.histogram(angle_5, density=True))


# a = np.array([1,2,1, 5, 5, 4, 3, 1, 2, 2, 3])
# # plt.hist(angle_1)
# plt.hist(a, bins = [1, 2, 3, 5, 4]) 
# plt.title("histogram") 
# plt.show()




# Path = "dataset/train/"
# filelist = os.listdir(Path)
# for i in filelist:
#     if i.endswith(".txt"):
#         print(Path+i)
#         # file_read(Path+i)
             
             
