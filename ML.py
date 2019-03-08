from keras.layers import Conv1D, Dense, MaxPooling1D, Flatten, Dropout, LSTM, Input, BatchNormalization, TimeDistributed
from keras.models import Model
from keras.models import load_model
import numpy as np
import os



train_data = np.loadtxt("song.csv", delimiter=',')
train_data = np.swapaxes(train_data,0,1)
train_data = np.expand_dims(train_data, axis=2)
#train_data = train_data[:, np.newaxis, np.newaxis, :]
# train_data = np.swapaxes(train_data,0,3)

lable_data = np.loadtxt("Expert.csv", delimiter=',')
lable_data = np.expand_dims(lable_data, axis=1)




# X = np.loadtxt("test_song.csv", delimiter=',')
# X = np.swapaxes(X,0,1)
# X = np.expand_dims(X, axis=2)
#
# Y = np.loadtxt("test_pu.csv", delimiter=',')
# Y = np.expand_dims(Y, axis=1)
#
# X1 = np.loadtxt("test_song1.csv", delimiter=',')
# X1 = np.swapaxes(X1,0,1)
# X1 = np.expand_dims(X1, axis=2)
#
# Y1 = np.loadtxt("test_pu1.csv", delimiter=',')
# Y1 = np.expand_dims(Y1, axis=1)





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
#layer = BatchNormalization(axis = 1)(layer)
layer = Dense(1)(layer)
model = Model(model_input, layer)

model.compile(loss='mse', optimizer='adam')

print(model.summary())

# fit model
# print('------------Training------------')
# model.fit(train_data, lable_data)
# model.fit(X, Y)
#
# print('------------Test------------')
# cost = model.evaluate(X, Y)
# print('test coast:', cost)
#
# cost = model.evaluate(X1, Y1)
# print('test coast:', cost)


def fitMode(path, rate):
    os.chdir(path)
    filePath = os.listdir()
    count = 1
    total = len(filePath)
    for fileName in os.listdir():
        print(fileName)
        os.chdir(fileName)
        haveCsv = 0
        for file in os.listdir():
            if (os.path.splitext(file)[-1] == ".wav"):
                songName = os.path.splitext(file)[0]
                for fileCsv in os.listdir():
                    if (fileCsv == songName + ".csv"):
                        X = np.loadtxt(fileCsv, delimiter=',')
                        X = np.swapaxes(X, 0, 1)
                        X = np.expand_dims(X, axis=2)
                    elif (os.path.splitext(fileCsv)[-1] == ".csv"):
                        Y = np.loadtxt(fileCsv, delimiter=',')
                        Y = np.expand_dims(Y, axis=1)
                if(float(count/total) < rate):
                    model=load_model('test.h5')
                    print('------------Training------------')
                    model.fit(X, Y)
                    model.save('test.h5')
                    del model
                # else:
                #     print('------------Test------------')
                #     model = load_model('test.h5')
                #     cost = model.evaluate(X, Y)
                #     print('test coast:', cost)
                #     del model
        print("已完成：", count, "/", total)
        count += 1
        os.chdir("..")

def loadData(path):
    X = np.zeros((1, 128, 1))
    Y = np.ndarray((1, 1))
    os.chdir(path)
    filePath = os.listdir()
    count = 1
    total = len(filePath)
    for fileName in os.listdir():
        print(fileName)
        os.chdir(fileName)
        haveCsv = 0
        for file in os.listdir():
            if (os.path.splitext(file)[-1] == ".wav"):
                songName = os.path.splitext(file)[0]
                for fileCsv in os.listdir():
                    if (fileCsv == songName + ".csv"):
                        data = np.loadtxt(fileCsv, delimiter=',')
                        data = np.swapaxes(data,0,1)
                        data = np.expand_dims(data, axis=2)
                        X = np.concatenate((X, data), axis=0)
                        del data
                    elif (os.path.splitext(fileCsv)[-1] == ".csv"):
                        data = np.loadtxt(fileCsv, delimiter=',')
                        data = np.expand_dims(data, axis=1)
                        Y = np.concatenate((Y, data), axis=0)
                        del data
                        break
        print("已完成：", count, "/", total)
        count += 1
        os.chdir("..")
    return X, Y


X, Y = loadData("trainData/unzipFile")
X_train = X[:200]
Y_train = Y[:200]
X_test = X[200:]
Y_test = Y[200:]

#fit model
print('------------Training------------')
model.fit(X_train, Y_train)

print('------------Test------------')
cost = model.evaluate(X_test, Y_test)
print('test coast:', cost)