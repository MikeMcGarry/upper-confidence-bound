#Uppper Confidence Bound

#importing the libraries
#http://pandas.pydata.org/
import pandas as pd
#http://www.numpy.org/
import numpy as np

#Maths
import math

#Reduce function
from functools import reduce

#Step 1: Importing Data
#importing the dataset using pandas
def import_dataset(dataset_name, file_type):
	  dataset = getattr(pd, "read_{}".format(file_type))(dataset_name)
	  return dataset

#Step 1: Importing Data
dataset_name = 'Your dataset name here including file type'
dataset_type = 'File type'
dataset = import_dataset(dataset_name, dataset_type)

#Step 2: Number of selections with iteration
def all_rounds(dataset, number_bandits, total_rounds, default_confidence, default_average):
    number_times = [0] * number_bandits
    sum_reward = [0] * number_bandits
    winner_index = 0
    selected_ad = []
    for i in range(0,total_rounds):
        number_times[winner_index] += 1
        sum_reward[winner_index] += dataset.values[i, winner_index]
        average_reward = []
        confidences = []
        upper_bound = []
        selected_ad.append(winner_index)
        for i in range(0,number_bandits):
            #Error handling in case number_times == 0
            try: 
                average = (sum_reward[i]/number_times[i])
            except:
                average = default_average
            try:
                confidence = math.sqrt(1.5*math.log(i+1)/number_times[i])
            except:
                confidence = default_confidence
                
            average_reward.append(average)
            confidences.append(confidence)
            upper_bound.append(average_reward[i] + confidences[i])
        
        
        winner = max(upper_bound)
        winner_index = upper_bound.index(winner)
        
    return (number_times, sum_reward, selected_ad)
        
result = all_rounds(dataset, len(dataset.columns), len(dataset), 0.5, 0.5)
        
total_score = reduce(lambda x,y: x+y, result[1])  