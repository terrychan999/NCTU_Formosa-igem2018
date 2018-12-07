from Bio import SeqIO
count =0
seq_list = []
name_list = []
fasta_sequences = SeqIO.parse(open('../raw/pos/combined.fasta'),'fasta')
for i in fasta_sequences:
    seq = str(i.seq)
    name = i.id
    seq_list.append(seq)
    name_list.append(name)
exist_seq = []
with open('../raw/pos/combined2.fasta','w') as output:
    for i in range(len(seq_list)):
        seq = seq_list[i]
        name = name_list[i]
        if seq not in exist_seq:
            exist_seq.append(seq)
            output.write('>'+name+'\n'+seq+'\n')
        count+=1
        complete = int(round(count/len(seq_list),2)*100)
        if count%1000==0:
            print('stillwork',count,str(complete)+'%')
print(len(seq_list),len(exist_seq))