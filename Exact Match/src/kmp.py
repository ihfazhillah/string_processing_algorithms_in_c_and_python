'''
Created on 01/09/2015

@author: raul
'''
import numpy as np

class KMP(object):

    def __init__(self,text_file,pattern):
        self.kmp(text_file,pattern)
        
    
    def kmp(self,text_file,pattern):
        occ=[]
        log=open("log.txt","w")
        next_kmp=self.kmpnext(pattern)
        text_file1=open(text_file)
        for text in text_file1:
            text=text.strip("\n")
            n=len(text)
            m=len(pattern)
            i,j=0,0
            for i in range(len(text)):
                while j>0 and text[i]!=pattern[j]:
                    j=max(0,next_kmp[j])
                if pattern[j]==text[i]:
                    j+=1
                    if j==m:
                        occ.append(i-(j - 1))
                        log.write("%s\n%d\n" %(text,len(occ)))
                        log.flush()
                        j=0      
         
                    
        log.close()
        print "%s - %d"%(pattern,len(occ))
        return occ
    
    def proper_suffix(self,pattern):
        ps_return=[]
        m=len(pattern)
        for i in range(m-1):
            ps_return.append(pattern[i+1:])
        return ps_return
        
    def proper_prefix(self,pattern):
        pp_return=[]
        m=len(pattern)
        for i in range(m-1):
            pp_return.append(pattern[:i+1])
        return pp_return
    
    def kmpnext(self,pattern):
        m=len(pattern)
        kmpnext=-np.ones(m,dtype=int)
        k=0
        for i in range(1,m+1):
            ps=self.proper_suffix(pattern[:i])
            pf=self.proper_prefix(pattern[:i])
            if not ps and not pf:
                kmpnext[k]=0
                
            longest_word=""
            found=False
            flag=False
            for j in range(len(ps)):
                for l in range(len(pf)):
                    if ps[j]==pf[l] and len(ps[j])>len(longest_word):
                        longest_word=ps[j]
                        try:
                            if longest_word[-1]!=pattern[k+1]:
                                kmpnext[k]=0
                                flag=True
                        except IndexError:
                            pass
                        if not found and not flag:
                            found=True
                        
            if found:
                kmpnext[k]=len(longest_word)
            k+=1     
        return kmpnext
        


if "__main__"==__name__:
        kmp=KMP("big.txt","ghost")
        kmp=KMP("big.txt","herself")
        kmp=KMP("big.txt","independence")

        
    