file1 = open('../raw/pos/positive.txt','r') #fasta_raw
file1_content = file1.read().strip('\n').split('\n')
file2 = open('../raw/pos/identity50_p_seq.txt','r') #identity
file2_content = file2.read().strip('\n').split('\n')
file3 = open('postitveseq1014.txt','w') #output

k = 1 #positive = 1, negative = 0
for i in range(len(file2_content)):
    for j in range(len(file1_content)):
        if file2_content[i] == file1_content[j]:
            file3.write(file1_content[j+1]+'\t'+str(k)+'\n') 