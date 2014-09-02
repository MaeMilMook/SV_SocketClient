'''
Created on 2014. 5. 27.

@author: cho
'''

class ClientFileManager:
    '''
    classdocs
    '''


    def __init__(self, saveDir):
        self.__saveDir = saveDir
    
    def putFile(self, fileName, fileData):
        self.__fileWriter.putFile(self.__saveDir + fileName, fileData)
        
    def isFileExist(self, fileName):
        import os
        
        return os.path.isfile(os.path.join(self.__saveDir, fileName))
    
    def inputFileIndex(self, fileNameList):
        
        inputIdx = ''
    
        fileListCnt = len(fileNameList)
        
        while True:
            
            usrInput = input('choice file Number To Download : ')
            
            try:
                inputIdx = int(usrInput)
                
                if 0 <= inputIdx < fileListCnt:
                    
                    fileInfo = fileNameList[inputIdx]
                    
                    print('111111111',fileInfo['name'])
                    
                    if self.isFileExist(fileInfo['name']):
                        
                        print('the File you selected is already Exist as Same Name.', 'Do you want download?(Y or N)')
                        answer = input()
                        
                        print(answer.lower())
                        
                        # '==' 과 'is'는 다름. '==' 값비교, 'is' 포인터 비교 
                        if answer.lower() != 'y'.lower() :
                            # 음수(-1) 인덱스도 python에선 인식됨
                            inputIdx = -1
                            
                        break
                    else:
                        break
                else:
                    print('Out Of Index, please input number between 0 ~', fileListCnt)
                
            except Exception as e:
                 
                print('Error', e.args[0])
                
                print('please again input number.')
                continue
        
        return inputIdx
    
    def setFileWriter(self, fileWriter):
        self.__fileWriter = fileWriter