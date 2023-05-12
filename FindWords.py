#!/usr/bin/python
import numpy as np  

## Read in dictionary
dictionary = np.genfromtxt('dictionary.txt', dtype='str')
print("%d words in dictionary" % len(dictionary))

## Subset of words without 's' and with 7 or fewer letters
bee_words = [word for word in dictionary if \
             len(word) >= 4 and 's' not in word and len(set(word)) <= 7]

print("%d possible words found" % len(bee_words))

## Print out the longest words
max_length = len(max(bee_words, key=len))
longest_words = [word for word in bee_words if len(word) == max_length]

print("Longest words:", longest_words)
