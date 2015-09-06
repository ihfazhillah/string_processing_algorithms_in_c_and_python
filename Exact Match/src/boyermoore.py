'''
Created on 03/09/2015

@author: raul
'''
import numpy as np

class BoyerMoore(object):
    
    def badchar(self,pattern,alf):
        c={}
        for i in alf:
            pos=pattern.rfind(i)
            if pos==-1:
                c[i]=0
            else:
                c[i]=pos
        return c
    

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
    
    def b(self,pattern):
        m=len(pattern)
        goodsuffix=np.zeros(m,dtype=int)
        k=0
        for i in range(m):
            ps=self.proper_suffix(pattern[:i+1])
            pf=self.proper_prefix(pattern[:i+1])
            if not ps and not pf:
                goodsuffix[k]=0    
            longest_word=""
            for j in range(len(ps)):
                for l in range(len(pf)):
                    if ps[j]==pf[l] and len(ps[j])>len(longest_word):
                        longest_word=ps[j]
                        goodsuffix[k]=len(longest_word)
            k+=1
             
        return goodsuffix

    def goodsuffix(self,pattern):
        b=self.b(pattern)
        blinha=self.b(pattern[::-1])
        m=len(pattern)
        s=([m]*m)-b
        for l in range(m):
            j=m-blinha[l]-1
            if s[j]>l-blinha[l]:
                s[j]=l-blinha[l]
        return s
        
    def boyermoore(self,text_file,pattern,alf):
        occ=[]
        c=self.badchar(pattern,alf)
        s=self.goodsuffix(pattern)
        text_file1=open(text_file)
        for text in text_file1:
            text=text.strip("\n")
            n=len(text)
            m=len(pattern)
            i=0
            for i in range(len(text)):
                j=m
                while j>0 and i+j-1<n and text[i+j-1]==pattern[j-1]:
                    j-=1
                if j>0 and i+j-1<n:
                    i+=max(s[m-j],c[text[i+j-1]])
                elif j==0:
                    occ.append(i-(j-1))
        print len(occ)
        return occ

    
if "__main__"==__name__:
        bm=BoyerMoore()
        alf=[]
        for i in range(32,127):
            alf.append(chr(i))
        alf.append("\n")
        alf.append("\r")
        alf.append("\t")
        alf.append("\n\r")
        bm.boyermoore("big.txt","herself",alf)
        #bm.boyermoore("big.txt","ghost",alf)
        #bm.boyermoore("big.txt","independence",alf)
        