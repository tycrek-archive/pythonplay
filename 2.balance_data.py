# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

# !!!!! Change training_id to what you used in script 1!
training_id = 'Tycrek001' # The label for the training files.
starting_value = 1 # !!!!! Whatever your training files start with
ending_value = 200 # !!!!! Whatever your training files end with
file_name = 'training_data-{}-{}.npy'.format(training_id, starting_value)


for i in range(starting_value, ending_value + 1): # Iterate through all the training files
    train_data = np.load('training_data-{}-{}.npy'.format(training_id, i))

    df = pd.DataFrame(train_data)
    print(df.head())
    print(Counter(df[1].apply(str)))

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

    np.save('balanced_training_data-{}-{}.npy'.format(training_id, i), final_data)
