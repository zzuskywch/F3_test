import os
from sys import argv
popu1=argv[2]
target=argv[1]
fuhao=1
if '-' in argv[3]:

        infile=open('/home/wangchenghu/somepy/002.han_taiwan/qp3pop/002.logfile3.r.sort','r')
#       order=""
#002.logfile3.r.sort' 是Guangdongs 而logfile3.r.zhenghao.sort是gdsouth
        outfile1=open('target_'+target+'.-'+popu1+'.rscript','w')
        outfile=open('target_'+target+'.-'+popu1+'.rfile','w')
        fuhao=-1
else:
        infile=open('/home/wangchenghu/somepy/002.han_taiwan/qp3pop/002.logfile3.r.zhenghao.sort','r')
import os
from sys import argv
popu1=argv[2]
target=argv[1]
fuhao=1
if '-' in argv[3]:

        infile=open('/home/wangchenghu/somepy/002.han_taiwan/qp3pop/002.logfile3.r.sort','r')
#       order=""
#002.logfile3.r.sort' 是Guangdongs 而logfile3.r.zhenghao.sort是gdsouth
        outfile1=open('target_'+target+'.-'+popu1+'.rscript','w')
        outfile=open('target_'+target+'.-'+popu1+'.rfile','w')
        fuhao=-1
else:
        infile=open('/home/wangchenghu/somepy/002.han_taiwan/qp3pop/002.logfile3.r.zhenghao.sort','r')
        outfile=open('target_'+target+'.'+popu1+'.rfile','w')
        outfile1=open('target_'+target+'.'+popu1+'.rscript','w')
        fuhao=1
#       order="-"
##logfile4 he 4.1  target那一列  不对劲
popu1=argv[2]
target=argv[1]
#zhi=float(argv[3][1:])
count=0

#outfile=open('target_'+target+'.'+popu1+'.rfile','w')
#infile=open('/picb/humpopg-bigdata5/wangchenghu/converge.han_taiwan/002.qp3test/rfile/'+target+'.target','r')
for line in infile:
        l=line.split('\t')
        #if len(l)<7:
        #       continue
#       print (l)
#       if zhi==0:
        if l[1]==popu1 and l[3]==target :
                l = line.replace("gdsouth", "Guangdongs")
                if 'AX-AI' in l:
                        continue                        
                outfile.write(l)
                count+=1
                if count>=abs(int(argv[3])):
                        break
#       break
        else:
                continue
                

infile.close()
outfile.close()


#outfile1=open('target_'+target+'.'+popu1+'.rscript','w')
outfile1.write('library(ggplot2)\n')
if fuhao<0:
        outfile1.write('data<-read.csv("target_'+target+'.-'+popu1+'.rfile",sep = "\t",header = F,col.names=c("result","PopA", "PopB", "PopC", "F3", "StdErr", "Z", "SNPs"))\n')
else:
        outfile1.write('data<-read.csv("target_'+target+'.'+popu1+'.rfile",sep = "\t",header = F,col.names=c("result","PopA", "PopB", "PopC", "F3", "StdErr", "Z", "SNPs"))\n')
outfile1.write('data2<-data[order(-data$F3),]\n')
outfile1.write('poplist<-data2$PopB\n')

outfile1.write('p <- ggplot(data2)+geom_point(mapping = aes(x = factor(PopB,level = poplist), y = F3),color="red",size = 3,alpha =0.8)+geom_errorbar(aes(x=factor(PopB,level = poplist),ymin=F3-StdErr, ymax=F3+StdErr), width=.3)+theme_classic()+coord_flip()+scale_y_continuous(position = "right")+theme(axis.title.y = element_blank())+ylab( expression( plain(paste(italic(f),"3 ('+target+';'+popu1+', X)")) ) )\n')
outfile1.write('ggsave(filename = "target_'+target+'.'+popu1+'.'+argv[3]+'.pdf",width = 9,height=6)\n')

outfile1.close()
if fuhao<0:
        os.system('Rscript target_'+target+'.-'+popu1+'.rscript')
else:
        os.system('Rscript target_'+target+'.'+popu1+'.rscript')
~
