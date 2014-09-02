'''
Created on 2014. 5. 27.

@author: cho
'''
import os

class FileWriter:
    '''
    classdocs
    '''


    def __init__(self):
        pass
        
    def putFile(self, fullFilePath, rawFile):
        
        dirName = os.path.dirname(fullFilePath)
        
        #디렉토리 생성
        if not self.__checkDir(dirName):
            self.__makeDirPath(dirName)
        
        file = open(fullFilePath, mode='wb')
        
        print(fullFilePath ,'에 전송시작...')
        
        for data in rawFile:
            
            file.write(data)
        
            #쓰레드로 다시 처리
            #print(round(RECV_LEN/recvFileSize*100, 2), '%..전송중')
        
        file.close()
        
        print('**', fullFilePath, '전송완료**')
        
    def __checkDir(self, dirName):
        return os.path.exists(dirName)
    
    def __makeDirPath(self, dirPath):
        dividedPath = os.path.split(dirPath)
        
        if not self.__checkDir(dividedPath[0]):
            self.__makeDirPath(dividedPath[0])
        
        os.mkdir(dirPath)
            
        
        
        