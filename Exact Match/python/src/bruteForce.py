'''
Created on 06/10/2015

@author: raul
'''

class BruteForce(object):
    
    def bruteforce(self,text_file,pattern):
        occ=[]
        text_file1=open(text_file)
        m=len(pattern)
        for text in text_file1:
            j=0
            n=len(text)
            for i in range(n-m):
                while j<m and text[i+j]==pattern[j]:
                    j+=1
                if j==m:
                    occ.append(j)
                i+=1
                j=0
        print len(occ)
        text_file1.close()
        return occ
    

if "__main__"==__name__:
    bf=BruteForce()
    bf.bruteforce("big.txt","herself")
    bf.bruteforce("big.txt","ghost")
    bf.bruteforce("big.txt","independence")
    bf.bruteforce("big.txt","yourself")
    bf.bruteforce("big.txt","her")
    bf.bruteforce("big.txt","self")