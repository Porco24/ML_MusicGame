from keras.layers import Conv1D, Dense, MaxPooling1D, Flatten, Dropout, LSTM, Input, BatchNormalization, MaxPool1D
from keras.models import Model, Sequential
from keras.models import load_model
import numpy as np
import os
import librosa



# train_data = np.loadtxt("song.csv", delimiter=',')
# train_data = np.swapaxes(train_data,0,1)
# train_data = np.expand_dims(train_data, axis=2)
# #train_data = train_data[:, np.newaxis, np.newaxis, :]
# # train_data = np.swapaxes(train_data,0,3)
#
# lable_data = np.loadtxt("Expert.csv", delimiter=',')
# lable_data = np.expand_dims(lable_data, axis=1)




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




model = Sequential()
model.add(Conv1D(filters=40,
               kernel_size=5,
               padding='valid',
               activation='relu',
                input_shape=(128, 1)))
model.add(MaxPooling1D(pool_size = 6,
                       padding='same'))
model.add(Conv1D(filters=40,
               kernel_size=5,
               padding='valid',
               activation='relu'))
model.add(MaxPooling1D(pool_size=6,
                     padding='same'))
model.add(BatchNormalization(axis=2))
model.add(Dropout(0.3))
model.add(LSTM(40, return_sequences=True,
             activation="tanh"))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(40, activation = 'relu'))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')





# model_input = Input(shape=(128, 1), name='input')
# layer = model_input
# layer = Conv1D(filters=40,
#                kernel_size=5,
#                padding='valid',
#                activation='relu')(layer)
# layer = MaxPooling1D(pool_size=6,
#                      padding='same')(layer)
# layer = Conv1D(filters=40,
#                kernel_size=5,
#                padding='valid',
#                activation='relu')(layer)
# layer = BatchNormalization(axis=2)(layer)
# layer = MaxPooling1D(pool_size=6,
#                      padding='same')(layer)
# layer = Dropout(0.3)(layer)
# layer = LSTM(40, return_sequences=True,
#              activation="tanh")(layer)
# layer = Dropout(0.3)(layer)
# layer = Flatten()(layer)
# layer = Dense(40, activation = 'relu')(layer)
# #layer = BatchNormalization(axis = 1)(layer)
# layer = Dense(1)(layer)
# model = Model(model_input, layer)
#
# model.compile(loss='mse', optimizer='adam')

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

def loadData(path, rate):
    X_train = np.zeros((1, 128, 1))
    Y_train = np.ndarray((1, 1))
    X_test = np.zeros((1, 128, 1))
    Y_test = np.ndarray((1, 1))
    os.chdir(path)
    filePath = os.listdir()
    count = 1
    total = len(filePath)
    for fileName in os.listdir():
        print(fileName)
        os.chdir(fileName)
        hasY = 0
        for file in os.listdir():
            if(rate >= float(count / total)):
                break
            if (os.path.splitext(file)[-1] == ".wav"):
                songName = os.path.splitext(file)[0]
                for fileCsv in os.listdir():
                    if (fileCsv == songName + ".csv"):
                        data = np.loadtxt(fileCsv, delimiter=',')
                        data = np.swapaxes(data,0,1)
                        data = np.expand_dims(data, axis=2)
                        if (rate >= float(count / total)):
                            None
                            #X_train = np.concatenate((X_train, data), axis=0)
                        else:
                            X_test = np.concatenate((X_test, data), axis=0)
                        del data
                    elif (os.path.splitext(fileCsv)[-1] == ".csv" and hasY == 0):
                        data = np.loadtxt(fileCsv, delimiter=',')
                        data = np.expand_dims(data, axis=1)
                        if (rate >= float(count / total)):
                            None
                            #Y_train = np.concatenate((Y_train, data), axis=0)
                        else:
                            Y_test = np.concatenate((Y_test, data), axis=0)
                        del data
                        hasY = 1
        print("已完成：", count, "/", total)
        count += 1
        os.chdir("..")
    return X_train, Y_train, X_test, Y_test


# X_train, Y_train, X_test, Y_test = loadData("trainData/unzipFile", 0.8)
# #np.save('X_train.npy', X_train)
# #np.save('Y_train.npy', Y_train)
# np.save('X_test.npy', X_test)
# np.save('Y_test.npy', Y_test)
#
# #fit model
# print('------------Training------------')
# model.fit(X_train, Y_train)
#
# print('------------Test------------')
# cost = model.evaluate(X_test, Y_test)
# print('test coast:', cost)
# print('complete')

X_train = np.load('X_train.npy')
Y_train = np.load('Y_train.npy')

model.fit(X_train, Y_train)
model.save('first.h5')
#
# print('------------Test------------')
# cost = model.evaluate(X_test, Y_test)
# print('test coast:', cost)

# data, sample = librosa.load('song.wav')
# S = librosa.feature.melspectrogram(y=data, sr=sample)
# S = np.swapaxes(S, 0, 1)
# S = np.expand_dims(S, axis=2)
# myModel = load_model('first.h5')
# predictions = myModel.predict_classes(S)
# find1 = []
# for i in predictions:
#     if(i==1):
#         find1.append(i)
# print(find1)
# print(predictions)