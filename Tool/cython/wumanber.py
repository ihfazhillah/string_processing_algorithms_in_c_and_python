'''
Created on 25/09/2015

@author: raul
'''

class WuMamber(object):
    
    def wumamber(self,text_file,pattern,alf,q):
        q=int(q)
        cm=self.char_mask(pattern,alf)
        m=len(pattern)
        msb=1<<(m-1)
        s=[(1<<m)-1]
        occ=[]
        for k in range(1,q+1):
            s.append(s[k-1]<<1)
        text_file1=open(text_file)
        for text in text_file1:
            for i in range(len(text)):
                letter=text[i]
                stemp=s[0]
                s[0]=(s[0]<<1) | cm[letter]
                
                for k in range(1,q+1):
                    stemp2=s[k]
                    s[k]=((s[k]<<1) | cm[letter]) & (stemp<<1) & (s[k-1]<<1) & stemp
                    stemp=stemp2
                if ((s[q] & ((1<<m)-1)))<msb:
                    occ.append(i)
        text_file1.close()
        print len(occ)
        
    def char_mask(self,pattern,alf):
        c={}
        one=1
        pos_mask=~one
        for a in alf:
            c[a]=~0
        for i in range(len(pattern)):
            letter=pattern[i]
            c[letter] &=pos_mask
            pos_mask=(pos_mask<<1) | one
        return c   
    
'''
if "__main__"==__name__:
    alf=[]
    for x in range(256):
        alf.append(chr(x))
        
    wm=WuMamber()
    wm.wumamber("big.txt","independence",alf,2)
    wm.wumamber("big.txt","herself",alf,2)
    wm.wumamber("big.txt","ghost",alf,2)
'''    
