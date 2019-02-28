import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
import librosa
import librosa.display
import pylab
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    ##
])


def build_model():
    model1 = keras.Sequential([
        keras.layers.TimeDistributed(keras.layers.Conv2D(16, (2, 2),
                                                         data_format='channels_last'),
                                     input_shape=(time_interval, train_shape[1], train_shape[2], train_shape[3])),
        keras.layers.TimeDistributed(keras.layers.MaxPool2D((1, 2),
                                                            data_format='channels_last')),
        keras.layers.TimeDistributed(keras.layers.Activation(activation=tf.nn.relu)),
        keras.layers.TimeDistributed(keras.layers.Dropout(0.3)),
        keras.layers.TimeDistributed(keras.layers.Conv2D(16, (2, 3),
                                                         data_format='channels_last')),
        keras.layers.TimeDistributed(keras.layers.MaxPool2D((1, 2),
                                                            data_format='channels_last')),
        keras.layers.TimeDistributed(keras.layers.Activation(activation=tf.nn.relu)),
        keras.layers.TimeDistributed(keras.layers.Dropout(0.3)),
        keras.layers.TimeDistributed(keras.layers.Flatten()),
        keras.layers.LSTM(64, activation=tf.nn.tanh, return_sequences=True)
    ])

    input2 = keras.layers.InputLayer(input_shape=(time_interval, div_shape[1]));

    conc = keras.layers.concatenate([model1.output, input2.output]);
    dense1 = keras.layers.Dense(71, activation=tf.nn.tanh)(conc);
    dense2 = keras.layers.Dense(71, activation=tf.nn.relu)(dense1);
    dense3 = keras.layers.Dense(label_shape[1], activation=tf.nn.tanh)(dense2);

    optimizer = tf.train.RMSPropOptimizer(0.001);

    final_model = tf.keras.models.Model(inputs=[model1.input, input2.input], outputs=dense3);
    final_model.compile(loss='mse',
                        optimizer=optimizer,
                        metrics=[keras.metrics.mae])
    return final_model