# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import rhash


# !!!!! Change training_id to what you used in script 1!
training_id = 'BarnabusX002' # The label for the training files.
starting_value = 1 # !!!!! Whatever your training files start with
ending_value = 4 # !!!!! Whatever your training files end with
file_name = 'training_data-{}-{}.npy'.format(training_id, starting_value)

TRIM_SIZE = 4 # !!!!! Must be a factor of SAVE_INTERVAL in script 1
TAKE_TOP = 6


for i in range(starting_value, ending_value + 1): # Iterate through all the training files
    train_data = np.load('training_data-{}-{}.npy'.format(training_id, i))

    # Display info for data set
    #df = pd.DataFrame(train_data)
    #print(df.head())
    #print(Counter(df[1].apply(str)))


    # My attempt at trimming data (bad)
    #shuffle(train_data)
    #final_data = []
    #for i2 in range(0, len(train_data), TRIM_SIZE):
    #    final_data.append(train_data[i2])

    #shuffle(final_data)
    #

    # My attempt at balancing data
    #key_classes = {}
	#for key_class in train_data:
    #	key_class = key_class[1]
    #	if rhash.rhash(str(key_class)) in key_classes:
    #	    key_classes[rhash.rhash(str(key_class))] += 1
    #	else:
    #		key_classes[rhash.rhash(str(key_class))] = 1
    classes = []
    for data in train_data:
    	classes.append(data[1])
    print(classes)
    print(len(classes))
    input()





    '''
    lefts = []
    rights = []
    forwards = []

    shuffle(train_data)

    for data in train_data:
        img = data[0]
        choice = data[1]

        if choice == [1,0,0]:
            lefts.append([img,choice])
        elif choice == [0,1,0]:
            forwards.append([img,choice])
        elif choice == [0,0,1]:
            rights.append([img,choice])
        else:
            print('no matches')


    forwards = forwards[:len(lefts)][:len(rights)]
    lefts = lefts[:len(forwards)]
    rights = rights[:len(forwards)]

    final_data = forwards + lefts + rights
    shuffle(final_data)
    '''

    #np.save('trimmed_training_data-{}-{}.npy'.format(training_id, i), final_data)
