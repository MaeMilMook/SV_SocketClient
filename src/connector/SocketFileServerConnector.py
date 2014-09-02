'''
Created on 2014. 5. 27.

@author: cho
'''


from connector.FileServerConnector import FileServerConnector



class SocketFileServerConnector(FileServerConnector):
    '''
    classdocs
    '''


    def __init__(self):
        pass
        
    def connectToServer(self, ip, port):
        
        import socket
        
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        socket.connect((ip, port))
        
        return socket