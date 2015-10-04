'''
Created on 29/09/2015

@author: raul
'''


class Ukkonen(object):
    
    def ukkonen(self,text_file,pattern,alf,distance):
        a=self.build_ukk_fsm(pattern, distance, alf)
        s=range(len(pattern)+1)
        occ=[]
        m=len(pattern)
        delta=a[2]
        acc_states=a[4]
        if m<=distance:
            occ.append(0)
        text_file1=open(text_file)
        for text in text_file1:
            for i in range(len(text)):
                s=delta[(tuple(s),text[i])]
                
                if acc_states.count(s)>0:
                    occ.append(i)
        print len(occ)
    
    def build_ukk_fsm(self,pattern,distance,alf):
        m=len(pattern)
        q0=range(m+1) 
        i=0 
        trans={}
        trans[tuple(q0)]=i #index(S)
        Q=[] #nova fila 
        Q.append(q0)
        n=[]
        n.append(q0)
        f=[]
        delta={}
        if m<=distance:
            f.append(0)
        while n:
            col=n.pop(0)
            for a in alf:
                s=self.next_column(col, pattern, a, distance)
                if Q.count(s)==0:
                    Q.append(s)
                    n.append(s)
                    trans[tuple(s)]=i
                    i+=1
                    m=s[-1]
                    if m<=distance:
                        f.append(tuple(s))
                delta[tuple(col),a]=tuple(s)
  
        return (q0,alf,delta,trans,f)
    
    def next_column(self,slinha,pattern,a,distance):
        s=[]
        for i in range(len(pattern)+1):
            s.append(0)
        for i in range(1,len(pattern)+1):
            minimo=min(slinha[i-1]+self.fi(pattern[i-1],a),slinha[i]+1,s[i-1]+1,distance+1)
            s[i]=minimo
        return s
    def fi(self,pattern,letter):
        if pattern==letter:
            return 0
        else:
            return 1       
if "__main__"==__name__:
    alf=[]
    for x in range(256):
        alf.append(chr(x))  
    u=Ukkonen()
    u.ukkonen("big.txt","independence",alf,2)
    u.ukkonen("big.txt","herself",alf,2)
    u.ukkonen("big.txt","ghost",alf,2)
