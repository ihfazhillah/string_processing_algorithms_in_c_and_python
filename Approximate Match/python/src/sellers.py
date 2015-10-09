'''
Created on 29/09/2015

@author: raul
'''
import numpy as np
class Sellers(object):
    
    def sellers(self,text_file,pattern,distance):
        m=len(pattern)
        text_file1=open(text_file)
        occ=[]
        text1=""
        for text in text_file1:
            text1+=text
            
        n=len(text1)
        d=np.zeros((m+1,n+1),dtype=int)
        for i in range(m+1):
            d[i,0]=i
        for j in range(1,n+1):
            d[0,j]=0
            for i in range(1,m+1):
                d[i,j]=min(d[i-1,j-1]+self.fi(pattern[i-1],text1[j-1]),d[i,j-1]+1,d[i-1,j]+1)
            if d[m,j]<=distance:
                occ.append(j)
        text_file1.close()      
        print len(occ)
    
    def fi(self,pattern,text):
        if pattern==text:
            return 0
        else:
            return 1

if "__main__"==__name__:
    s=Sellers()
    s.sellers("big.txt","independence",2)
    s.sellers("big.txt","herself",2)
    s.sellers("big.txt","ghost",2)