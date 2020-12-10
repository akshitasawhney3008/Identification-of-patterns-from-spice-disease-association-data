positive_file = open('l3_positive.tsv')
negative_file = open('l3_negative.tsv')

positive_lines = positive_file.readlines()
negative_lines = negative_file.readlines()

tot_pos = 0
positive_dict = {}
for line in positive_lines:
    temp = line.split('\t')
    spice = temp[1]
    count = temp[2]
    disease = temp[3]
    association = spice + ':' + disease
    positive_dict[association.strip()] = count
    tot_pos += int(count)

tot_neg = 0
negative_dict = {}
for line in negative_lines:
    temp = line.split('\t')
    spice = temp[1]
    count = temp[2]
    disease = temp[3]
    association = spice + ':' + disease
    negative_dict[association.strip()] = count
    tot_neg += int(count)

noise_list = []

for key_p, val_p in positive_dict.iteritems():
    for key_n, val_n in negative_dict.iteritems():
        if key_p == key_n:
            noise_list.append(key_p)

op1 = open('l3_positive_strategy_1.tsv', 'w')
on1 = open('l3_negative_strategy_1.tsv', 'w')

for key, val in positive_dict.iteritems():
    flag = 0
    for elt in noise_list:
        if elt == key:
            flag = 1
            break
    if flag == 0:
        op1.write(key + ' ' + str(val) + '\n')

for key, val in negative_dict.iteritems():
    flag = 0
    for elt in noise_list:
        if elt == key:
            flag = 1
            break
    if flag == 0:
        on1.write(key + ' ' + str(val) + '\n')

op2 = open('l3_positive_strategy_2.tsv', 'w')
on2 = open('l3_negative_strategy_2.tsv', 'w')

count1 = 0
count2 = 0
for key, val in positive_dict.iteritems():
    val = int(val)
    flag = 0
    for elt in noise_list:
        if key == elt:
            if val*1.0/tot_pos > int(negative_dict[key])*1.0/tot_neg:
                op2.write(key + ' ' + str(val) + '\n')
                count1 += 1
            flag = 1
            break
    if flag == 0:
        op2.write(key + ' ' + str(val) + '\n')
for key, val in negative_dict.iteritems():
    val = int(val)
    flag = 0
    for elt in noise_list:
        if key == elt:
            if val*1.0/tot_neg > int(positive_dict[key])*1.0/tot_pos:
                on2.write(key + ' ' + str(val) + '\n')
                count1 += 1
            flag = 1
            break
    if flag == 0:
        on2.write(key + ' ' + str(val) + '\n')

print ('PtoN ') + str(count1)
print ('NtoP ') + str(count2)