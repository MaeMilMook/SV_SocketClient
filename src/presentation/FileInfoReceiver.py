'''
Created on 2014. 5. 28.

@author: cho
'''

class FileInfoReceiver:
    '''
    classdocs
    '''

    def __init__(self, connector ,fileListReceiver, fileReceiver):
        self.__connector = connector
        self.__fileListReceiver = fileListReceiver
        self.__fileReceiver = fileReceiver
    
    
    def runClientToReceiveFile(self, ip, port):
        
        self.__connectFileServer(ip, port)
        
        #receive File List(Presentation)
        fileListInfo = self.__fileListReceiver.receiveFileList(self.__conn)
        
        #Show a Received File List
        self.__showFileList(fileListInfo[0])
        
        #inputFile index From User
        inputIdx = self.__clientFileManager.inputFileIndex(fileListInfo[0])
        
        self.__requestFileByFileIndex(inputIdx)
        
        if self.__isDownloadFile(inputIdx):
            
            self.__receiveFileFromServer()
        
        self.__conn.close()
        
    
    def __connectFileServer(self, ip, port):
        conn = self.__connector.connectToServer(ip, port)
        self.__conn = conn
        
    def __requestFileByFileIndex(self, fileIndex):
        
        import struct
        self.__conn.sendall(struct.pack('>i', fileIndex))
        
    def __receiveFileFromServer(self):
        
        fileListCount = self.__fileReceiver.receiveFileListCount(self.__conn)
        
        for i in range(fileListCount):
            fileName = self.__fileReceiver.receiveFileName(self.__conn)
        
            rawFileData = self.__fileReceiver.receiveFile(self.__conn)
        
            self.__clientFileManager.putFile(fileName, rawFileData)
        
    def __showFileList(self, fileList):
        import os
        
        fileMenuList = []
        fileMenuList.append('===Sever File List===\r\n')
        fileMenuList.append('\tNumber\tFileName\tSize(KB)')
        fileMenuList.append('\r\n')
       
        self.__makeFileListToShow(fileList, fileMenuList)
        
        print(''.join(fileMenuList))
        
        
    def __makeFileListToShow(self, fileList, fileMenuList):
        import os
        
        for idx, fileInfo in enumerate(fileList):
            
            baseName = os.path.basename(fileInfo['name'])
            depth = fileInfo['depth']
            
            fileMenuList.append('\t')
            fileMenuList.append(str(idx))
            fileMenuList.append('\t'*depth)
            fileMenuList.append('|--\t')
            fileMenuList.append(baseName)
            fileMenuList.append('\t')
            fileMenuList.append(str(fileInfo['size']))
            fileMenuList.append('\r\n')
            
        
    
    def __isDownloadFile(self, answer):
        return answer >= 0
    
    def setClientFileManager(self, clientFileManager):
        self.__clientFileManager = clientFileManager
        
        