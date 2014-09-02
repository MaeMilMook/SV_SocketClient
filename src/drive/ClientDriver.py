'''
Created on 2014. 5. 25.

@author: cho
'''

from dom.ClientFileManage import ClientFileManager
from connector.SocketFileServerConnector import SocketFileServerConnector
from presentation.FileInfoReceiver import FileInfoReceiver
from presentation.FileReceiver import FileReceiver
from presentation.FileListReceiverWithSize import FileListReceiverWithSize
from presentation.FileListReceiver import FileListReceiver
from dom.FileWriter import FileWriter
from presentation.FileListReceiverWithPickleSize import FileListReceiverWithPickleSize

if __name__ == '__main__':
    
    ''' Configuration Start'''
    #Domain
    clientFileManager = ClientFileManager('C:\\receivedFiles\\')
    clientFileManager.setFileWriter(FileWriter())
    
    fileServerConnector = SocketFileServerConnector()

    #fileListReceiver = FileListReceiverWithSize()
    fileListReceiver = FileListReceiverWithPickleSize()
    
    fileReceiver = FileReceiver()
    
    fileInfoReceiver = FileInfoReceiver(fileServerConnector, fileListReceiver, fileReceiver)
    fileInfoReceiver.setClientFileManager(clientFileManager)
    ''' Configuration End'''
    
    
    print('::::::::Start Client::::::::')
    fileInfoReceiver.runClientToReceiveFile('127.0.0.1', 8889)
    print('::::::::End Client::::::::')


