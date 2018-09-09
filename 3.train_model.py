# train_model.py

import numpy as np
from alexnet import alexnet

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
training_id = ''
MODEL_NAME = 'pythonplay-{}-{}-epochs.model'.format(training_id,EPOCHS)
LOAD_PREVIOUS_MODEL = False # if you want to improve an existing model, change to true


model = alexnet(WIDTH, HEIGHT, LR)

if LOAD_PREVIOUS_MODEL:
	model.load(MODEL_NAME)
	print("Loaded previous model!")

train_files_end = 15 # how many training files you have
for i in range(EPOCHS):
    for i in range(1,train_files_end+1):
        train_data = np.load('balanced_training_data-{}-{}.npy'.format(training_id, i))
        #train_data = np.load('training_data.npy')

        train = train_data[:-100]
        test = train_data[-100:]

        X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
        Y = [i[1] for i in train]

        test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
            snapshot_step=500, show_metric=True, run_id=MODEL_NAME, batch_size=32)

        model.save(MODEL_NAME)



# tensorboard --logdir=foo:C:/path/to/log