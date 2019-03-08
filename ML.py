from keras.layers import Conv1D, Dense, MaxPool1D, Flatten, TimeDistributed, Activation
from keras.models import Sequential
import numpy as np



train_data = np.loadtxt("song.csv", delimiter=',')
train_data = np.swapaxes(train_data,0,1)
train_data = np.expand_dims(train_data, axis=2)
#train_data = train_data[:, np.newaxis, np.newaxis, :]
# train_data = np.swapaxes(train_data,0,3)

lable_data = np.loadtxt("Expert.csv", delimiter=',')
lable_data = np.expand_dims(lable_data, axis=1)

maxlen = train_data.shape[1]

model = Sequential()
model.add(Conv1D(
    filters=2,
    kernel_size=2,
    input_shape=(maxlen, 1)
))
model.add(Activation('relu'))
model.add(MaxPool1D(
    pool_size=2,
    strides=2,
    padding='same'
))
model.add(Conv1D(
    filters=2,
    kernel_size=2
))
model.add(Activation('relu'))
model.add(MaxPool1D(
    pool_size=2,
    strides=2,
    padding='same'
))
model.add(Flatten())
model.add(Dense(50))
model.add(Activation('relu'))

# Fully connected layer 2 to shape (10) for 10 classes
model.add(Dense(1))
model.add(Activation('softmax'))
model.compile(loss='mse', optimizer='adam')


print(model.summary())


# fit model
model.fit(train_data, lable_data)

