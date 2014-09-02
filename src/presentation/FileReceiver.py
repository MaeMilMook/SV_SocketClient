'''
Created on 2014. 5. 27.

@author: cho
'''

import struct

class FileReceiver:
    '''
    classdocs
    '''


    def __init__(self):
        pass

    def receiveFile(self, server):
        
        recvFileSize = self.__getDataLen(server)
        
        buffData = self.__receiveData(server, recvFileSize, 1024)
        
        return buffData
            
            
    def receiveFileListCount(self, server):
        
        fileListCount = self.__getDataLen(server)
        
        return fileListCount
        
    def receiveFileName(self, server):
        
        fileNameLen = self.__getDataLen(server)
        
        buffData = self.__receiveData(server, fileNameLen, fileNameLen)
        
        return ''.join([data.decode('utf-8') for data in buffData])
                    
            
    def __receiveData(self, server, maxLength, buffSize):
        
        BUF_DATA = []
        
        recvLen = 0
        
        if buffSize > maxLength:
            buffSize = maxLength
        
        print('Start receiving', maxLength, 'bytes..')
        
        while recvLen < maxLength:
            
            restSize = maxLength - recvLen
            
            if restSize > buffSize:
                data = server.recv(buffSize)
            else:
                data = server.recv(restSize)
            
            if not data:
                break
            
            recvLen = recvLen + len(data)
            
            BUF_DATA.append(data)
            
        print('End receiving')
        
        return BUF_DATA
        
    def __getDataLen(self, server):
        data = server.recv(4)
        
        dataLen = struct.unpack('>i', data)[0]
        
        return dataLen
        
            