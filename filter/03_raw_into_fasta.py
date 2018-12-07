from Bio import SeqIO
count =0
dic = {}
fasta_sequences = SeqIO.parse(open('../raw/pos/combined2.fasta'),'fasta')
for i in fasta_sequences:
    seq = str(i.seq)
    name = i.id
    dic[seq] =  name
file_list =  sorted(dic, key=len, reverse=True)
file2 = open('../raw/pos/positive.txt','w')
file3 = open('../raw/pos/p_name.txt','w')
seqli = list(dic.keys())
for i in range(len(file_list)):
    seq = seqli[i]
    name = dic[seq]
    file2.write(">sequence_"+str(i+1)+"\n"+seq+"\n")
    file3.write(name+'\t'+">sequence_"+str(i+1)+"\n")
    count+=1
    complete = int(round(count/len(file_list),2)*100)
    if count%1000==0:
        print('stillwork',count,str(complete)+'%')
