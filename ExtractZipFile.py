import zipfile
import os

def unzip(path, unzipPath):
    filePath = os.listdir(path)
    fileNum = len(filePath)
    i = 1
    for file_name in filePath:
        print(file_name)
        file_nameinPath = path + file_name
        if zipfile.is_zipfile(file_nameinPath):
            zipf = zipfile.ZipFile(file_nameinPath)
            zipf.extractall(unzipPath)
            zipf.close()
        print(i,"/", fileNum)
        i += 1

if(zipfile.is_zipfile('zipTest/19-3.zip')):
    print("ok")
unzip("trainData/BeatSaver/", "trainData/unzipFile")
#zipf = zipfile.ZipFile("2681-1870.zip")
#zipf.extractall('zipTest')