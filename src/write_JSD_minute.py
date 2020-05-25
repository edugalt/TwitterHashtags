import os, sys, codecs
import numpy as np
import gzip
import pandas as pd
import random

from jsd import *
from general import *

# MINUTE SCALE

random.seed(2020)

###########################################################
# CHANGE THE DIRECTORY
twitter_data_path = "../twitterHashtags/"
min_path = "data_by_minute/"
###########################################################

list_of_files = []

for file in os.listdir(twitter_data_path + min_path):
    if file.endswith(".gz"):
        list_of_files.append(file)
        
num_of_files = len(list_of_files)

random_total = 5000        # choose 5000 minute files at random
random_order = random.sample(range(num_of_files), random_total) 

hashtag_freq_dict_min = get_freq_dict(0, num_of_files, list_of_files, twitter_data_path + min_path, "min")

jsd1 = np.empty([random_total, random_total])
jsd2 = np.empty([random_total, random_total])
Dt = np.empty([random_total, random_total], dtype = int)

for j in range(random_total):
    for i in range(j, random_total):
        Dt[i, j] = random_order[j] - random_order[i]
        Dt[j, i] = random_order[i] - random_order[j]
        if random_order[i] == random_order[j]:
            jsd1[i, j] = 0
            jsd2[i, j] = 0
        else:
            jsd1[i, j] = jsd(hashtag_freq_dict_min[random_order[i]], hashtag_freq_dict_min[random_order[j]], alpha = 1.0)
            jsd1[j, i] = jsd1[i, j]
            jsd2[i, j] = jsd(hashtag_freq_dict_min[random_order[i]], hashtag_freq_dict_min[random_order[j]], alpha = 2.0)
            jsd2[j, i] = jsd2[i, j]

# Change the directory here
path_out = "../output/JSD/min/"
#############################################

np.save(path_out + "jsd1.npy", jsd1) 
np.save(path_out + "jsd2.npy", jsd2) 
np.save(path_out + "Dt.npy", Dt)
np.save(path_out + "random_order.npy", random_order)
