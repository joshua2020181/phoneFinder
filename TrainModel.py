import numpy as np
from alexnet import alexnet2
from random import shuffle
import pandas as pd

# use a previous model to begin?
START_FRESH = True

WIDTH = 150
HEIGHT = 100
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'model-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)
EXISTING_MODEL_NAME = ''

model = alexnet2(WIDTH, HEIGHT, LR)
train_data = np.load('C:/Users/joshc/Desktop/Python/Robot/trainingData.npy')
if not START_FRESH:
    model.load(EXISTING_MODEL_NAME)

for i in range(EPOCHS):
##        df = pd.DataFrame(train_data)
##        df = df.iloc[np.random.permutation(len(df))]
##        train_data = df.values.tolist()

    train = train_data[:-50]
    test = train_data[-50:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
        snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

    model.save(MODEL_NAME)

# tensorboard --logdir=foo:C:/Users/H/Desktop/ai-gaming-phase5/log
