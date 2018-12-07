file1 = open('../raw/pos/positive.out','r')
file1_content = file1.read().strip('\n').split('Query= ')
file2 = open('../raw/pos/seq_dic.txt','r')
file2_content = file2.read().strip('\n').split('\n')
for query in range(1,len(file1_content)-1):
    query_list = file1_content[query].split('\n')
    a = str(query_list[0]).strip(' ').split('sequence_')
    a = int(a[1])
    for line in range(1,len(query_list)):
        if query_list[line].startswith('>'):
            title = str(query_list[line][2:]).strip(' ').split('sequence_')
            title = int(title[1])
            if a != title : #and a > title:
                list1 = query_list[line+5].split(',')
                if list1[0] == '***** No hits found *****':
                    break
                list2 = list1[1].split('=')
                expect = float(str(list2[1]).strip(' '))
                list3 = query_list[line+6].split(',')
                list4 = list3[0].split('=')
                ident_list = str(list4[1]).strip(' ').split(' ')
                ident = str(ident_list[0])
                ident = ident.split('/')
                identity = float(ident[0])/float(ident[1])
                if expect < 1e-20 and identity > 0.7:
                    try:
                        file2_content.remove('sequence_'+str(a))
                    except ValueError:
                        pass
                    continue
print(len(file2_content))
file3 = open('../raw/pos/identity50_p_seq.txt','w')
for j in file2_content:
    file3.write(">"+j+"\n")