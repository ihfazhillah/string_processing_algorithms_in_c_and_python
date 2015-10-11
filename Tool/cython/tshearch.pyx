import argparse
import sys
import glob
from kmp import KMP
from wumanber import WuMamber

def main():
    '''Instanciando um parser dos argumentos passados pela linha de comando'''
    parser=argparse.ArgumentParser()
    
    '''Adicionar um argumento para o parser para receber arquivos textos'''
    parser.add_argument("-i","--input",nargs="+",help="text file input")
    parser.add_argument("-e","--edit",help="maximum edit distance")
    parser.add_argument("-c","--count",action='store_true',help="count number of occurrences")
    parser.add_argument("-p","--pattern",help="pattern file")
    args=parser.parse_args()

    if not args.input:
        usage()
        sys.exit()
    else:
        alf=[]
        for i in range(250):
            alf.append(chr(i))

        if not args.edit and args.count and args.pattern:
            for i in args.input:
                inp=glob.glob(i)
                for j in inp:
                    patterns=open(args.pattern).readlines()
                    for p in patterns:
                        KMP(j,p.strip("\n"))
        #elif not args.edit and args.pattern and args.pattern:
        #    for i in args.input:
        #        inp=glob.glob(i)
        #        for j in inp:
        #            Shor(args.pattern,j,0,alf)
        elif args.edit and args.count and args.pattern:
            for i in args.input:
                inp=glob.glob(i)
                for j in inp:
                    patterns=open(args.pattern).readlines()
                    for p in patterns:
                        wm=WuMamber()
                        wm.wumamber(j,p,alf,int(args.edit))
                    	#WB(args.pattern,j,1,alf,args.edit)
        #elif args.edit and args.pattern!="" and len(args.input)>0:
        #    for i in args.input:
        #        inp=glob.glob(i)
        #        for j in inp:
        #            WB(args.pattern,j,0,alf,args.edit)
            







def usage():
    print "Usage: tsearch -p <pattern_file> -i [texts_files] [-c] [-e] <edit distance>"
    
if __name__=="__main__":
    main()