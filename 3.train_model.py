# train_model.py

import numpy as np
from alexnet import alexnet

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
# !!!!! Change training_id to what you used in script 1 and script 2!
training_id = 'Tycrek001'
MODEL_NAME = 'pythonplay-{}-{}-epochs.model'.format(training_id,EPOCHS)
LOAD_PREVIOUS_MODEL = False # if you want to improve an existing model, change to true

BATCH_SIZE = 32 # Smaller = less RAM used; Larger = finishes quicker


model = alexnet(WIDTH, HEIGHT, LR)

if LOAD_PREVIOUS_MODEL:
    model.load(MODEL_NAME)
    print("Loaded previous model!")

train_files_end = 200 # how many training files you have
end_count = EPOCHS * train_files_end
count = 1
for i in range(EPOCHS):
    for i in range(1, train_files_end + 1):
        print("\n\nStep " + str(count) + "/" + str(end_count))
        train_data = np.load('balanced_training_data-{}-{}.npy'.format(training_id, i))
        #train_data = np.load('training_data.npy')

        train = train_data[:-100]
        test = train_data[-100:]

        X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
        Y = [i[1] for i in train]

        test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
            snapshot_step=500, show_metric=True, run_id=MODEL_NAME, batch_size=BATCH_SIZE)

        model.save(MODEL_NAME)
        count += 1



# tensorboard --logdir=foo:C:/path/to/log