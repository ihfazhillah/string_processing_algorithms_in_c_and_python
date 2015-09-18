'''
Created on 06/09/2015

@author: raul
'''

class AhoCorasick(object):
    
    def ac(self,text_file,pattern_list,alf):
        s=States()
        g,f,o=s.build_fsm(pattern_list,alf)
        occ=[]
        text_file1=open(text_file)
        herself=0
        ghost=0
        independence=0
        yourself=0
        her=0
        self=0
        for text in text_file1:
            text=text.strip("\n")
            n=len(text)
            cur=0
            for i in range(n):
                try:
                    while not g.has_key((cur,text[i])):
                        cur=f[cur] 
                    cur=g[(cur,text[i])]
                    if cur==7:
                        herself+=1
                    elif cur==12:
                        ghost+=1
                    elif cur==24:
                        independence+=1
                    elif cur==3:
                        her+=1
                    elif cur==32:
                        yourself+=1
                    elif cur==36:
                        self+=1
                    for k in o[cur]:
                        occ.append(o[cur])
                except KeyError:
                    pass
        

        print "Total de ocorrencias"
        print len(occ)
        print "herself = %d\nher = %d\nghost = %d\nindependence = %d\nself = %d\nyourself = %d"%(herself,her,ghost,independence,self,yourself)
        return occ
        text_file1.close()

class States(object):


        
    def build_fsm(self,pattern_list,alf):
        g,o,t = self.build_goto(pattern_list,alf)
        #print "Mapa de transicao"
        #print g
        f,o = self.build_fail(g,o,t,pattern_list,alf)
        #print "Tabela O de ocorrencias de estado final"
        #print o
        #print "Tabela de Falha"
        #print f
        return (g,f,o)
    

    

              
    def build_goto(self,pattern_list,alf):
        g={}
        o={}
        nextstate=1
        newstate=0
        for k in range(len(pattern_list)):
            cur=0
            j=0
            for j in range(len(pattern_list[k])):
                try:
                    cur=g[(cur,pattern_list[k][j])]
                except KeyError:
                    newstate+=1
                    g[(cur,pattern_list[k][j])]=newstate
                    cur=g[(cur,pattern_list[k][j])]
                    nextstate=newstate

            for j in range(j,len(pattern_list[k])-1):
                nextstate+=1
                g[(cur,pattern_list[k][j])]=nextstate
                cur=nextstate
            o[cur]=[k]
        
        for a in alf:
            if not g.has_key((0,a)):
                g[(0,a)]=0
        totalstate=nextstate
        
        
        for a in alf:
            if not g.has_key((0,a)):
                g[(0,a)]=0 
        

        return (g,o,totalstate)
        
    def build_fail(self,g,o,totalstate,pattern_list,alf):
        q=[]
        f={}
        for i in range(1,totalstate+1):
            if not f.has_key(i):
                f[i]=-1
        for a in alf:
            if g[(0,a)]!=0:
                q.append(g[(0,a)])
                f[g[(0,a)]]=0
        
        while q:
            cur=q.pop(0)
            for a in alf:
                if g.has_key((cur,a)):
                    nextstate=g[(cur,a)]
                    q.append(nextstate)
                    b=f[cur]
                    while not g.has_key((b,a)):
                        b=f[cur]
                        g[(b,a)]=b

                    f[nextstate]=g[(b,a)]
                    if o.has_key(nextstate):
                            o[nextstate].append(f[nextstate])


        for i in range(1,totalstate+1):
            if f[i]==-1:
                f[i]=0
        return (f,o)
 

if "__main__"==__name__:
    alf=[]
    for i in range(32,127):
        alf.append(chr(i))
    alf.append("\n")
    alf.append("\r")
    alf.append("\t")
    alf.append("\n\r")
    ac=AhoCorasick()
    ac.ac("big.txt",["herself","ghost","independence","yourself","her","self"],alf)
