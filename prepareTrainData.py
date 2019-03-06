import numpy as np
import librosa
import librosa.display
import json
import os

def getNotes(path):
    os.chdir(path)
    filePath = os.listdir()
    count = 1
    total = len(filePath)
    songLen = 0
    for fileName in os.listdir():
        print(fileName)
        os.chdir(fileName)
        for file in os.listdir():
            #获取歌曲长度
            if (os.path.splitext(file)[-1] == ".wav"):
                for fileFindSongCsv in os.listdir():
                    if (fileFindSongCsv == os.path.splitext(file)[0]+".csv"):
                        S = np.loadtxt(fileFindSongCsv,delimiter=',')
                        songLen = S.shape[1]
                        print(songLen)
        for file in os.listdir():
            if (os.path.splitext(file)[-1] == ".json" and os.path.splitext(file)[0] != 'info'):
                print(file)
                with open(file , 'r') as f:
                    data = json.load(f)
                bpm = data['_beatsPerMinute']
                notes = data['_notes']
                # 歌曲每个节拍点所对应的真实歌曲时间
                times = []
                # 歌曲每个节拍点所对应的Beat Saver中的时间
                BS_time = []
                #存储csv格式
                csvFormat = np.zeros((1,songLen))
                for note in notes:
                    if not (BS_time):
                        i = int((note['_time'] * 60 / bpm)*22050/512)
                        if (i >= songLen):
                            break
                        csvFormat[0][i] = 1
                        BS_time.append(note['_time'])
                    elif (note['_time'] != BS_time[-1]):
                        i = int((note['_time'] * 60 / bpm)*22050/512)
                        if(i >=songLen):
                            break
                        csvFormat[0][i] = 1
                        BS_time.append(note['_time'])
                haveCsv = 0
                #判断是否已经存在要生成的Csv文件
                for Csvfile in os.listdir():
                    if (Csvfile != (os.path.splitext(file)[0] + ".csv") == Csvfile):
                        haveCsv = 1
                if(haveCsv == 0):
                    np.savetxt(os.path.splitext(file)[0] + ".csv", csvFormat, delimiter=',')
        print("已完成文件夹数：",count,"/",total)
        count += 1
        os.chdir("..")

def Wav2Csv(path):
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
                        print(fileCsv)
                        haveCsv = 1
                if(haveCsv == 0):
                    data, sample = librosa.load(file)
                    S = librosa.feature.melspectrogram(y=data, sr=sample)
                    np.savetxt(os.path.splitext(file)[0]+".csv", S, delimiter=',')
        print("已完成：",count,"/",total)
        count += 1
        os.chdir("..")

def findMaxAudio(path):
    os.chdir(path)
    filePath = os.listdir()
    count = 1
    total = len(filePath)
    maxAudio = 0
    maxAudioName = "none"
    L = []
    for fileName in os.listdir():
        print(fileName)
        os.chdir(fileName)
        for file in os.listdir():
            if (os.path.splitext(file)[-1] == ".csv"):
                print("OK")
        print("已完成：",count,"/",total)
        count += 1
        os.chdir("..")
    print("maxAudioName:",maxAudioName)
    print("maxAudio=",maxAudio)
    print(L)

def delNoteCsv(path):
    os.chdir(path)
    filePath = os.listdir()
    count = 1
    total = len(filePath)
    for fileName in os.listdir():
        print(fileName)
        os.chdir(fileName)
        for file in os.listdir():
            if (os.path.splitext(file)[-1] == ".wav"):
                name = os.path.splitext(file)[0]
                for fileAngin in os.listdir():
                    if (os.path.splitext(fileAngin)[-1] == ".csv" and os.path.splitext(fileAngin)[0] != name):
                        os.remove(fileAngin)
        print("已完成：",count,"/",total)
        count += 1
        os.chdir("..")

getNotes("trainData/unzipFile")