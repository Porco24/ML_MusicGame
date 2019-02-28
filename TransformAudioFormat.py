import os

def transformAudio2Wav(path):
    os.chdir(path)
    filesPath = os.listdir()
    count = 1
    total = len(filesPath)
    for fileName in filesPath:
        print(fileName)
        for file in os.listdir(fileName):
            if(os.path.splitext(file)[-1] == ".ogg"):
                print(fileName)
                os.chdir(fileName)
                os.system("ffmpeg -i " + file + " " + os.path.splitext(file)[0] + ".wav" )
                os.chdir("..")
        print("已完成：", count , "/" , total)
        count += 1



transformAudio2Wav("trainData/unzipFile/")
