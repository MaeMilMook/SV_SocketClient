'''
Created on 2014. 5. 27.

@author: cho
'''

class FileListReceiver:


    def __init__(self, endMsg):
        self.__endMsg = endMsg
    
    def receiveFileList(self, conn):
        import struct
        
        BUF_DATA = []
        data = ''
        
        FILE_LIST_CNT = struct.unpack('>i', conn.recv(4))[0]
        
        while True:
            data = conn.recv(1024)
            
            decodedData = data.decode('UTF-8')
            
            if self.__endMsg in decodedData:
                BUF_DATA.append(decodedData[:decodedData.find(self.__endMsg)])
                break
            
            if not data:
                break
            
            BUF_DATA.append(decodedData)
            
        return (''.join(BUF_DATA), FILE_LIST_CNT) 