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
    for fileName in os.listdir():
        print(fileName)
        os.chdir(fileName)
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
                for note in notes:
                    if not (BS_time):
                        times.append(note['_time'] * 60 / bpm)
                        BS_time.append(note['_time'])
                        print("Times:", note['_time'] * 60 / bpm, " ,BS_Time:", note['_time'])
                    elif (note['_time'] != BS_time[-1]):
                        times.append(note['_time'] * 60 / bpm)
                        BS_time.append(note['_time'])
                        print("Times:", note['_time'] * 60 / bpm, " ,BS_Time:", note['_time'])
                print("已完成：",count,"/",total)
                count += 1
        os.chdir("..")

getNotes("trainData/unzipFile/")