'''
Created on 2014. 6. 15.

@author: cho
'''

class ProgressiveBar(object):
    '''
    classdocs
    '''


    def __init__(self):
        pass
        
    def update_progress(self, progress):
        curPrgs = progress//10
        
        print('\r[{0}{1}] {2}%'.format('#'*curPrgs, ' '*(10 - curPrgs) ,progress) )