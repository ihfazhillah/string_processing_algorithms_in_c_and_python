'''
Created on 18/09/2015

@author: raul
'''


class ShiftOR(object):
    
    def shiftor(self,text_file,pattern,alf):
        cm=self.char_mask(pattern,alf)
        m=len(pattern)
        occ=[]
        msb=1<<(m-1)
        s=[(1<<m)-1]
        text_file1=open(text_file)
        for text in text_file1:
            text=text.strip("\n")
            for i in range(len(text)):
                letter=text[i]
                s= (s<<1) | cm[letter]
                if ((s[0] & ((1<<m)-1)))<msb:  
                    occ.append(i)         
                
                
        print len(occ)
        text_file1.close()
        return occ
        
    
    def char_mask(self,pattern,alf):
        c={}
        for a in alf:
            c[a]=~0
        for i in range(len(pattern)):
            letter=pattern[i]
            c[letter] &=~(1<<i)
        return c   
    
    
if "__main__"==__name__:
    alf=[]
    for x in range(256):
        alf.append(chr(x))
    shor=ShiftOR()
    shor.shiftor("big.txt","herself",alf)
    shor.shiftor("big.txt","independence",alf)
    shor.shiftor("big.txt","ghost",alf)
    shor.shiftor("big.txt","yourself",alf)