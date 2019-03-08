from keras.layers import Conv1D, Dense, MaxPool1D, MaxPooling1D, Flatten, TimeDistributed , Activation, Dropout, LSTM, Input, BatchNormalization
from keras.models import Model
import numpy as np



train_data = np.loadtxt("song.csv", delimiter=',')
train_data = np.swapaxes(train_data,0,1)
train_data = np.expand_dims(train_data, axis=2)
#train_data = train_data[:, np.newaxis, np.newaxis, :]
# train_data = np.swapaxes(train_data,0,3)

lable_data = np.loadtxt("Expert.csv", delimiter=',')
lable_data = np.expand_dims(lable_data, axis=1)




X = np.loadtxt("test_song.csv", delimiter=',')
X = np.swapaxes(X,0,1)
X = np.expand_dims(X, axis=2)

Y = np.loadtxt("test_pu.csv", delimiter=',')
Y = np.expand_dims(Y, axis=1)

X1 = np.loadtxt("test_song1.csv", delimiter=',')
X1 = np.swapaxes(X1,0,1)
X1 = np.expand_dims(X1, axis=2)

Y1 = np.loadtxt("test_pu1.csv", delimiter=',')
Y1 = np.expand_dims(Y1, axis=1)





maxlen = train_data.shape[1]



model_input = Input(shape=(maxlen, 1), name='input')
layer = model_input
layer = Conv1D(filters=40,
               kernel_size=10,
               padding='valid',
               activation='relu')(layer)
layer = BatchNormalization(axis=2)(layer)
layer = MaxPooling1D(pool_size=40,
                     padding='same')(layer)
layer = Dropout(0.3)(layer)
layer = LSTM(40, return_sequences=True,
             activation="tanh")(layer)
layer = Dropout(0.3)(layer)
layer = Flatten()(layer)
layer = Dense(40, activation = 'relu')(layer)
#layer = BatchNormalization(axis = 2)(layer)
layer = (Dense(1))(layer)
model = Model(model_input, layer)

model.compile(loss='mse', optimizer='adam')

print(model.summary())

# fit model
print('------------Training------------')
model.fit(train_data, lable_data)

print('------------Test------------')
cost = model.evaluate(X, Y)
print('test coast:', cost)

cost = model.evaluate(X1, Y1)
print('test coast:', cost)
