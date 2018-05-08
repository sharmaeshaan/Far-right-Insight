import os

def getfiles():
    # list all files in working dir
    dirlist = os.listdir(path='./')
    # place all content in list
    files = list()
    for f in dirlist:
        if f.endswith('.txt')
        fhand = open(f, mode='r')
        files.append(fhand.read())
    return files