Author: Gordon Dina

How to run from the terminal:
make sure dataset folder is in the same directory has the python file
type $ python3 skeleton_train.py
type $ python3 skeleton_test.py
type $ python3 custom_train.py
type $ python3 custom_test.py

Alternative the code could be run in visual studio code, provides the same result


Implementation:
I used a dictionary to catalog each frame and their respected joints, since they were arrays it made it simpler; I also grabbed the center for each frame and stored that in a list for the distance. Then I calculated the distances and angles through functions and stored the results into their repected lists: distance_rhand, distance_head, distance_lhand, distance_lfoot, distance_rfoot, angle_1, angle_2, angle_3, angle_4, and angle_5. 
Joints used in the RAD representation are 8 (right hand), 4 (head), 12 (left hand), 16 (right foot), and 20 (left foot); and for the custom representationare 5 (right shoulder), 3 (center shoulder), 9 (left shoulder), 14 (right knee), and  18 (left knee).
Histograms were made using numpy.histogram(array) function, the array used were the distances and angles calculated, then were normalized by dividing by max number frames. The number of bins that were used was the default for numpy.histogram() which is 10 
