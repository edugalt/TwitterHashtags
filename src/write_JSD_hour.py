import os, sys, codecs
import numpy as np
import gzip
import pandas as pd

from jsd import *
from general import *


# HOUR SCALE


###########################################################
# CHANGE THE DIRECTORY
twitter_data_path = "../TwitterHashTagData/"
hour_path = "data_by_hour/"
###########################################################

list_of_files = []

for file in os.listdir(twitter_data_path + hour_path):
    if file.endswith(".gz"):
        list_of_files.append(file)
        
num_of_files = len(list_of_files)

hashtag_freq_dict_hour = get_freq_dict(0, num_of_files, list_of_files, twitter_data_path + hour_path, "hour")

N = len(hashtag_freq_dict_hour)

jsd1 = np.empty([N, N])
jsd1[:] = np.nan
jsd2 = np.empty([N, N])
jsd2[:] = np.nan # initializing by having every entry as nan
Dt = np.empty([N, N])
Dt[:] = np.nan
# Since we skip a lot of the hours, it is inconvenient to have the array
# initialized to be full of zeros as this may mislead the reader to think that
# the JSD is 0 which is not true. We merely skipped that index.
for j in range(N):
    for i in range(j, N):
        if np.abs(i - j) in np.power(2, np.arange(0, 15)):
            Dt[i, j] = j - i
            Dt[j, i] = i - j
        
            if i == j:
                jsd1[i, j] = 0
                jsd2[i, j] = 0
            else:
                jsd1[i, j] = jsd(hashtag_freq_dict_hour[i], hashtag_freq_dict_hour[j], alpha = 1.0)
                jsd1[j, i] = jsd1[i, j]
                jsd2[i, j] = jsd(hashtag_freq_dict_hour[i], hashtag_freq_dict_hour[j], alpha = 2.0)
                jsd2[j, i] = jsd2[i, j]

# Change the directory here
path_out = "../output/JSD/hour/"
#############################################

np.save(path_out + "jsd1.npy", jsd1) 
np.save(path_out + "jsd2.npy", jsd2) 
np.save(path_out + "Dt.npy", Dt)
