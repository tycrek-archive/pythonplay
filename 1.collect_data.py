# create_training_data.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
from keydefs import keylist


## Convert our input keys to an array for Numpy
## [A,W,D] boolean values
#! TO-DO: Add more keys
def keys_to_output(keys): #                                        26
    output = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0, 0,0,0,0,0,0,0,0,0,0]
    

    for key in keylist:
    	if key in keys:
    		if key.isalpha():
    			output[ord(key) - 65] = 1 # Any letter
    		elif key == " ":
    			output[26] = 1 # Space bar
    		elif key.isdigit():
    			output[(ord(key) - 48) + 27] = 1
    return output

'''
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output
'''

# !!!!! Change training_id to whatever you want, but keep it consistent in script 2 and script 3!
training_id = 'Tycrek001' # The label for the training files.
starting_value = 1 # The index to start naming training files with.
file_name = 'training_data-{}-{}.npy'.format(training_id, starting_value)
training_data = []

SAVE_INTERVAL = 5000 # How many frames to take before saving


while(True): # Check if the current training files exist and make a new start value.
    if os.path.isfile(file_name):
        print("File exists, increasing start!")
        starting_value += 1
        file_name = 'training_data-{}-{}.npy'.format(training_id, starting_value)
    else:
        break


def main():

    print("\n\nStarting in 5")
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    
    global training_data
    global file_name
    global starting_value
    global training_id
    global SAVE_INTERVAL

    while(True):

        if not paused:
            # 800x600 windowed mode
            screen = grab_screen(region=(0,40,800,640)) # Take a screenshot
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160,120)) # Resize the screenshot to something more reasonable for a NN

            keys = key_check()
            output = keys_to_output(keys)

            training_data.append([screen,output])
            
            if len(training_data) % 100 == 0:
                print(len(training_data))

            if len(training_data) % SAVE_INTERVAL == 0:
                print('Saved data in file  ' + file_name)
                np.save(file_name,training_data)
                starting_value += 1
                training_data = []
                file_name = 'training_data-{}-{}.npy'.format(training_id, starting_value)

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('Unpaused!')
                time.sleep(1)
            else:
                print('Paused!')
                paused = True
                time.sleep(1)


main()