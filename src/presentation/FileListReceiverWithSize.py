'''
Created on 2014. 6. 5.

@author: cho
'''

class FileListReceiverWithSize:
    '''
    classdocs
    '''


    def __init__(self):
        pass
    
    def receiveFileList(self, conn):
        
        import struct
        
        BUF_SIZE = 1024;
        LEN_SIZE_BYTE = 4
        TOTAL_VIEW_SIZE = 0; 
        READ_SIZE = 0;
        
        BUF_DATA = []
        
        TOTAL_VIEW_SIZE = struct.unpack('>i', conn.recv(LEN_SIZE_BYTE))[0]
        FILE_LIST_CNT = struct.unpack('>i', conn.recv(LEN_SIZE_BYTE))[0]
        
        while READ_SIZE < TOTAL_VIEW_SIZE:
            
            data = conn.recv(BUF_SIZE)
            
            if not data:
                break
            
            READ_SIZE = READ_SIZE + len(data)
            
            decodedData = data.decode('UTF-8')
            
            BUF_DATA.append(decodedData)
        
        #Tuple 타입(viewContent, fileListCount)으로 리턴
        #View생성을 Client에서가 맞는지 Server에서가 맞는지 고민할것
        return (''.join(BUF_DATA), FILE_LIST_CNT)
        