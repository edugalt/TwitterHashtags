import numpy as np

########################################################################################
# Function that calculates alpha-entropy of a word/hashtag frequency dictionary (wfd).
def H(wfd, alpha = 2.0):
    freqs = np.array(list(wfd.values()))
    if alpha != 1:
        return (np.sum(np.power(freqs,alpha))-1)/(1 - alpha)
    else:
        return -1*np.sum(np.log(freqs)*freqs)

########################################################################################
# Function that joins two word/hashtag frequency dictionaries together
def joinwfds(wfd1, wfd2):
    allWords = list(set(list(wfd1.keys())+list(wfd2.keys())))
    #Combine the keys of the two dictionaries
    wfd12 = {}
    # Averaging the frequencies of the words
    for w in allWords:
        wfd12[w] = 0.0
        if w in wfd1:
            wfd12[w] = wfd12[w] + wfd1[w]/2
        if w in wfd2:
            wfd12[w] = wfd12[w] + wfd2[w]/2
    return(wfd12)

########################################################################################
# Function that returns the Jensen-Shannon Divergence between frequency distributions    
def jsd(wfd1, wfd2, alpha = 2.0):
    wfd12 = joinwfds(wfd1, wfd2)
    return H(wfd12, alpha) - 0.5 * H(wfd1, alpha) - 0.5 * H(wfd2, alpha)
