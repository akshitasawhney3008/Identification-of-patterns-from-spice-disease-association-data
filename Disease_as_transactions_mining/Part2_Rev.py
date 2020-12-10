import itertools
import random
import math

iterations = 100

file_association_rules = open('out(.25-1).txt', 'r')
rule_lines = file_association_rules.readlines()

sd_dict = {}
file_disease_to_spice = open('Spice_disease.tsv', 'r')
sd_lines = file_disease_to_spice.readlines()
for sd_line in sd_lines:
    temp = sd_line.split('\t')
    if temp[3].strip() in sd_dict:
        list_of_spices = sd_dict.get(temp[3].strip())
        list_of_spices.append(temp[1].strip())
        list_of_spices = list(set(list_of_spices))
        sd_dict[temp[3].strip()] = list_of_spices
    else:
        list_of_spices = []
        list_of_spices.append(temp[1].strip())
        sd_dict[temp[3].strip()] = list_of_spices

i = 0
dp_dict = {}
file_disease_to_phyto = open('Disease_to_phytochemical.tsv', 'r')
dp_lines = file_disease_to_phyto.readlines()
for dp_line in dp_lines:
    if i != 0:
        temp = dp_line.split('\t')
        if temp[4] in dp_dict:
            list_of_phyto = dp_dict.get(temp[4])
            list_of_phyto.append(temp[2].strip())
            list_of_phyto = list(set(list_of_phyto))
            dp_dict[temp[4]] = list_of_phyto
        else:
            list_of_phyto = []
            list_of_phyto.append(temp[2].strip())
            dp_dict[temp[4]] = list_of_phyto
    i += 1

j = 0
sp_dict = {}
sp_list = []
file_spice_to_phyto = open('Spice_to_phytochemical.tsv', 'r')
sp_lines = file_spice_to_phyto.readlines()
for sp_line in sp_lines:
    if j != 0:
        temp = sp_line.split('\t')
        if temp[0].strip() in sp_dict:
            list_of_phyto = sp_dict.get(temp[0].strip())
            list_of_phyto.append(temp[1].strip())
            sp_list.append(temp[1].strip())
            list_of_phyto = list(set(list_of_phyto))
            sp_dict[temp[0].strip()] = list_of_phyto
        else:
            list_of_phyto = []
            list_of_phyto.append(temp[1].strip())
            sp_list.append(temp[1].strip())
            sp_dict[temp[0].strip()] = list_of_phyto
    j += 1
sp_list = list(set(sp_list))

def get_phytochemical_count_after_mapping_to_spices(diseases, phyto_list):
    list_to_be_returned = []
    for phyto in phyto_list:
        flag = 0
        for disease in diseases:
            if disease in dp_dict:
                p_list = dp_dict.get(disease)
                if phyto not in p_list:
                    flag = 1
                    #list_to_be_returned.append(phyto)
                    break
            else:
                flag = 1
                break
        if flag == 0:
            list_to_be_returned.append(phyto)
    return list_to_be_returned

s_list = []
pc_list = []
zscore_list = []
for line in rule_lines:
    temp_list = line.split(' ==> ')
    temp_list_lhs = temp_list[0].split(';')
    temp_list_rhs = temp_list[1].split(', SUP')[0].split(';')
    diseases = temp_list_lhs + temp_list_rhs
    all_spices = []
    phytochemicals_from_spices = []
    phytochemicals_checked_from_diseases = []
    for disease in diseases:
        all_spices.append(sd_dict.get(disease))
    all_spices = list(set(list(itertools.chain.from_iterable(all_spices))))
    for spice in all_spices:
        if spice in sp_dict:
            extracted_phytochemical_list = sp_dict[spice]
            for pc in extracted_phytochemical_list:
                phytochemicals_from_spices.append(pc)
    phytochemicals_from_spices = list(set(phytochemicals_from_spices))

    # ZScore calculation
    mapped_phyto = get_phytochemical_count_after_mapping_to_spices(diseases, phytochemicals_from_spices)
    biological_count = len(mapped_phyto)
    number_of_random_samples = len(phytochemicals_from_spices)

    rand_list = []
    for k in range(0, iterations):
        phytochemicals_from_random_pick = []
        while len(phytochemicals_from_random_pick) != number_of_random_samples:
            phytochemicals_from_random_pick.append(random.choice(sp_list))
            phytochemicals_from_random_pick = list(set(phytochemicals_from_random_pick))
        mapped_random_phyto = get_phytochemical_count_after_mapping_to_spices(diseases, phytochemicals_from_random_pick)
        rand_list.append(len(mapped_random_phyto))
    list_sum = 0
    for elt in rand_list:
        list_sum += int(elt)
    mean = list_sum*1.0/iterations

    numerator = 0
    for elt in rand_list:
        numerator += (elt-mean)*(elt-mean)
    denominator = iterations-1
    std = math.sqrt(numerator*1.0/denominator)
    if std != 0:
        zscore = ((biological_count - mean)*1.0)/std
    else:
        zscore = 0
    zscore_list.append(zscore)

    sp = ''
    counter = 0
    for spice in all_spices:
        if counter != len(all_spices) - 1:
            sp += spice + ', '
        else:
            sp += spice + '->' + str(len(all_spices)) + '\n'
        counter += 1
    s_list.append(sp)
    pc = ''
    counter = 0
    for phyto in mapped_phyto:
        if counter != len(mapped_phyto) - 1:
            pc += phyto + ', '
        else:
            pc += phyto + '->' + str(len(mapped_phyto)) + '\n'
        counter += 1
    pc_list.append(pc)

output_file = open('Zscore.txt', 'w')
for it in range(0, len(zscore_list)):
    output_file.write(rule_lines[it] + '\n' + s_list[it] + pc_list[it] + str(zscore_list[it]) + '\n' + '\n')