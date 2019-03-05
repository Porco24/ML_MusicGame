import os

def transformAudio2Wav(path):
    os.chdir(path)
    filesPath = os.listdir()
    count = 1
    total = len(filesPath)
    haveWav = 0
    for fileName in filesPath:
        haveWav = 0
        print(fileName)
        for file in os.listdir(fileName):
            if(file.endswith(".wav")):
                haveWav = 1
        if(haveWav == 0):
            for file in os.listdir(fileName):
                if (file.endswith(".ogg")):
                    print(fileName)
                    os.chdir(fileName)
                    print(fileName)
                    os.system("ffmpeg -i \"" + file + "\"" + " \"" + os.path.splitext(file)[0] + "\"" + ".wav")
                    os.chdir("..")
        print("已完成：", count , "/" , total)
        count += 1



transformAudio2Wav("trainData/unzipFile/")
