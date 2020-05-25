import os, sys, codecs
import numpy as np
import gzip
import pandas as pd

from jsd import *
from general import *

###########################################################
# DAY SCALE
###########################################################

# CHANGE THE DIRECTORY
twitter_data_path = "../TwitterHashTagData/"
day_path = "data_by_day/"
##########################################################
list_of_files = []

for file in os.listdir(twitter_data_path + day_path):
    if file.endswith(".gz"):
        list_of_files.append(file)
        
num_of_files = len(list_of_files)

hashtag_freq_dict_time = get_freq_dict(0, num_of_files, list_of_files, twitter_data_path + day_path, "day")

N = len(hashtag_freq_dict_time)

jsd1 = np.empty([N, N])
jsd2 = np.empty([N, N])
Dt = np.empty([N, N], dtype = int)
for j in range(N):
    #print(j)
    for i in range(j, N):
        Dt[i, j] = j - i
        Dt[j, i] = i - j
        
        if i == j:
            jsd1[i, j] = 0
            jsd2[i, j] = 0
        else:
            jsd1[i, j] = jsd(hashtag_freq_dict_time[i], hashtag_freq_dict_time[j], alpha = 1.0)
            jsd1[j, i] = jsd1[i, j]
            jsd2[i, j] = jsd(hashtag_freq_dict_time[i], hashtag_freq_dict_time[j], alpha = 2.0)
            jsd2[j, i] = jsd2[i, j]

# Change the directory here
path_out = "../output/JSD/day/"  
#############################################

np.save(path_out + "jsd1.npy", jsd1) 
np.save(path_out + "jsd2.npy", jsd2) 
np.save(path_out + "Dt.npy", Dt)
