from Bio import SeqIO
count =0
fasta_sequences = SeqIO.parse(open('../raw/pos/uniprot-bacteriocin+keyword%3A_Antimicrobial+%5BKW-0929%5D_+mass%3A%5B_+TO+1--.fasta'),'fasta')
with open('../raw/pos/uniprot-bacteriocin+keyword%3A_Antimicrobial+%5BKW-0929%5D_+mass%3A%5B_+TO+1--_reg.fasta','w') as output:
    for i in fasta_sequences:
        seq = str(i.seq)
        name = i.id
        if 'X' in seq or 'Z' in seq or 'B' in seq or 'J' in seq or 'U' in seq or 'O' in seq:
            continue
        else:
            output.write('>'+name+'\n'+seq+'\n')