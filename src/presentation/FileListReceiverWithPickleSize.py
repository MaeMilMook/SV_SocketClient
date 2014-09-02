'''
Created on 2014. 6. 13.

@author: cho
'''

class FileListReceiverWithPickleSize:
    '''
    classdocs
    '''


    def __init__(self):
        pass
    
    
    def receiveFileList(self, conn):
        import struct, pickle
        
        BUF_SIZE = 12;
        LEN_SIZE_BYTE = 4
        TOTAL_VIEW_SIZE = 0; 
        READ_SIZE = 0;
        
        #recvData = b''        - b''는 바이트니까 b''.join 하면 같은 바이트 타입끼리 조인결성가능
        recvData = []
        
        TOTAL_VIEW_SIZE = struct.unpack('>i', conn.recv(LEN_SIZE_BYTE))[0]
        
        while READ_SIZE < TOTAL_VIEW_SIZE:
            
            restSize = TOTAL_VIEW_SIZE - READ_SIZE
            
            if restSize > BUF_SIZE:
                data = conn.recv(BUF_SIZE)
            else:
                data = conn.recv(restSize)
            
            if not data:
                break
            
            READ_SIZE = READ_SIZE + len(data)
            
            #recvData += data
            recvData.append(data)
        
        fileList = pickle.loads(b''.join(recvData))
        
        #Tuple 타입(viewContent, fileListCount)으로 리턴
        return (fileList, len(fileList))
        