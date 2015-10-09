'''
Created on 06/09/2015

@author: raul
'''


class States(object):
    
    def __init__(self):
        pass
    
    def build(self,pattern,alf):
        m=len(pattern)
        tab={}
        for i in range(len(alf)):
            tab[(0,alf[i])]=0
        prev=0
        for j in range(m):
            prev=tab[(prev,pattern[j])]
            tab[(j,pattern[j])]=j+1
            for o in range(len(alf)):
                tab[(j+1,alf[o])]=tab[(prev,alf[o])]
        return tab
class AhoCorasick(object):
    
    
    def ac(self,text_file,pattern,alf):
        s=States()
        m=s.build(pattern, alf)
        cur=0
        occ=[]
        text_file1=open(text_file)
        for text in text_file1:
            n=len(text)
            for i in range(n):
                cur=m[(cur,text[i])]
                if cur==len(pattern):
                    occ.append(i-len(pattern)+1)
                    
        text_file1.close()
        print "%s-%d"%(pattern,len(occ))
                
        

if "__main__"==__name__:
    alf=[]
    for x in range(256):
        alf.append(chr(x))
    ac=AhoCorasick()
    ac.ac("big.txt","herself",alf)
    ac.ac("big.txt","ghost",alf)
    ac.ac("big.txt","independence",alf)
    