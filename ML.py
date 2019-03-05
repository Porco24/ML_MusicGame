import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
import librosa
import librosa.display
import pylab
import tensorflow as tf
import keras
from keras.layers import TimeDistributed, Dense, Conv2D, MaxPool2D, Dropout, LSTM, Flatten, Activation

time_interval = np.shape()
fzSize = 128
sample = 22050
chanel = 1

model = keras.Sequential()
model.add(TimeDistributed(Conv2D(16, (2, 2), input_shape=(time_interval, fzSize, chanel))))
model.add(TimeDistributed(MaxPool2D((1, 2))))
model.add(TimeDistributed(Activation(activation=tf.nn.relu)))
model.add(TimeDistributed(Dropout(0.3)))
model.add(TimeDistributed(Conv2D(16, (2, 3), input_shape=(time_interval, fzSize))))
model.add(TimeDistributed(MaxPool2D((1, 2))))
model.add(TimeDistributed(Activation(activation=tf.nn.relu)))
model.add(TimeDistributed(Dropout(0.3)))
model.add(TimeDistributed(Flatten()))
model.add(LSTM(64, activation=tf.nn.tanh, return_sequences=True))
model.add(Dense(6720))
model.add(Activation(tf.nn.tanh))
model.add(Dense(2))
model.add(Activation(tf.nn.relu))

# model.build()
# model.summary()

model.fit()


# history = model.fit([new_train_data, new_div_data], new_train_labels, epochs=EPOCHS,
#                         validation_split=0.2, verbose=0, #batch_size=10,
#                         callbacks=[early_stop, PrintDot()])